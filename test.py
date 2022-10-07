from Class_Game import Game

A = Game()
game_over = False
player1 = True

while not game_over:
    A.print_maps()
    
    if player1:
        symbol = 'X'
        step = int(input('Игрок 1, Ваш ход: '))
    else:
        symbol = 'O'
        step = int(input('Игрок 2, Ваш ход: '))
    
    A.user_step(step, symbol)
    win = A.get_result()
    
    if win != '':
        game_over = True
    else:
        game_over = False
    
    player1 = not(player1)
    
A.print_maps()
print(f'Победил - {win}!')