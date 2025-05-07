# services/filter_service.py

def filter_by_category(all_data: dict, allowed_keys: list) -> dict:
    """
    Filter only the categories specified in allowed_keys.
    """
    categorized_data = {}
    for key in allowed_keys:
        items = all_data.get(key, [])
        if isinstance(items, list):
            categorized_data[key] = items
    return categorized_data


def filter_by_query(categorized_data: dict, query: str) -> dict:
    """
    Filter candidates within categories based on query string.
    """
    query = query.lower()
    for key in categorized_data:
        categorized_data[key] = [
            c for c in categorized_data[key]
            if query in c.get("firstName", "").lower()
            or query in c.get("lastName", "").lower()
            or query in c.get("interviewRefNo", "").lower()
            or query in c.get("major", "").lower()
        ]
    return categorized_data
