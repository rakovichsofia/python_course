# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


def find_index(items: list, item_to_find: str):
    """
    Finds the first `item_to_find` item in the items list.

    Returns:
        * The first index if item was found in the list,
            None - otherwise.
    """

    if item_to_find in items:
        return items.index(item_to_find, 0)
    return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)# TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
