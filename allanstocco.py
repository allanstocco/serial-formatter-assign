def format_serial_number(serial, length):

    # Getting serial clean and capitalized
    s_clear = ''.join(serial.upper().split('-'))

    # Using an array to work my string
    new_string = []
    for i in range(0, len(s_clear), length):
        if len(s_clear) % length == 0:
            new_string.append(s_clear[i:i+length])

        else:
            if i == 0:
                new_string.insert(0, s_clear[i])

            i += len(s_clear) % length
            new_string.append(s_clear[i:i+length])

    s_formated = '-'.join(new_string)

    # Checking if odd number we must remove a 
    if s_formated[-1] == '-':
        s_formated = s_formated[:-1]
        return print(s_formated)
    else:
        return print(s_formated)


if __name__ == '__main__':
    format_serial_number('6F2k-1d-0-z', 4)
    format_serial_number('14k-9-b', 2)
    format_serial_number('7Hnwad9Jk', 4)

    serial = str(input("Serial: "))
    l = int(input("Length: "))
    format_serial_number(serial, l)
