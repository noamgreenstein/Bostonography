import pandas

locations = [("Allston", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="Allston")),
("North End", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="North End")),
("Jamaica Plain", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="Jamaica Plain")),
("Back Bay", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="Back Bay")),
("Fenway", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="Fenway")),
("Roxbury", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="Roxbury")),
("South End", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="South End")),
("South Boston", pandas.read_excel("neighborhoodsummaryclean_1950-2010.xlsx", sheet_name="South Boston"))]


def get_pop_data(loc):
    for place in locations:
        if place[0] == loc:
            return place[1].iloc[1][13]





