#imports
import time
from os import system
import sys

def efeito(frase): #função de efeito
      for i in list(frase):
        print(i, end='')
        
        sys.stdout.flush()
        time.sleep(0.00) #tempo entre cada letra
      print('')#pular pra próxima linha
      return 


def efeito_1(frase): #função de efeito
      for i in list(frase):
        print(i, end='')
        
        sys.stdout.flush()
        time.sleep(0.08) #tempo entre cada letra
      print('')#pular pra próxima linha
      return 

  
def morte():# Função que vai dar a mensagem de morte na tela
  backMenu = None
  while True:
    print('')
    print('')
    efeito_1('''             VOCÊ MORREU!!!!!!!!! 
    
Sim! e com certeza foi porque você foi burro(a) ou copiou a resposta errado...''')
    print('')
    print('')
    resposta = input('Digite 1 para ir ao Menu: ')
    if resposta == '1':
      backMenu = menu()
      break
    else:
      print('Resposta Inválida')  
  backMenu()  


def menu():#Menu
  system('clear')
  opçao = None
  print('''       MENU GAME''')
  print('><-'*8)
  print('''  [ 1 ] Iniciar o Jogo
  [ 2 ] Sinopse 
  [ 3 ] Pedir DLC 
  [ 4 ] Créditos''')
  print('><-'*8)
  print('')
  print('')

  
  while True:
    opçao_menu = (input('>>Digite a opção escolhida Aqui: '))
    if opçao_menu == '1':
      opçao = start_game()
      break
     
    elif opçao_menu == '2':
      opçao = sinopse()
      break
    
    elif opçao_menu == '3':
      opçao = DLC()
      break 
    
    elif opçao_menu == '4':
      opçao = creditos()
      break
    
    else:
      print('Opção inválida, digite corretamente')
    
  opçao()


def creditos(): #Créditos (4)
  
  system('clear')
  opçao = None
  print('    CRÉDITOS')
  efeito('História: João Pedro Uchoa ')
  efeito('Direção: João Pedro Uchoa')
  efeito('Produção: João Pedro Uchoa')
  efeito('Maquiagem: João Pedro Uchoa')
  efeito('Fotografia: João Pedro Uchoa')
  efeito('Efeitos Especiais: João Pedro Uchoa')
  efeito('Direção de Arte: João Pedro Uchoa')
  while True:
    print('')
    resposta = (input('Digite 1 para voltar: '))
    
    if resposta == '1':
      opçao = menu()
      break
    
    else:
      print('Opção inválida, tente novamente:')  
  
  opçao()


def DLC(): #dlc(3)
  
  system('clear')
  opçao = None
  print(''' Contato para pedir DLC''')
  print('Envie R$200,00 pelo pix')
  print('''PIX: uchoajoaopedro@gmail.com''')
  while True:
    print('')
    resposta = (input('Digite 1 para voltar: '))

    if resposta == '1':
      opçao = menu()
      break
    
    else:
      print('Opção inválida, tente novamente:')  
  
  opçao()

  
def sinopse(): #Sinopse(2)
  opçao_menu = None
  system('clear')

  efeito('''    SINOPSE
O nosso Personagem acorda em meio ao caos de uma batalha recente.
Encontra Mírya, uma amiga do mesmo batalhão, eles devem unir forças pra sair desse local com vida!
Você deve escolher o melhor caminho para salva-los. BOA SORTE 
Let's go GAME!!!!!!''') 


  while True:
    resposta = (input('Digite 1 para voltar: '))


    if resposta == '1':
      opçao_menu = menu()
      break
    
    
    
    else:
      print('Opção inválida, tente novamente')


  
  opçao_menu() 


salvo = [] # vetor fora da função (global)
nome_player = [] # vetor fora da função (global)


