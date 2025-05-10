from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

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


def fuzzy_match(query, candidate_data):
    # ปรับลดเกณฑ์ความแม่นยำจาก 60 เป็น 50
    return fuzz.token_sort_ratio(query.lower(), candidate_data.lower()) > 60

  # ลดความแม่นยำลง

# ฟังก์ชันที่ใช้ TF-IDF Vectorization สำหรับการค้นหาคล้ายความหมาย
def vector_match(query, candidate_data):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([query] + candidate_data)
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).A
    print("Cosine Similarities: ", cosine_similarities)  # ดูค่าคล้ายกัน
    return cosine_similarities[0, 1:] > 0.5  # ลดเกณฑ์จาก 0.5 เป็น 0.4



def filter_by_query(categorized_data: dict, query: str) -> dict:
    """
    Filter candidates within categories based on fuzzy matching and vector-based similarity.
    """
    query = query.lower()
    for key in categorized_data:
        candidates = categorized_data[key]

        if not candidates:
            continue

        # Candidate texts for vector matching
        candidate_texts = [
            f"{c.get('firstName', '')} {c.get('lastName', '')}" for c in candidates
        ]

        # Run vector similarity once
        vector_results = vector_match(query, candidate_texts)

        matched_candidates = []
        for i, c in enumerate(candidates):
            is_fuzzy_match = (
                fuzzy_match(query, c.get("firstName", ""))
                or fuzzy_match(query, c.get("lastName", ""))
                or fuzzy_match(query, c.get("interviewRefNo", ""))
                or fuzzy_match(query, c.get("major", ""))
            )
            is_vector_match = vector_results[i] if i < len(vector_results) else False

            if is_fuzzy_match or is_vector_match:
                matched_candidates.append(c)

        categorized_data[key] = matched_candidates

    return categorized_data

