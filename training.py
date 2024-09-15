import pandas as pd
from src.utils import download_images
import os


def open_csv_file(file_path, download_folder):
    df = pd.read_csv(file_path)

    # required_columns = {"index", "image_link", "group_id", "entity_name", "entity_value"}
    required_columns = {"index", "image_link", "group_id", "entity_name"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing columns: {required_columns}")

    image_links = df["image_link"].dropna().tolist()

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        download_images(image_links, download_folder)
        print("All images downloaded successfully.")
    except Exception as e:
        print(f"An error occurred while downloading images: {e}")


if __name__ == "__main__":
    file_path = ""
    download_folder = ""
    open_csv_file(file_path, download_folder)