def start_game():# inicio do Jogo (Capítulo UM) (1)
  system('clear') 
  efeito('''Bem-Vindo(a)!
Esse game funciona com uma história em quem escolhe o destino das personagens é você!
digite corretamente as respostas, senão você não seguirá o caminho desejado!
BOM JOGO!!!''')
  print('')
  print('')
  player_name = input('Qual o seu Nome? ')
  nome_player.append(player_name) 
  system('clear')
  
  #Começo da História
  efeito_1('''           C.A.P.Í.T.U.L.O    U.M             ''')
  print('')
  print('')
  system('clear')

  efeito('''Acordo meio tonto, parece que fui nocauteado... lembro de pouca coisa...
eu estava lutando, quer dizer, fungindo de algo...
era algo grande... e parecia assustador...
Ergo minha cabeça e me sento com dificuldade no chão
Sinto uma dor no joelho direito
 
''')
  
  
  levantando = input('DEVO LEVANTAR? (digite Sim ou Não) ').lower()
  if levantando != 'sim':
    print('')
    print('')
    efeito('Eu não sei o que pode estar por perto, tenho que sair daqui...')
    
      
    levantando = input('DEVO LEVANTAR? (digite Sim ou Não) ').lower()
    
    if levantando != 'sim':
        efeito('Você vê bastante sangue no chão, e se dá conta de que é o seu!')
        morte()
        

    
  
  
    
  efeito('''
levanto-me com mais dificuldade ainda, de longe vejo alguém deitado no chão...

— É a Mírya?
— É a Mírya!

O meu instinto diz pra ir embora o mais rápido que eu puder...
mas...
acho que devo checar se ela ainda está com vida!, não posso abandona-la


''')

  checar_mirya = input('CHECAR SE A MÍRYA ESTÁ COM VIDA? (digite Sim ou Não) ').lower()
  print('')

  if checar_mirya != 'sim':
    efeito(f'''Eu preciso sair daqui...
não tenho tempo pra ir lá, acho que ela já está morta!

MÍRYA GRITA:
— {player_name}!!!

Ela está viva''')

    
  efeito('ainda com medo...')

  efeito('''Vou até onde ela está deitada e a vejo de olhos abertos
  ''')

  efeito(f'''O olhar dela parece preocupado...

Eu pergunto se ela está bem, e com um tom irônico ela rebate:

(MÍRYA)— Parece que Ele te acertou em cheio mesmo hein! 

({player_name})— O que? — pergunto confuso.

(MÍRYA)— Você tá machucado? — ela me pergunta.

({player_name})— Sinto o joelho, mas não deve ser nada!

(MÍRYA)— A gente precisar voltar pra base, não dá pra ficar muito tempo aqui!
ela diz com olhar ainda mais procupado e se levanta com dificuldade.

({player_name})— Base? acho que estamos bem longe dela.

({player_name})— Ei! depois que eu apaguei não faço idéia do que houve

(MÍRYA)— Muita coisa garoto!
eu não consegui mata-lo, ele deve tá aqui ainda
ela fala olhando para os lados, como se procurasse algo.

({player_name})— Quem? — sussurro preocupado.

(MÍRYA)— Um Sentinela, soldado Mogadoriano. — 

({player_name})— Mogadorianos! por um momento esqueci o porque de estarmos aqui!

Nesse momento sinto um calafrio, parecia que a temperatura tinha caído.

(MÍRYA)— Temos que nos mover, parados somos presas fáceis

''')
  ir_Mírya = input('IR COM A MÍRYA? (digite Sim ou Não) ').lower()
  if ir_Mírya != 'sim':
    efeito('(MÍRYA)— Você só pode ser louco!, está bem, sigo sozinha!')
    efeito('Se você morrer, a culpa não é minha garotão')
    print('')

    efeito('Você segue sozinho!')
    print('')
    efeito('cansado de andar, você senta em uma pedra com o joelho ainda doendo')
    efeito('sozinho e cansado, um Sentinela te encontra e rapidamente dispara contra você')
    efeito('sua visão escurece...')
    morte()

  efeito('''sigo com Mírya 

recebemos um sinal no nosso rádio:

(MÍRYA)— É uma mensagem da nossa base!

uma voz fala no rádio:

<< Atenção Sobreviventes
A nave de resgate está sobrevoando a dois quilômetros ao Norte do local 
que perdemos o contato com a tropa.
Não podemos chegar mais próximo que isso, existem forças hostís nessa região...
estaremos lá até o amanhecer, tomem cuidado!!! >> 

(MÍRYA)— Vamos pra lá, não estamos muito longe

''')

  ir_norte = input('SEGUIR PARA O NORTE? (digite Sim ou Não) ').lower()
  if ir_norte != 'sim':
    print('')
    efeito('Você segue para outra direção sozinho!')
    print('')
    efeito('Um soldado Mogadoriano, te encontra')
    efeito('você tenta correr e lutar, mas é abatido com facilidade')
    morte()

  efeito(f'''({player_name})— Claro!, vamos logo 
(MÍRYA)— certo garotão!

Vocês dois seguem para o norte...''')
  print('')
  print('')
  
  while True:
    capitulo2 = input('digite 1 para seguir ao capitulo dois: ')
    if capitulo2 == '1':
      break
    else:
      print('Opção inválida!')
      print('')

  capitulo2_1()  


