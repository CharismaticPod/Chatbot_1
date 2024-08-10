from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Buat instance ChatBot
bot = ChatBot('Assistant')

# Tentukan data training
conversation = [
    "Halo",
    "Halo, ada yang bisa saya bantu?",
    "Apa kamu robot?",
    "Ya, saya adalah chatbot AI yang dibuat untuk membantu Anda.",
    "Bagaimana cara kamu bekerja?",
    "Saya menggunakan teknologi pemrosesan bahami alami dan machine learning untuk memahami dan merespons pesan Anda. Saya akan berusaha semaksimal mungkin untuk menjawab pertanyaan Anda dengan tepat."
]

# Latih chatbot dengan data training
trainer = ListTrainer(bot)
trainer.train(conversation)

# Fungsi untuk memulai percakapan
def start_chat():
    print("Halo, saya adalah chatbot AI. Silakan tanyakan apa pun kepada saya!")
    while True:
        try:
            user_input = input("Anda: ")
            bot_response = bot.get_response(user_input)
            print("Chatbot: ", bot_response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Mulai percakapan
start_chat()