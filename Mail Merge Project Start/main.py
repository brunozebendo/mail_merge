PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letters = letter_contents.replace(PLACEHOLDER, stripped_names)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letters:
            completed_letters.write(new_letters)

"""O objetivo do projeto é criar cartas a partir de uma carta padrão,
substituindo o nome do convidado e criando novas cartas para cada um.
Primeiro, criou uma variável constante, depois abriu o arquivo já o estabelecendo
 como uma variável. Importante notar que a linha de comando para abrir o arquivo
  começa na pasta que está na mesma posição, em um modo de identação, depois,
   atribui-se uma nova variável (names) que será lida, então, abre-se um
    novo arquivo que é o da carta inicial. Então, um for loop vai iterar pela
     lists de nomes que foi criada pelo comando readlines, o comando strip vai
      apagar os espaços em branco e o comando replace vai substituir o [name]
       pelo novo nome (na carta original o name está assim marcado [name]),
        por fim, o novo open vai criar um arquivo já com o nome do convidado,
         nesse caso não pode esquecer o comando w de write, para que ele abra
          e escreva."""