def capitulo2_1():
  system('clear')
  efeito_1('''           C.A.P.Í.T.U.L.O    D.O.I.S             ''')
  system('clear')

  
  
  
  efeito(f'''Seguindo ao Norte, encontramos um lobo com a pata presa em arames farpados 
(MÍRYA)— Que Droga! olha! coitado do pobre animal
({nome_player[0]})— A gente pode ajuda-lo!
(MÍRYA)— ou pode ser algum tipo de armadilha, eles podem estar usando esse animal como isca!
''')
  print('')
  salvar_animal = input('SALVAR O LOBO? (digite sim ou não) ').lower()
  if salvar_animal == 'sim':
    animal_salvo = 1
    salvo.append(animal_salvo)
    efeito(f'''({nome_player[0]})— Ele não podia ficar aí, espero que ele fique bem...

(MÍRYA)— Ainda bem que a gente ajudou ele, espero que esse favor seja retribuído.

Salvamos o lobo e ele fugiu ainda mancando...''')
    print('')

  
  else:
    efeito(f'''({nome_player[0]})— acho melhor a gente ir embora, ele vai ficar bem!
(MÍRYA)— é verdade! melhor seguirmos, ele vai ficar bem...''')
  print('')
  efeito(f'''Seguindo em frente, encontramos dois caminhos:

>>Por cima da Montanha, caminho mais curto e talvez mais arriscado!

>>Dar a volta na Montanha, caminho mais longo e talvez menos arriscado!

(MÍRYA)— e agora? por onde vamos?  

''')
  print('''
Digite 1 para ir por cima do Morro 
Digite 2 para dar a volta no Morro
''')

  
  
  while True:
    print('')
    ir_caminho = input('QUAL CAMINHO SEGUIR? ')
    
    if ir_caminho == '1':
      break
    
    elif ir_caminho == '2':
      capitulo2_2()
      break

    else:
      print('Opção inválida! tente novamente.')
      print('')


  efeito(f'''({nome_player[0]})— Vamos por cima, é mais rápido!
(MÍRYA)— Ok, vamos!

Seguimos subindo o Morro!


a medida que ando, sinto meu joelho doer cada vez mais, preciso sentar e descansar,
mas isso pode custar a nossa vida.
tenho que continuar...

 ''')
  
  sentar = input('DEVO SENTAR E DESCANSAR? ').lower()
  if sentar == 'sim':
    print('')
    efeito(f'''paramos pra descansar um pouco
é visivel minha dificuldade pra conseguir continuar!
não tarda muito e começamos a ouvir passos
(MÍRYA)— não foi uma boa ideia!
(MÍRYA)— Você aguenta correr? precisamos nos esconder! 
''')
    correr = input('VOCÊ VAI CORRER? (digite Sim ou não)').lower()
    if correr == 'sim:':
      print('')
      efeito('''Você e Míria correm... mas não conseguem ir muito longe
Um Sentinela atravessa uma lança no seu peito, sem chance de defesa você Morre...''')
      morte()
    
    else:
      print('')
      efeito('''Vocês tentam ficar parados e quietos, mas mesmo assim,
você vê Mírya ser decaptada em um único golpe e logo vê uma lança atravessar seu abdômen,
Morte certa...  
''')
      morte()
  
  print('')
  efeito(f'''({nome_player[0]})— Eu tô bem cansado, mas não vamos parar não!

(MÍRYA)— Eu também não acho uma boa idéia, muito arriscado

({nome_player[0]})— Mírya, o que aconteceu lá? antes de eu apagar...

(MÍRYA)— Eu tenho certeza que a Missão vazou, eles sabiam de tudo,
estavam preparados e nos abateram, eu não entendo como isso aconteceu
tem coisa errada, temos um informante no nosso exército

({nome_player[0]})— Você sabe que uma afirmação dessas é perigosa né?
eu digo isso porque, nossa comandante não vai acreditar nisso

(MÍRYA)— Eu sei, mas é isso o que eu acho, eles conseguiram prever nossas manobras de batalha
isso é impossível! sabiam do nosso arsenal e ainda sabiam do objetivo da Missão

({nome_player[0]})— É! com certeza tem algo errado. ei como você foi nocauteada? 

(MÍRYA)— Eu conseguir matar dois Sentinelas, mas, um explodiu uma granada na minha frente
eu fiz o própio corpo dele de escudo, fui arremessada, acho que bati a cabeça e apaguei!

({nome_player[0]})— Você matou dois Sentinelas? que manobra voce usou?

(MÍRYA)— Eu usei a padrão, esperei o primeiro ataque e revidei com mais velocidade.

({nome_player[0]})— é uma boa manobra mesmo!   

(MÍRYA)— A gente conseguiu chegar no topo do morro, olha! ali está o local de resgate

({nome_player[0]})— Por que eu não to vendo o helícoptero sobrevoar o lugar?

Nesse momento vocês são cercados por dois Mogadorianos...

(MÍRYA)— Não da pra fugir! 

({nome_player[0]})— Eu sei, eles nem são Sentinelas, é uma classe menor...

(MÍRYA)— Então dá pra lutar!
''')


  while True:
    print('')
    lutar = input('VOCÊS DEVEM LUTAR? (digite Sim ou Não) ').lower()
    if lutar== 'sim':
      break
    
    elif lutar == 'não':
      efeito('(MÍRYA)— Não dá pra correr...')
      print('')
      lutar = input('VOCÊS DEVEM LUTAR? (digite Sim ou Não) ').lower()
      if lutar != 'sim':
        print('')
        efeito('Você vira as costas pra correr, e dois passos depois sente uma pancada na nuca...')
        morte()
        break
      else:
        break

    else:
      print('Opção inválida, tente novamente: ')
  
  efeito(f'''
(MÍRIA)— Posicionamento de luta padrão!
  
({nome_player[0]})— Certo! 

>>Atacar com a mão Direita
>>Atacar com a perna Direita

digite 1 para mão
digite 2 para perna
''')

  while True:
    print('')
    atacar = input('COMO ATACAR? ')
  
    if atacar == '1':
      break
    elif atacar == '2':
      print('')
      efeito('Sua perna ainda está machucada!')
      efeito('Seu ataque foi muito fraco')
      print('')
      atacar = input('ATAQUE NOVAMENTE! ')
      if atacar == '1':
        break
      
      elif atacar == '2':
       efeito('Antes de conseguir erguer sua perna pra outro golpe')
       efeito('O Mogadoriano acerta sua cabeça, Você cai desacordado!') 
       morte()
      
      else:
        print()
        print('Opção inválida, tente novamente')
    else:
      print('')
      print('Opção inválida, tente novamente:')

  efeito(f'''Seu golpe nocauteou um deles...
você olha para o lado e Mírya já derrubou o segundo...

(MÍRYA)— Agora a gente corre!
''')
  while True:
    capitulo3 = input('digite 1 para seguir ao capitulo Três: ')
    if capitulo3 == '1':
      break
    else:
      print('Opção inválida!')
      print('')
  
  capitulo3()    



