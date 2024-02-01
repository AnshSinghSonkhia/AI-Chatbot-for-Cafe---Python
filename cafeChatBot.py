from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('CafeBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on custom data along with the English language data
trainer.train('chatterbot.corpus.english', './custom_data.yml')

# Define a function to get responses from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Example usage
user_question = "What types of coffee do you offer?"
bot_response = get_response(user_question)
print(bot_response)
