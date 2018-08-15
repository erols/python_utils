import csv


class CsvAddCol:
    """Class that adds a column to a given csv file and uses a supplied function to add a value to all the rows"""

    def __init__(self, in_csvfile, out_csvfile, col_name, cell_filler):
        self.in_csvfile = in_csvfile
        self.out_csvfile = out_csvfile
        self.col_name = col_name
        self.cell_filler = cell_filler

    def add_col(self):
        reader = csv.reader(open(self.in_csvfile, newline=''))
        rows = list(reader)
        rows[0].append(self.col_name)
        for i in range(1, len(rows)):
            rows[i].append(self.cell_filler(rows[i]))
        writer = csv.writer(open(self.out_csvfile, 'w', newline=''))
        writer.writerows(rows)



