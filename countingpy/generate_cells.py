#!/usr/bin/python3
"""
generate_cells.py

Generates the cells object from the parameters 
"""

from cells_object import CellsObject
import pandas as pd


def generate_cells_obj(height=1, width=1, steps=1, filename=None, verbocity=0):
    """
    """
    cobj = CellsObject()
    df = pd.read_csv(filename, index_col=0)
    df.columns = df.columns.astype(int)
    for (y_index, rowobj) in df.iterrows():
        for (x_index, cell_value) in rowobj.items():
            print(f"For ({y_index} {type(y_index)}, {x_index} {type(x_index)}) we have value {cell_value} {type(cell_value)}")
            cobj.set_point(y_index, x_index, cell_value)

    return cobj
    


if __name__ == "__main__":
    cobj = generate_cells_obj(filename="tables/example1.csv")
