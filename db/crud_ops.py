from db.connection import collection

def add_record(data: dict):
    """Add a new record to MongoDB."""
    result = collection.insert_one(data)
    return f"Record added successfully with ID: {result.inserted_id}"

def find_record(query: dict):
    """Find a record based on a query dictionary."""
    doc = collection.find_one(query)
    if not doc:
        return "No matching record found."
    doc.pop("_id", None)
    return doc

def edit_record(filter_query: dict, updates: dict):
    """Edit a record matching the filter query."""
    result = collection.update_one(filter_query, {"$set": updates})
    if result.modified_count > 0:
        return "Record updated successfully."
    return "No record updated. Check your filter query."

def delete_record(query: dict):
    """Delete a record based on a query."""
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return "Record deleted successfully."
    return "No record found to delete."
