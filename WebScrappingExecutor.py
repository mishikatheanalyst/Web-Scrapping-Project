from Scrapper import Scrapper
from SSLConnection import SSLConnection
from DataFrameToCSV import DataFrameToCSV


class WebScrappingExecutor:
    def __init__(self):
        self._ssl_connection = SSLConnection()
        self._internet_scrapper = Scrapper()
        self.product_name, self.product_rating, self.product_price =self._internet_scrapper.information_scrapper()
        self._dataframetocsv = DataFrameToCSV(self.product_name, self.product_rating, self.product_price)

    def web_scrapping_executor(self):
        self._ssl_connection.ssl_connection()
        return self._dataframetocsv.scrapped_data_to_file()
