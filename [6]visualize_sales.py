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
