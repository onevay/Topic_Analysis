def thems_count(documents):
    num_docs = len(documents)
    print(num_docs)
    optimal_topics = max(3, min(num_docs // 22, 10))

    return optimal_topics