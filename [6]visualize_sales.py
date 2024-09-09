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

    # Rotate item labels to avoid overlap if there are many items
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    script_dir = os.path.dirname(os.path.abspath(__file__))
    graph_folder = os.path.join(script_dir, "visualization")
    os.makedirs(graph_folder, exist_ok=True)
    plt.savefig(os.path.join(graph_folder, "sales_summary.png"))
    plt.show()

def main():
    summary_path = get_file_path(os.path.join("summary", "receipt_summary.txt"))

    if not os.path.exists(summary_path):
        raise FileNotFoundError(f"The file {summary_path} does not exist. Please run the summarization script first.")
    
    # Read the summary data from the file
    with open(summary_path, "r") as summary_file:
        try:
            summary = ast.literal_eval(summary_file.read())  # Safely evaluate the string as a Python dictionary
        except (SyntaxError, ValueError) as e:
            raise ValueError("Failed to parse the summary file. Ensure it's in valid dictionary format.") from e
    
    # Visualize sales based on the summary data
    visualize_sales(summary)

if __name__ == "__main__":
    main()
