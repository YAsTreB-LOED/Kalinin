



def join_strs(a : str, b : str) -> str:

    if len(b) > len(a):

        a, b = b, a

    return b + a[::-1] + b




def main() -> None:



    a = "|12345|"
    b = "|987654|"

    out = join_strs(a, b)

    print(out)


main()