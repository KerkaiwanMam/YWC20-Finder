import requests
from config import CANDIDATES_API_URL, INTERVIEW_REF

def fetch_candidates(query: str = '', allowed_keys=None):
    if allowed_keys is None:
        allowed_keys = ['design', 'programming', 'marketing']  # Make sure all required categories are included

    response = requests.get(
        CANDIDATES_API_URL,
        headers={"x-reference-id": INTERVIEW_REF}
    )
    response.raise_for_status()

    all_data = response.json()

    # Initialize dictionary to group by categories
    categorized_data = {key: [] for key in allowed_keys}

    # Organize data by categories (major)
    for key in allowed_keys:
        items = all_data.get(key, [])
        if isinstance(items, list):
            categorized_data[key] = items

    # Apply query filtering if needed
    if query:
        query = query.lower()
        for key in allowed_keys:
            categorized_data[key] = [
                c for c in categorized_data[key]
                if query in c.get("firstName", "").lower()
                or query in c.get("lastName", "").lower()
                or query in c.get("interviewRefNo", "").lower()
                or query in c.get("major", "").lower()
            ]

    return categorized_data
