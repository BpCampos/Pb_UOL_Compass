animais = ['abelha', 'abutre', 'aguia', 'alce', 'alpaca', 'cabra', 'cachorro',
           'cagado', 'camarao', 'camelo', 'jabuti', 'jacare', 'jacu', 'jaguar', 'jegue', 'panda', 'pantera', 'papagaio', 'pardal', 'passaro',]

for i in sorted(animais):
    print(i)

with open('animais.txt', 'w', encoding='utf-8') as animais_txt:
    for animal in sorted(animais):
        animais_txt.writelines(f"{animal}\n")
