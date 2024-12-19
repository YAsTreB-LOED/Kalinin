





def calc_peoples(hands_c : int) -> int:

    s_start = 1

    ost = hands_c

    while True:

        ost = ost - s_start + 1

        if ost:

            # print("ost:", ost)

            s_start += 1

            # print("s_start:", s_start)

            continue

        else:

            break

    # print("s_start: ", s_start)

    return s_start





def main() -> None:

    TEST_PEOPLES_COUNT = 10  # eq 45 hands count
    TEST_HANDLE_COUNT = 45

    left_c = 7

    for i in range(1, TEST_PEOPLES_COUNT + 1):

        left_c += i - 1

    print(left_c)

    p_count = calc_peoples(left_c)

    print(p_count)



    


main()