import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
    Source:
        https://medium.com/@dtuk81/confusion-matrix-visualization-fc31e3f30fea
"""


def plot_confusion_matrix(cf,
                          group_names=True,
                          categories='auto',
                          count=True,
                          percent=True,
                          cbar=True,
                          xy_ticks=True,
                          sum_stats=True,
                          cmap=plt.cm.Blues,
                          title="Confusion Matrix"):
    blanks = ['' for _ in range(cf.size)]
    names = ["True Neg", "False Pos", "False Neg", "True Pos"]

    if group_names and len(names) == cf.size:
        group_labels = ["{}\n".format(value) for value in names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    if percent:
        group_percentages = ["{0:.2%}".format(value) for value in cf.flatten() / np.sum(cf)]
    else:
        group_percentages = blanks

    box_labels = [f"{v1}{v2}{v3}".strip() for v1, v2, v3 in zip(group_labels, group_counts, group_percentages)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    # CODE TO GENERATE SUMMARY STATISTICS & TEXT FOR SUMMARY STATS
    if sum_stats:
        # Accuracy is sum of diagonal divided by total observations
        accuracy = np.trace(cf) / float(np.sum(cf))

        # if it is a binary confusion matrix, show some more stats
        if len(cf) == 2:
            # Metrics for Binary Confusion Matrices
            precision = cf[1, 1] / sum(cf[:, 1])
            recall = cf[1, 1] / sum(cf[1, :])
            f1_score = 2 * precision * recall / (precision + recall)
            stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy, precision, recall, f1_score)
        else:
            stats_text = "\n\nAccuracy={:0.3f}".format(accuracy)
    else:
        stats_text = ""

    if not xy_ticks:
        categories = False

    plt.figure(figsize=(10, 8))
    sns.heatmap(cf, annot=box_labels, fmt="", cmap=cmap, cbar=cbar, xticklabels=categories, yticklabels=categories)

    plt.ylabel('True label')
    plt.xlabel('Predicted label' + stats_text)
    plt.colorbar()
    plt.title(title)
    plt.show()
