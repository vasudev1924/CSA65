prompts = {
    "Prompt A": "Explain renewable energy.",
    "Prompt B": "Explain renewable energy with examples.",
    "Prompt C": """
    Explain renewable energy in simple English.
    Include definition, three examples, two benefits,
    and one limitation. Use headings and bullet points.
    """
}

scores = {
    "Prompt A": 16,
    "Prompt B": 21,
    "Prompt C": 24
}

for name in prompts:
    print(name, ":", prompts[name])
    print("Score:", scores[name])

best = max(scores, key=scores.get)

print("\nBest Prompt:", best)
print("Refined Prompt:")
print(prompts[best])
