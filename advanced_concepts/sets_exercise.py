# Eliminando repetidos de una lista con for y con sets
# [1, 1, 1, 2, 2, 3, 4] --> [1, 2, 3, 4]

def remove_duplicates(list):
    without_duplicates = []
    for element in list: # Eliminando repetidos utilizando un for
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(list):
    return list(set(my_list)) # Eliminando repetidos utilizando sets


def run():
    my_list = [1, 1, 1, 2, 2, 3, 4, 4]
    print(remove_duplicates(my_list))
    print(remove_duplicates_with_sets(my_list))


if __name__ == "__main__":
    run()