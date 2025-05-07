import requests
from config import CANDIDATES_API_URL, INTERVIEW_REF
from services.filter_service import filter_by_category, filter_by_query

def fetch_candidates(query: str = '', allowed_keys=None):
    if allowed_keys is None:
        allowed_keys = ['design', 'programming', 'marketing', 'content']

    response = requests.get(
        CANDIDATES_API_URL,
        headers={"x-reference-id": INTERVIEW_REF}
    )
    response.raise_for_status()

    all_data = response.json()

    # Filter only the selected categories
    categorized_data = filter_by_category(all_data, allowed_keys)

    # Filter by query if provided
    if query:
        categorized_data = filter_by_query(categorized_data, query)

    return categorized_data
