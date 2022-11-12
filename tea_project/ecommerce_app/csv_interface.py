import csv

class CSV_Interface:
    def __init__(self, filename):

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            self.column_names = reader.fieldnames

        self.filename= filename
        self.all_data = self.update_data_from_file()

    def update_data_from_file(self):
        data = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        self.all_data = data
        return self.all_data

    def append_one_row_to_file(self, new_data_dict):
        with open(self.filename, "a", newline='') as f:
            writer = csv.DictReader(f, fieldnames=self.column_names)
            writer.writerow(new_data_dict)

        self.update_data_from_file()
        return self.all_data


