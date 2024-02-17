number_of_pages = 100
number_of_lines_per_page = 50
number_of_characters_per_line = 25
disk_capacity_mb = 1.44
character_size_bytes = 4
number_of_characters = number_of_pages * number_of_lines_per_page * number_of_characters_per_line
book_size_bytes = number_of_characters * character_size_bytes
book_size_mb = book_size_bytes / (1024 ** 2)
number_of_books = int(disk_capacity_mb // book_size_mb)
print("Количество книг, помещающихся на дискету:", number_of_books)
