import csv

def read_csv_into_nested_list(csv_path):
    logs_array = []
    with open(csv_path) as logfile:
        csv_reader = csv.reader(logfile)
        for n, row in enumerate(csv_reader):
            if n > 0:
                row = list(map(float, row))
            logs_array.append(row)
    return logs_array

def read_csv_into_list_of_data_point_dicts(csv_path):
    logs_array = []
    with open(csv_path) as logfile:
        csv_reader = csv.reader(logfile)
        for n, row in enumerate(csv_reader):
            if n == 0:
                headings = row
                continue
            data_point = {}
            for n, entry in enumerate(row):
                data_point[headings[n]] = float(entry)
            logs_array.append(data_point)
    return logs_array

