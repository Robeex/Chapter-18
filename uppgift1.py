f = open('./test.txt', 'w', encoding='utf-8')

Namn = input('Skriv ditt namn (tom rad avslutar): ')

while Namn :
  f.write(Namn+'\n')
  Tele = input('Skriv ditt telefonnummer (tom rad avslutar): ')
  f.write(Tele+'\n')
  Namn = input('Skriv ditt namn (tom rad avslutar): ')
f.close()

