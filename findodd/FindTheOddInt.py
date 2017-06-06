def find_it(seq):
    seq.sort()
    current_number = None
    times = None
    for number in seq:
        if current_number is None:
            current_number = number
            times = 1
        else:
            if number == current_number:
                times += 1
            else:
                if (times % 2) == 1:
                    return current_number
                else:
                    current_number = number
                    times = 1
    return current_number
