import json
import os
from pathlib import Path
from typing import Dict, List

from elasticsearch import Elasticsearch


def fetch_data_to_file(config_fpath: Path, out_fpath: Path):
    """Fetches data from Elastic into a .jsonl file
    This is a helper function to fetch data from Elastic and write it to a file.

    Parameters
    ----------
    config_fpath : Path
        Path to the config file containing relevant elastic and data config
    out_fpath : Path
        Destination .jsonl file path to write fetched data

    config_fpath contains data in the following format:
        {
          "elastic":{
            "server":{
              "number_of_hits": 100
            },
            "data":{
              "fetch":{
                "date_from": "2021-08-16",
                "date_to": "2021-08-20"
              },
            }
          }
        }
    """

    # Parse Config
    with open(config_fpath, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    # Create elastic client
    elastic_client = Elasticsearch(
        cloud_id=os.environ.get("ELK_CLOUD_ID"),
        api_key=(os.environ.get("ELK_API_KEY_ID"), os.environ.get("ELK_API_KEY")),
    )

    # Fetch needed documents
    retrieved_list = fetch_documents(
        elastic_client=elastic_client,
        nb_hits=config["elastic"]["server"]["number_of_hits"],
        date_field=config["elastic"]["data"]["fetch"]["date_field"],
        start_date=config["elastic"]["data"]["fetch"]["date_from"],
        end_date=config["elastic"]["data"]["fetch"]["date_to"],
    )

    write_documents_to_file(retrieved_docs=retrieved_list, out_fpath=out_fpath)


def fetch_documents(
    elastic_client: Elasticsearch,
    nb_hits: int,
    date_field: str,
    start_date: str,
    end_date: str,
) -> List[Dict]:
    """Fetch Elastic Documents in a specific date timeframe
    Parameters
    ----------
    elastic_client : Elasticsearch
        Elastic Client connected to the server
    nb_hits : int
        Number of hits per query
    date_field : str
        Date field to filter on
    start_date : str
        Start Date
    end_date : str
        End Date
    Returns
    -------
    List[Dict]
        List of the _source key of each Elastic Document
    """
    search_query_body = {
        "size": nb_hits,
        "query": {
            "bool": {
                "must": [
                    {"range": {date_field: {"gte": start_date, "lte": end_date}}},
                ]
            }
        },
    }

    search_result = elastic_client.search(body=search_query_body, scroll="1m")

    # Store initially retrieved docs (before scrolling)
    retrieved_documents_list: List[Dict] = [
        doc["_source"] for doc in search_result["hits"]["hits"]
    ]

    scroll_id = search_result["_scroll_id"]

    print("The scroll id for the search request is:" + scroll_id)

    scroll_query_body = {"scroll": "1m", "scroll_id": scroll_id}
    scroll_result = elastic_client.scroll(body=scroll_query_body)
    retrieved_scroll_hits = scroll_result["hits"]["hits"]

    while len(retrieved_scroll_hits) > 0:
        scroll_result = elastic_client.scroll(body=scroll_query_body)
        retrieved_scroll_hits = scroll_result["hits"]["hits"]
        for doc in retrieved_scroll_hits:
            retrieved_documents_list.append(doc["_source"])

    # Clear the scroll
    elastic_client.clear_scroll(scroll_id=scroll_id)

    return retrieved_documents_list


def write_documents_to_file(retrieved_docs: List, out_fpath: Path) -> bool:
    """Write a list of dicts into a .jsonl file
    Parameters
    ----------
    retrieved_docs : List of elastic documents
    out_fpath : Path
        Output file path
    """
    try:
        with open(out_fpath, "w", encoding="utf-8") as out_file:
            for doc in retrieved_docs:
                out_file.write(json.dumps(doc))
                out_file.write("\n")
        return True
    except Exception as e:
        print(f"Error while writing to file: {e}")
        return False
