import pandas as pd
from pandas import DataFrame
#from FileUtil import FileUtil

class DataFrameToCSV:

    def __init__(self, product_name, product_rating, product_price):
        self._product_name = product_name
        self._product_rating = product_rating
        self._product_price = product_price
        self._filename = 'FlipkartProducts.xlsx'

    def scrapped_data_to_file(self):
        _create_dataframe = self.create_dataframe()
        _final_file = self.write_file(_create_dataframe)
        return _final_file

    def create_dataframe(self):
        return pd.DataFrame({'Product Name': self._product_name,
                             'Product Price': self._product_price,
                             'Product Rating': self._product_rating})

    def write_file(self, dataframe):
        writer = pd.ExcelWriter(self._filename)
        dataframe.to_excel(writer, sheet_name='Product Above 4.5 rating')
        return writer.save()
