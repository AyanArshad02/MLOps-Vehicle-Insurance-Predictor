from abc import ABC, abstractmethod

import pandas as pd


# Abstract Base Class for Data Inspection Strategies
# --------------------------------------------------
# This class defines a common interface for data inspection strategies.
# Subclasses must implement the inspect method.

# Abstract Base Class for Data Inspection Strategies
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass


# Concrete Strategy for Data Types Inspection
# --------------------------------------------
# Subclass of DataInspectionStrategy that inspects the data types of each column (subclass implementing the abstract method).
# This strategy inspects the data types of each column and counts non-null values.
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())


# Concrete Strategy for Summary Statistics Inspection
# -----------------------------------------------------
# This strategy provides summary statistics for both numerical and categorical features.
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))


# Concrete Strategy for Duplicate Rows Inspection
# -----------------------------------------------------
# This strategy inspects the dataframe for duplicate rows.
class DuplicateRowsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints the number of duplicate rows in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints duplicate row count to the console.
        """
        num_duplicates = df.duplicated().sum()
        print(f"\nNumber of Duplicate Rows: {num_duplicates}")


# Concrete Strategy for Outlier Detection
# -----------------------------------------------------
# This strategy detects outliers in numerical columns using the IQR method.
class OutlierDetectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Detects and prints the number of outliers in numerical columns using the IQR method.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the count of outliers per column.
        """
        print("\nOutlier Detection (Using IQR Method):")
        for col in df.select_dtypes(include=["number"]).columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            print(f"{col}: {outliers.shape[0]} outliers")


# Concrete Strategy for Unique Values Inspection
# -----------------------------------------------------
# This strategy inspects the number of unique values in each categorical column.
class UniqueValuesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints the number of unique values in each categorical column.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the count of unique values per categorical column.
        """
        print("\nUnique Values Count (Categorical Features):")
        for col in df.select_dtypes(include=["O"]).columns:
            print(f"{col}: {df[col].nunique()} unique values")



# Context Class that uses a DataInspectionStrategy
# ------------------------------------------------
# This class allows you to switch between different data inspection strategies.
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """
        self._strategy.inspect(df)


# # Example usage
# if __name__ == "__main__":
#     # Example usage of the DataInspector with different strategies.

#     # Load the data
#     df = pd.read_csv('notebook/data.csv')

#     # Initialize the Data Inspector with a specific strategy
#     inspector = DataInspector(DataTypesInspectionStrategy())
#     inspector.execute_inspection(df)

#     # Change strategy to Summary Statistics and execute
#     inspector.set_strategy(SummaryStatisticsInspectionStrategy())
#     inspector.execute_inspection(df)

#     # Change strategy to Duplicate Rows
#     inspector.set_strategy(DuplicateRowsInspectionStrategy())
#     inspector.execute_inspection(df)

#     # Change strategy to Outlier Detection
#     inspector.set_strategy(OutlierDetectionStrategy())
#     inspector.execute_inspection(df)

#     # Change strategy to Unique Values Inspection
#     inspector.set_strategy(UniqueValuesInspectionStrategy())
#     inspector.execute_inspection(df)