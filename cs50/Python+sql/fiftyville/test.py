from mtranslate import translate

a = ['Hello i am fine', 'Good', 'You', 'Kill', 'Dad']

for phrase in a:
    transrow = translate(phrase, 'ru')
    print(f'{transrow}')