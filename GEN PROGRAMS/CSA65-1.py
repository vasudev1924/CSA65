zero_shot = """
Write a product description for a Smart Fitness Watch.
Include features and benefits.
"""

one_shot = """
Example:
Product: Smart Bottle
Description: Tracks water intake and sends reminders.

Write a description for a Smart Fitness Watch.
"""

few_shot = """
Product: Smart Bottle - Tracks water intake.
Product: Wireless Earbuds - Provides clear audio.

Write a description for a Smart Fitness Watch
in the same style.
"""

print("Zero-shot:", zero_shot)
print("One-shot:", one_shot)
print("Few-shot:", few_shot)
