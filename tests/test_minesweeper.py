import pytest
import minesweeper
from minesweeper.minesweeper import Minesweeper

def test_module_exits():
    assert minesweeper
    
    
def test_place_mines():
    game=Minesweeper(3,3,2)
    game.place_mines()
    assert len(game.mines)==2    
    
def test_game_over():
    game=Minesweeper(3,3,2)
    game.place_mines()
    r,c=next(iter(game.mines))
    assert game.reveal(r,c)=="Game Over"
    
    
def test_reveal():
    import random
    random.seed(0)
    game = Minesweeper(3, 3, 2)
    game.place_mines()
    result=game.reveal(2, 2)
    assert (2,2) in game.revealed
    assert result in ("Continue","Game Over","You Win")    
    
def test_is_winner():
    game = Minesweeper(2, 2, 1)
    for r in range(2):
        for c in range(2):
            if (r,c) not in game.mines:
                game.reveal(r,c)
                
    assert game.is_winner() is True  
    
def test_get_board():
    game = Minesweeper(2, 2, 1)
    for r in range(game.rows):
        for c in range(game.cols):
            if (r, c) not in game.mines:
                safe_cell = (r, c)
                break
            else:
                continue
        break   
    r,c=safe_cell
    game.reveal(r,c)
    board=game.get_board()
    assert board[r][c]!="■" 