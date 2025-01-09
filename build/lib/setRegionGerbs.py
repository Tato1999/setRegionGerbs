import requests
import os

# Base URL for downloading flags
BASE_URL = "https://flagcdn.com/w320"

class SetRegionGerbs:
    def __init__(self, regIso=None, formatType="png") -> None:
        """
        Initialize the class with region ISO codes and format type.
        :param regIso: List of region ISO codes (default: empty list).
        :param formatType: File format for the images (default: 'png').
        """
        self.regIso = regIso if regIso else []
        self.formatType = formatType
        self.dirForFlag = "gerb_folder"

    def make_dir(self):
        """
        Create a directory for storing flags if it doesn't already exist.
        """
        os.makedirs(self.dirForFlag, exist_ok=True)
        return f"{self.dirForFlag} created or already exists."

    def get_region_gerbs(self):
        """
        Download flags for all regions in `self.regIso`.
        """
        if not self.regIso:
            return "No region ISO codes provided."

        self.make_dir()  # Ensure the directory exists

        for iso in self.regIso:
            url = f"{BASE_URL}/{iso.lower()}.{self.formatType}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    file_path = f"{self.dirForFlag}/{iso.lower()}.{self.formatType}"
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded flag for {iso}.")
                else:
                    print(f"Failed to download flag for {iso}: {response.status_code}")
            except Exception as e:
                print(f"Error while downloading flag for {iso}: {e}")

        return "All flags processed."