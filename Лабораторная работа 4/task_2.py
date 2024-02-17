# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(delimiter=",", line_terminator="\n") -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, newline="", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=delimiter, lineterminator=line_terminator)
        data = []
        for row in csv_reader:
            data.append(row)
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as out_file:
        out_file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
