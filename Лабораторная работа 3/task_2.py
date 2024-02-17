# TODO Напишите функцию find_common_participants


def find_common_participants(first: str, second: str, sep: str = ",") -> list:
    """
    Finds the common participants in the 2 strings.
    Firstly this strings should be compared in the list by `sep`.

    Args:
        * first - The first group of participants
        * second - The second group of participants
        * sep - Separator

    Returns:
        The list of the common participants in the 2 groups.
    """

    first_list = first.split(sep)
    second_list = second.split(sep)
    common = []
    for participant in first_list:
        if participant in second_list:
            common.append(participant)
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
