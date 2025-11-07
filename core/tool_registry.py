from langchain_core.tools import tool
from db.crud_ops import add_record, find_record, edit_record, delete_record
import ast

def parse_str_to_dict(data: str):
    """A function to convert string to dictonary
    
    Keyword arguments:
    argument -- string user input
    Return: dictonary converted value of the user input string
    """
    

    if isinstance(data, str):
        try:
                data=ast.literal_eval(data)
        except Exception as e:
            return {"error":f"Failed to parse the input to dict: {e}"}

    if (type(data)==tuple):
        print("The parsed query is a tuple having multiple seperate values")

    print(f"parsed user input: {data}")
    return data



@tool
def add_record_tool(query: str):
    """Add a new record to MongoDB."""

    query=parse_str_to_dict(query)
    return add_record(query)

@tool
def find_record_tool(query: str):
    """Find a record in MongoDB."""
    query=parse_str_to_dict(query)
    return find_record(query)

@tool
def edit_record_tool(query: str):
    """Edit a record in MongoDB."""

    if isinstance(query, str):
        try:
        # Wrap in () so ast.literal_eval returns a tuple
            pair = ast.literal_eval(f"({query})")
            if isinstance(pair, tuple) and len(pair) == 2:
                
                filter_val,update_val=query[0],query[1]
                return edit_record(filter_val,update_val)
            
        except Exception as e:
            print(f"Parsing error: {e}")
    
    

@tool
def delete_record_tool(query: str):
    """Delete a record from MongoDB."""
    query=parse_str_to_dict(query)
    return delete_record(query)

crud_tools = [add_record_tool, find_record_tool, edit_record_tool, delete_record_tool]