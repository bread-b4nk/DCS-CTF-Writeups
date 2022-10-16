import socket
import chess
import chess.engine


def main():
    # Set up stockfish, a chess engine we'll use to solve the problem
    engine = chess.engine.SimpleEngine.popen_uci(r"/usr/local/bin/stockfish")

    # Socket connection to Deadface server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('grandmaster.deadface.io', 5000))

    # Get instructions and board to solve
    print(sock.recv(4096).decode())   # Instructions: "Which move forces mate in 2?"
    board = sock.recv(4096).decode()  # Receives an ascii chess board
    print(board)

    # Turn the ascii board into a FEN (standardized board representation) which
    # we can insert into the chess engine
    fen = constructFen(board)

    # Creating board from the FEN, feeding it to the chess engine
    board = chess.Board(fen=fen)
    move = engine.play(board, chess.engine.Limit(time=0.1))  # get next move within .1 secs
    move = str(move.move)                                    # extract move as a string

    # Change move (e.g. a1b2) into a move object (by extracting its start square
    # and end square) which can be converted to Standard Algebraic Notation
    move = chess.Move(chess.parse_square(move[0:2]),
                      chess.parse_square(move[2:]))
    move = board.san(move)  # standard algebraic notation

    # Send the best move to the server and print out the received flag
    sock.send(move.encode())
    print(move)
    print(sock.recv(4096).decode())


def constructFen(asciiBoard):
    """Construct a FEN from an ASCII board created by python-chess.

    See python-chess.readthedocs.io/en/latest/ for the format of the board
    See https://www.chess.com/terms/fen-chess for the format of FEN
    """
    fen = ""
    emptyCount = 0

    for char in asciiBoard:
        if char == " ":           # Ignore spaces
            continue
        if char == '.':           # . = empty square; keep track of how many
            emptyCount += 1
        else:
            if emptyCount != 0:   # add number of empty spaces to FEN
                fen += str(emptyCount)
            emptyCount = 0

            if char == '\n':      # newlines = rows of the board
                fen += "/"
            else:
                fen += char

    return(fen[:-1])              # cut off excess "/" at end of created fen


if __name__ == '__main__':
    main()
