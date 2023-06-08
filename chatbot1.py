# Define the input patterns and corresponding responses
input_patterns = ["hi", "hello", "how are you", "what's up", "goodbye"]
output_responses = ["Hello!", "Hi there!", "I'm fine, thank you!", "Not much. How about you?", "Goodbye!"]

# Function to generate a response based on the input
def generate_response(input_text):
    for pattern, response in zip(input_patterns, output_responses):
        if pattern in input_text.lower():
            return response
    return "Sorry, I didn't understand that."

# Main conversation loop
print("AI: Hi! I'm an AI chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = generate_response(user_input)
    print("AI:", response)
