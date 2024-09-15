import pandas as pd
import re
from src.constants import *
from src.utils import download_images


def extract_entity_value(text, entity):
    unit_pattern = r'(\d+\.?\d*)\s*(' + '|'.join(re.escape(unit) for unit in entity_unit_map.get(entity, [])) + r')'
    
    match = re.search(unit_pattern, text.lower())
    
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        return f"{value} {unit}"
    
    return ""


def open_csv_and_extract_info(file_path, entities_to_search):
    df = pd.read_csv(file_path)

    required_columns = {"index", "image_link", "group_id", "entity_name", "entity_value"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing columns: {required_columns}")

    for index, row in df.iterrows():
        image_link = row["image_link"]
        entity_name = row["entity_name"]
        entity_value = row["entity_value"]

        if entity_name in entities_to_search:
            if pd.notna(image_link):
                try:
                    download_images(image_link)
                    print(f"Successfully downloaded image from: {image_link}")
                except Exception as e:
                    print(f"Failed to download image from {image_link}.\nError: {e}")

            extracted_value = extract_entity_value(entity_value, entity_name)

            print(f"Index: {index}")
            print(f"Entity Name: {entity_name}")
            print(f"Extracted Value: {extracted_value}")
            print(f"Other Info: {entity_value}")
            print("------------")


if __name__ == "__main__":
    file_path = ""      # file path goes here
    entities_to_search = []  # List of entities to search

    open_csv_and_extract_info(file_path, entities_to_search)