def capitulo2_2():

  efeito(f'''({nome_player[0]})— Vamos dar a volta, é mais seguro!
(MÍRYA)— Ok, vamos!

Seguimos dando a volta no Morro!


a medida que ando, sinto meu joelho doer cada vez mais, preciso sentar e descansar,
mas isso pode custar a nossa vida.
tenho que continuar...

 ''')
  
  sentar = input('DEVO SENTAR E DESCANSAR? ').lower()
  if sentar == 'sim':
    print('')
    efeito(f'''paramos pra descansar um pouco
é visivel minha dificuldade pra conseguir continuar!
não tarda muito e começamos a ouvir passos
(MÍRYA)— não foi uma boa ideia!
(MÍRYA)— Você aguenta correr? precisamos nos esconder! 
''')
    correr = input('VOCÊ VAI CORRER? (digite Sim ou não)').lower()
    if correr == 'sim:':
      print('')
      efeito('''Você e Míria correm... mas não conseguem ir muito longe
Um Sentinela atravessa uma lança no seu peito, sem chance de defesa você Morre...''')
      morte()
    
    else:
      print('')
      efeito('''Vocês tentam ficar parados e quietos, mas mesmo assim,
você vê Mírya ser decaptada em um único golpe e logo vê uma lança atravessar seu abdômen,
Morte certa...  
''')
      morte()
  
  print('')
  efeito(f'''({nome_player[0]})— Eu tô bem cansado, mas não vamos parar não!

(MÍRYA)— Eu também não acho uma boa idéia, muito arriscado

({nome_player[0]})— Mírya, o que aconteceu lá? antes de eu apagar...

(MÍRYA)— Eu tenho certeza que a Missão vazou, eles sabiam de tudo,
estavam preparados e nos abateram, eu não entendo como isso aconteceu
tem coisa errada, temos um informante no nosso exército

({nome_player[0]})— Você sabe que uma afirmação dessas é perigosa né?
eu digo isso porque, nossa comandante não vai acreditar nisso

(MÍRYA)— Eu sei, mas é isso o que eu acho, eles conseguiram prever nossas manobras de batalha
isso é impossível! sabiam do nosso arsenal e ainda sabiam do objetivo da Missão

({nome_player[0]})— É! com certeza tem algo errado. ei como você foi nocauteada? 

(MÍRYA)— Eu conseguir matar dois Sentinelas, mas, um explodiu uma granada na minha frente
eu fiz o própio corpo dele de escudo, fui arremessada, acho que bati a cabeça e apaguei!

({nome_player[0]})— Você matou dois Sentinelas? que manobra voce usou?

(MÍRYA)— Eu usei a padrão, esperei o primeiro ataque e revidei com mais velocidade.

({nome_player[0]})— é uma boa manobra mesmo!   

(MÍRYA)— A gente conseguiu chegar no topo do morro, olha! ali está o local de resgate

({nome_player[0]})— Por que eu não to vendo o helícoptero sobrevoar o lugar?

Nesse momento vocês são cercados por dois Mogadorianos...

(MÍRYA)— Não da pra fugir! 

({nome_player[0]})— Eu sei, eles nem são Sentinelas, é uma classe menor...

(MÍRYA)— Então dá pra lutar!
''')


  while True:
    print('')
    lutar = input('VOCÊS DEVEM LUTAR? (digite Sim ou Não) ').lower()
    if lutar== 'sim':
      break
    
    elif lutar == 'não':
      efeito('(MÍRYA)— Não dá pra correr...')
      print('')
      lutar = input('VOCÊS DEVEM LUTAR? (digite Sim ou Não) ').lower()
      if lutar != 'sim':
        print('')
        efeito('Você vira as costas pra correr, e dois passos depois sente uma pancada na nuca...')
        morte()
        break
      else:
        break

    else:
      print('Opção inválida, tente novamente: ')
  
  efeito(f'''
(MÍRIA)— Posicionamento de luta padrão!
  
({nome_player[0]})— Certo! 

>>Atacar com a mão Direita
>>Atacar com a perna Direita

digite 1 para mão
digite 2 para perna
''')

  while True:
    print('')
    atacar = input('COMO ATACAR? ')
  
    if atacar == '1':
      break
    elif atacar == '2':
      print('')
      efeito('Sua perna ainda está machucada!')
      efeito('Seu ataque foi muito fraco')
      print('')
      atacar = input('ATAQUE NOVAMENTE! ')
      if atacar == '1':
        break
      
      elif atacar == '2':
       efeito('Antes de conseguir erguer sua perna pra outro golpe')
       efeito('O Mogadoriano acerta sua cabeça, Você cai desacordado!') 
       morte()
      
      else:
        print()
        print('Opção inválida, tente novamente')
    else:
      print('')
      print('Opção inválida, tente novamente:')

  efeito(f'''Seu golpe nocauteou um deles...
você olha para o lado e Mírya já derrubou o segundo...

(MÍRYA)— Agora a gente corre!
''')
  while True:
    capitulo = input('digite 1 para seguir ao capitulo Três: ')
    if capitulo == '1':
      break
    else:
      print('Opção inválida!')
      print('')
  
  capitulo3()    



