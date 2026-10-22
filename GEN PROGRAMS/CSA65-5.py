zero_shot = "Create a promotional post for an AI Workshop."

one_shot = """
Example:
Python Workshop! Learn coding skills.
Register now!

Create an AI Workshop post in the same style.
"""

few_shot = """
Example 1: Python Workshop - Learn coding.
Example 2: Data Science Workshop - Explore data.

Create an attractive AI Workshop post with hashtags.
"""

print("Zero-shot:\n", zero_shot)
print("One-shot:\n", one_shot)
print("Few-shot:\n", few_shot)
