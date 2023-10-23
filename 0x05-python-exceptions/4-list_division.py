#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    "divides element by element 2 lists"
    result_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("Wrong type")
        except ZeroDivisionError:
            result = 0
            print("Division by 0")
        except IndexError:
            result = 0
            print("Out of range")
        finally:
            result_list.append(result)

    return result_list