def capitulo3():

  system('clear')
  efeito_1('''           C.A.P.Í.T.U.L.O    T.R.Ê.S  (FINAL)           ''')
  system('clear')
  
  efeito(f'''
Vocês ainda estão correndo,
a menos de 400 metros de distancia do local de resgate
Um Sentinela pula na frente dos dois
não há como fugir... 

(MÍRYA)— Esse aí não dá pra fugir não!

({nome_player[0]})— O que a gente faz?

(MÍRYA)— Bem, vai ser uma morte digna! eu fico aqui e você continua, vou destraí-lo!

({nome_player[0]})— Você tá maluca?

(MÍRYA)— É o unico jeito, do contrário nós dois vamos morrer!

({nome_player[0]})— Espera! não precisa ser você, eu fico!

QUEM DEVE FICAR?
>>MÍRYA (digite 1)
>>{nome_player[0]} (digite 2)
''')
  
  while True:
    ficar = input('ESCOLHA UM: ')

    if ficar == '1':
      mirya()
  
    elif ficar == '2':
      player()

    else:
      print('')
      print('Opção inválida< tente novamente:')



def mirya():
  efeito(f'''
(MÍRYA)— Vai logo! rápido!

Corro em direção ao local, chego a tempo de ser socorrido
A Nave sobe e Vejo Mírya já desacordada...
Sinto que falhei com ela
irei carregar o peso dessa decisão pra sempre...  
''')


  efeito(' Fim de jogo! ')
  while True:
    print('')
    capitulo = input('digite 1 para seguir ao MENU GAME ')
    if capitulo == '1':
      break
    else:
      print('Opção inválida!')
      print('')
  menu()


def player():
  efeito(f'''
Decido ficar, Mírya entende e corre, não há tempo para despedidas
O Sentinela Pula sobre mim...

e então...

 ''')
  if 1 in salvo:
    efeito(f'''
escuto um Uivar...
é aquele lobo...
ele pula nas costas do Sentinela, e me dá a chance de correr
Meu joelho está doendo muito, mas mesmo assim, não paro
alcanço a nave, e Mírya sem entender como eu sobrevivi...
eu apenas respondo...
({nome_player[0]})— O bem foi retribuido! 

estamos Salvos, Espero que aquele Lobo fique bem!''')
    print('')
    print('')
    efeito(' Fim de jogo! ')
    while True:
      print('')
      capitulo = input('digite 1 para seguir ao MENU GAME ')
      if capitulo == '1':
        break
      else:
        print('Opção inválida!')
        print('')
    menu()

  else:
    efeito('''
Sinto o golpe, vejo o sangue
não tenho tempo nem de sentir dor, tudo fica escuro...
''')
    efeito(' Fim de jogo! ')
    while True:
      print('')
      capitulo = input('digite 1 para seguir ao MENU GAME ')
      if capitulo == '1':
        break
      else:
        print('Opção inválida!')
        print('')
    menu()

menu() 