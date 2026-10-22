task = "Explain machine learning in three sentences."

prompts = {
    "Zero-shot": task,
    "One-shot": """
    Example: AI enables machines to perform intelligent tasks.
    Explain machine learning in three sentences.
    """,
    "Few-shot": """
    Example 1: AI performs intelligent tasks.
    Example 2: Deep learning uses neural networks.
    Explain machine learning in three sentences.
    """
}

for technique, prompt in prompts.items():
    print("\n", technique)
    print(prompt)
