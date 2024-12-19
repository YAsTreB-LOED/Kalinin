






def sort_command(command : list[int]) -> tuple[int, int]:

    c1 = command[::2]
    c2 = command[1::2]

    return (sum(c1), sum(c2))




def main() -> None:



    command = [1, 2, 3, 4, 5, 6]

    c_sizes = sort_command(command)

    print(c_sizes)


main()
