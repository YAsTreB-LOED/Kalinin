




def select_by_val(items_count : dict[int, int], value) -> dict[int, int]:

    new_d : dict = {}

    for k, v in items_count.items():

        if v == value:

            new_d[k] = v

    return new_d







# def sort_nums(i_c_list : list[int, int]) -> list[int, int]:
    

#     ...




def Solve(nums : list[int]) -> list[int]:

    sorted_nums = []

    items_count : dict[int, int] = {}

    for i in nums:

        if not (i in items_count.keys()):

            items_count[i] = 1

        else:

            items_count[i] += 1

    print(items_count)

    i_c_list = [[k, v] for k, v in items_count.items()]

    print(i_c_list)

    i_c_list.sort(key = lambda x: x[1], reverse = True)

    for k, v in i_c_list:

        sorted_nums += [k] * v

    return sorted_nums

    # print(i_c_list)


    # s_keys = sorted(items_count.keys())

    # print("s_keys:", s_keys)

    # for s_key in s_keys:

    #     value = items_count[s_key]

    #     nums_c_eq = select_by_val(items_count, value)

    #     print("nums_c_eq:", nums_c_eq)

    #     if len(nums_c_eq.keys()) > 1:

    #         s2_key = sorted(nums_c_eq.keys())[0]

    #         # print(s2_keys)

    #         # for s2_key in s2_keys:

    #         sorted_nums += [s2_key] * nums_c_eq[s2_key] 

    #         del items_count[s_key]

    #     else:

    #         sorted_nums.append(s_key)


    # print(sorted_nums)










def main() -> None:
    

    nums = [3,2,5,7,9,5,3,7]

    sorted_nums = Solve(nums)


    print(sorted_nums)



main()