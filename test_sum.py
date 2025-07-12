# test_summarizer.py
from summarizer import generate_summary

test_text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines 
that are programmed to think and learn like humans. AI has a wide range of applications 
including natural language processing, robotics, and image recognition.
"""

summary = generate_summary(test_text)
print("Summary:")
print(summary)
