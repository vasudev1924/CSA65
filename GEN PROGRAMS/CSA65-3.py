article = input("Enter article: ")

zero_shot = "Summarize this article in 50 words:\n" + article

one_shot = """
Example:
Article: AI helps computers learn from data.
Summary: AI enables computers to learn patterns from data.

Summarize this article in 50 words:
""" + article

few_shot = """
Example 1: Solar energy uses sunlight to produce power.
Example 2: Wind energy uses moving air to generate power.

Summarize this article in 50 words:
""" + article

print("\nZero-shot Prompt:\n", zero_shot)
print("\nOne-shot Prompt:\n", one_shot)
print("\nFew-shot Prompt:\n", few_shot)
