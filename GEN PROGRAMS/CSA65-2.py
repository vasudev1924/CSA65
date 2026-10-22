zero_shot = """
Write a 200-word blog on Applications of Artificial
Intelligence in Healthcare.
"""

one_shot = """
Example: AI in Education improves learning through
personalized lessons.

Write a 200-word blog on AI in Healthcare
using a similar structure.
"""

few_shot = """
Example 1: AI in Education supports personalized learning.
Example 2: AI in Agriculture improves crop monitoring.

Write a 200-word blog on AI in Healthcare
using simple English.
"""

print("Zero-shot Prompt:\n", zero_shot)
print("One-shot Prompt:\n", one_shot)
print("Few-shot Prompt:\n", few_shot)
