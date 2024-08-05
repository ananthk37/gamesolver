from urllib.request import urlopen
from bs4 import BeautifulSoup
from sudoku_solver import solve, console_print

base_url = 'https://five.websudoku.com/'


def scrape_problem():
    """
        Scrape sudoku problem from website into usable format for solver
        using beautifulsoup4.
    """
    page = urlopen(base_url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    
    
    all_cells = soup.find_all("input")
    inital_board = {}
    wanted_classes = {'s0'}
    for cell in all_cells:
        try:
            if cell['class'][0] in wanted_classes:
                cell_index = cell['id'][1:]
                row, col = [int(i) for i in list(cell_index)]
                inital_board[row * 9 + col] = int(cell['value'])
                
        except KeyError:
            continue
    return inital_board


if __name__ == '__main__':
    board = scrape_problem()
    console_print(solve(board))

    pass