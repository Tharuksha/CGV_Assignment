import matplotlib.pyplot as plt
import os
import ast

def get_file_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)
def validate_summary_data(summary):
    if not isinstance(summary, dict):
        raise ValueError("The summary data is not in the correct format. Expected a dictionary.")
    if "items" not in summary:
        raise ValueError("The summary data does not contain 'items'.")
    if not isinstance(summary["items"], list):
        raise ValueError("'items' should be a list.")
    for item in summary["items"]:
        if not all(k in item for k in ("name", "price")):
            raise ValueError("Each item must contain 'name' and 'price' keys.")

import matplotlib.pyplot as plt

def visualize_sales(summary):
    # Validate the summary data before proceeding
    validate_summary_data(summary)
    
    items = [item["name"] for item in summary["items"]]
    prices = [float(item["price"]) for item in summary["items"]]

    if not items or not prices:
        raise ValueError("The list of items or prices is empty. Cannot generate a graph.")
    
    # Plot sales summary as a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(items, prices, color='blue')
    plt.xlabel('Items')
    plt.ylabel('Prices (Currency)')
    plt.title('Sales Summary')
    plt.show()

# Rotate item labels to avoid overlap if there are many items
plt.xticks(rotation=45, ha="right")
