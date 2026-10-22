zero_shot = "Write a professional sick-leave email."

one_shot = """
Example:
Dear Sir,
I request leave due to personal reasons.
Thank you.

Write a sick-leave email in the same format.
"""

few_shot = """
Example 1: Request leave due to personal work.
Example 2: Request permission for an appointment.

Write a professional sick-leave email.
"""

print("Zero-shot:\n", zero_shot)
print("One-shot:\n", one_shot)
print("Few-shot:\n", few_shot)
