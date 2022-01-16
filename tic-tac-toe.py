'''
Tic-Tac-Toe
Sheldon Jensen
'''

def main():
    play_again = 'yes'
    while play_again != 'no':
        player = next_play("")
        board = create_board()
        while not (has_win(board) or has_draw(board)):
            display_board(board)
            make_play(player, board)
            player = next_play(player)
        display_board(board)
        
        if has_win(board):
            if player == 'x':
                print('Player O has won!')
            elif player =='o':
                print('Player X has won!')
        if has_draw(board):
            print('No winner! (Draw)')
        
        play_again = input('Do you want to play again? (yes/no) ')    

#create starting board
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

#display grid
def display_board(board):
    print()
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print()

#check win conditions
def has_win(board):
    return (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6])

#check for draw
def has_draw(board):
    for square in range(9):
        if board[square] != '\033[1;30;42mX\033[1;37;40m' and board[square] != '\033[1;30;43mO\033[1;37;40m':
            return False
    return True

#change player
def next_play(current):
    if current == "" or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'

#
def make_play(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))

    if player == 'x':
        color = '\033[1;30;42mX\033[1;37;40m'
    elif player == 'o':
        color = '\033[1;30;43mO\033[1;37;40m'
    board[square - 1] = color

if __name__ == "__main__":
    main()
