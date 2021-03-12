def josephus(n):
    return (n - biggest_power_of_two(n)) * 2 + 1


def biggest_power_of_two(n):
    counter = 0
    while (n > 1):
        n //= 2
        counter += 1
    return 2 ** counter


if __name__ == '__main__':
    print(josephus(41))
