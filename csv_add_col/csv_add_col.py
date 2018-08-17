import csv


class CsvAddCol:
    """Add a column to a given csv file and use a supplied function to add a value to all the rows"""

    def __init__(self, in_csvfile, out_csvfile, col_name, cell_filler):
        """Add a new column to a csv file and fill the new cells

        Keyword arguments:
        in_csvfile - string - the path to the csv file
        out_csvfile - string - the path to save the new file to
        col_name - string - name of the new column
        cell_filler - function - add the desired values in the new column"""
        self.in_csvfile = in_csvfile
        self.out_csvfile = out_csvfile
        self.col_name = col_name
        self.cell_filler = cell_filler

    def add_col(self):
        """open csv to read obj, add column, fill new cells, save to new csv"""
        reader = csv.reader(open(self.in_csvfile, newline=''))
        rows = list(reader)
        rows[0].append(self.col_name)
        for i in range(1, len(rows)):
            rows[i].append(self.cell_filler(rows[i]))
        writer = csv.writer(open(self.out_csvfile, 'w', newline=''))
        writer.writerows(rows)



