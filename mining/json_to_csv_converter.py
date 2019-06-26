import argparse
import collections
import csv
import json


def read_and_write_file(json_file_path, csv_file_path, column_names):
    with open(csv_file_path, 'w+') as fout:
        csv_file = csv.writer(fout)
        csv_file.writerow(list(column_names))
        with open(json_file_path, encoding="utf8") as fin:
            for line in fin:
                line_contents = json.loads(line)
                csv_file.writerow(get_row(line_contents, column_names))


def get_superset_of_column_names_from_file(json_file_path):
    column_names = set()
    with open(json_file_path) as fin:
        for line in fin:
            line_contents = json.loads(line)
        column_names.update(set(get_column_names(line_contents).keys()))
    return column_names


def get_column_names(line_contents, parent_key=''):
    column_names = []
    for k, v in line_contents.items():
        column_name = "{0}.{1}".format(parent_key, k) if parent_key else k
        if isinstance(v, collections.MutableMapping):
            column_names.extend(get_column_names(v, column_name).items())
        else:
            column_names.append((column_name, v))
    return dict(column_names)


def get_nested_value(d, key):
    if '.' not in key:
        if key not in d:
            return None
        return d[key]
    base_key, sub_key = key.split('.', 1)
    if base_key not in d:
        return None
    sub_dict = d[base_key]
    return get_nested_value(sub_dict, sub_key)


def get_row(line_contents, column_names):
    row = []
    for column_name in column_names:
        line_value = get_nested_value(line_contents, column_name, )
        if isinstance(line_value, str):
            row.append('{0}'.format(line_value.encode('utf-8')))
        elif line_value is not None:
            row.append('{0}'.format(line_value))
        else:
            row.append('')
    return row


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Yelp data from JSON format to CSV.', )

    parser.add_argument('json_file', type=str, help='The json file to convert.', )

    args = parser.parse_args()

    json_file = args.json_file
    csv_file = '{0}.csv'.format(json_file.split('.json')[0])

    column_names = get_superset_of_column_names_from_file(json_file)
    read_and_write_file(json_file, csv_file, column_names)
