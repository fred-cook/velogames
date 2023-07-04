from bs4 import BeautifulSoup, Tag
import pandas as pd

class ParseVelogames:
    """
    Given some soup from a velogames league which has happened
    extract riders:
        - Names
        - Teams
        - Type
        - Price
        - Points
    and return the leage as a Pandas DataFrame
    """
    def __init__(self):
        # Hard coded values from inspection of the site
        self.html_rows = {1: "name",
                          #2: "team",
                          3: "type",
                          4: "price",
                          #5: "percent_selected",
                          6: "points"}
        
    def table_to_dicts(self, soup: BeautifulSoup
                       ) -> list[dict[str, str]]:
        """
        Return a list of dictionaries for each rider
        """
        table = soup.find("tbody")
        riders = table.findAll("tr")
        return [
            {column: rider.findAll("td")[index]
             for index, column in self.html_rows.items()}
             for rider in riders
        ]

