"""
Json navigator programm!!
"""
import json
import copy
import sys


def read_data(path):
    """
    This function reads information from json file and retuns it. If path type
    is not str, the function returns None
    >>> read_data([])

    """
    if not isinstance(path, str):
        return None
    with open(path) as file:
        data = json.load(file)
        return data


def get_dict_info(data):
    """
    If input data type is dict, then navigate this way. If data type is not
    dict, the function returns None
    >>> get_dict_info('123')

    """
    if not isinstance(data, dict):
        return None
    keys = [ind for ind in data]
    for ind in range(len(keys)):
        print(str(ind + 1) + ")", keys[ind])
    print("\nA) Enter one of the keys mentioned above\nB) Enter \
'-1' to go one level back\nC) Enter 'get' to print current dictionary")
    while True:
        answer = input()
        if answer == '-1':
            return -1
        if answer in keys or answer.lower() == 'get':
            return answer
        print('Enter one of the keys mentioned above:')
        answer = input()


def get_list_info(list_data):
    """
    If input data type is list, then navigate this way. If data type is not
    list, the function returns None
    >>> get_list_info({123})

    """
    if not isinstance(list_data, list):
        return None
    while True:
        try:
            print("The number of items in list: " + str(len(list_data)))
            print("Enter the index of an item you want to get in range \
[0, " + str(len(list_data) - 1) + "]")
            print("To go back, type '-1'\nTo print all information, \
enter 'get'")
            answer = input()
            if answer.lower() == "get":
                print("\n", list_data, "\n")
            elif int(answer) <= len(list_data) - 1 and int(answer) >= -1:
                return int(answer)
        except:
            continue


def return_back(data, keys):
    """
    This function is used to get the user back in navigation in JSON file.
    if data type is not
    """
    keys = copy.deepcopy(keys)[:-1]
    result = copy.deepcopy(data)
    for ind in keys:
        result = result[ind]
    main(data, result, keys)


def main(data, list_data, keys):
    """
    This is the function to navigate through JSON file
    """
    if isinstance(list_data, list):
        choice = get_list_info(list_data)
        if choice == -1:
            return_back(data, keys)
        else:
            keys.append(choice)
            main(data, copy.deepcopy(list_data[choice]), keys)
    elif isinstance(list_data, dict):
        answer = get_dict_info(list_data)
        if answer == -1:
            return_back(data, keys)
        elif answer.lower() == "get":
            print(list_data)
        else:
            keys.append(answer)
            main(data, list_data[answer], keys)
    else:
        print("\n", list_data, "\n")
        while True:
            print("You have reached the end! Enter '-1' to return back or \
'quit' to stop programm execution")
            answer = input()
            if answer == '-1':
                return_back(data, keys)
            elif answer == 'quit':
                sys.exit()
        main(data, list_data, keys)


def start_navigation():
    """
    This is the main function in this module to start the navigation through\
    JSON file
    """
    print('Enter a path to JSON file you want to navigate: ')
    path = input()
    data = read_data(path)
    print("Hello!\nThis app will help you to navigate through JSON file\n")
    main(data, copy.deepcopy(data), [])


if __name__ == '__main__':
    start_navigation()
