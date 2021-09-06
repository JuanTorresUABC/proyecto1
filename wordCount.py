print('Bienvenido')
word = input('Que hiciste hoy?\n')
word_list = word.split()

number_of_words = len(word_list)
print('Me contaste todo con tan solo '+ str(number_of_words)+' palabras.')