import typer

"""
Reference:
    https://typer.tiangolo.com/
"""
app = typer.Typer()


@app.command()
def function_1():
    print("Called function 1")


@app.command()
def function_2():
    print("Called function 2")


if __name__ == "__main__":
    app()
