import os
import sys
import json
import pymongo
from dotenv import load_dotenv

import pandas as pd 
import numpy as np 
from src.logger import logging
from src.exception import MyException

load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
# print(MONGO_DB_URL) # printing for verifying if it's able to retrieve from .env or not

import certifi
ca=certifi.where()

class VehicleDataExtract():
    """
    A class to extract, transform, and load network data into MongoDB.

    This class provides methods to:
    - Convert a CSV file into JSON records.
    - Insert JSON records into a specified MongoDB database and collection.
    """

    def __init__(self) -> None:
        """
        Initializes the VehicleDataExtract class.

        Handles any initialization requirements. Currently, it does not initialize any instance variables.
        
        Raises:
            MyException: If an error occurs during initialization.
        """
        try:
            pass
        except Exception as e:
            raise MyException(e,sys)
        
    def csv_to_json(self,file_path):
        """
        Converts a CSV file into a list of JSON records.

        Parameters:
            file_path (str): The path to the CSV file to be converted.

        Returns:
            list: A list of JSON records extracted from the CSV file.

        Raises:
            MyException: If an error occurs while reading or transforming the CSV file.
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            logging.info("Successfully converted data from csv to json")
            return records

        except Exception as e:
            raise MyException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        """
        Inserts JSON records into a MongoDB database and collection.

        Parameters:
            records (list): The list of JSON records to be inserted.
            database (str): The name of the MongoDB database.
            collection (str): The name of the MongoDB collection.

        Returns:
            int: The number of records successfully inserted.

        Raises:
            MyException: If an error occurs while interacting with the MongoDB database.
        """
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            logging.info("Started inserting data into MongoDB")
            self.collection.insert_many(self.records)
            logging.info("Inserted data into MongoDB")
            return(len(self.records))
        
        except Exception as e:
            raise MyException(e,sys)
        

if __name__=="__main__":
    file_path="notebook/data.csv"
    database="Proj1"
    collection="Proj1-Data"

    network_obj = VehicleDataExtract()
    records = network_obj.csv_to_json(file_path=file_path)
    no_of_records=network_obj.insert_data_to_mongodb(records,database,collection)
    print(no_of_records)
    # print(records)




# "Below line of code is used to verify if connection has been made successfully or not"
# from pymongo.mongo_client import MongoClient

# # Create a new client and connect to the server
# client = MongoClient(MONGO_DB_URL)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)