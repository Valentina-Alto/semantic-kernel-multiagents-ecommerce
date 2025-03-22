from semantic_kernel.functions import kernel_function
import sqlite3


class QueryDbPlugin:
    """
    Description: Get the result of a SQL query
    """
    def __init__(self, db_path) -> None:
        self._db_path = db_path
    
    @staticmethod
    def __clean_sql_query__(sql_query):
        sql_query = sql_query.replace(";", "")
        sql_query = sql_query.replace("/n ", " ")

        return sql_query  
    
    @kernel_function(name="query_db",
                     description="Query a database using a SQL query")
    def query_db(self, sql_query: str) -> str:    
        # Connect to the SQLite database
        conn = sqlite3.connect(self._db_path)

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        try:
            cursor.execute(self.__clean_sql_query__(sql_query))
            
            # Get the column names from cursor.description
            columns = [column[0] for column in cursor.description]

            # Initialize an empty list to store the results as dictionaries
            results = []

            # Fetch all rows and create dictionaries
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()
            conn.close()
        
        return str(results)