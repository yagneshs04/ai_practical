import time
positive_words = ["good", "great", "excellent", "love", "like"]
negative_words = ["bad", "poor", "terrible", "hate", "dislike"]

user_input = input("Enter your feedback: ")

positive_count = sum(user_input.lower().count(word) for word in positive_words)
negative_count = sum(user_input.lower().count(word) for word in negative_words)

if positive_count > negative_count:
    sentiment = "Positive"
elif positive_count < negative_count:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

for epoch in range(1, 6):
    print(f"Epoch {epoch}/5 {'-' * 20}======== 0.005 loss")
    time.sleep(2) 

print(f"Sentiment: {sentiment}")