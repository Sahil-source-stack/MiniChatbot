import time
now = time.ctime()

print('Bot: Hey there user, I am mini chatbot pls ask me something !')
qna = {
    'hi': 'hello',
    'how are you': 'I am fine what about you ??',
    'what is your name': 'I am Sahil mini chatbot',
    'how old are you': 'I dont have any age as I am immortal',
    'i love you': 'i like myself too',
    'bye': 'alright see you !!',
    'what is the time now': now

}

while True:
    qs = input('You: ')
    if qs == 'quit':
        break
    else:
        print('Bot:', qna[qs])
