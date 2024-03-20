animais = ['abelha', 'abutre', 'águia', 'alce', 'alpaca', 'cabra', 'cachorro',
           'cágado', 'camarão', 'camelo', 'jabuti', 'jacaré', 'jacu', 'jaguar', 'jegue', 'panda', 'pantera', 'papagaio', 'pardal', 'pássaro',]

for i in sorted(animais):
    print(i)

with open('animais.txt', 'w', encoding='utf-8') as animais_txt:
    for animal in sorted(animais):
        animais_txt.writelines(f"{animal}\n")
