rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

grid = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."

def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def grid_values(grid):
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))
    pass

def replace_dots(d_grid):
    d_grid.update((k, '123456789') for k,v in d_grid.items() if v == '.')
    # for k, v in d_grid.items():
    #     if v == '.':
    #         d_grid[k] = '123456789'
    return d_grid

def eliminate(d_grid):
    for k, v in d_grid.items():
        if len(v) != 1:
            # iterate peers of v
            for p in peers[k]:
                if len(d_grid[p]) == 1:
                    d_grid[k] = d_grid[k].replace(d_grid[p], '')
    return d_grid

def only_choice(d_grid):


g_values = grid_values(grid)
# display(g_values)
modified_g_values = replace_dots(g_values)
# display(modified_g_values)
eliminated_g_values = eliminate(modified_g_values)
display(eliminated_g_values)
