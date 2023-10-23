# ---- Similarity Search ---
def nearest_neighbors(query, vectorstore):
    return vectorstore.similarity_search_with_score(query, k=5)