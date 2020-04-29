import numpy as np 
import cv2

#only change block_size to vary the chess board size
block_size = 30

chess_board = np.zeros((block_size * 8, block_size * 8))
kernel = np.ones((block_size, block_size)) * 255

for i in range(0, block_size * 8, block_size):
    for j in range(0, block_size * 8, block_size):
        if ((i + j) // (block_size)) % 2 == 0:
            chess_board[i:i + block_size, j:j + block_size] = kernel

cv2.imshow("chess_board", chess_board)
cv2.waitKey(0)
cv2.destroyAllWindows()
