





def inc_list(nums : list[int]) -> list[int]:

    if not nums:

        return []
    
    new_list = []

    for idx in range(len(nums)):

        pos = idx + 1

        num = nums[idx] + pos

        if len(str(num)) > 1:

            num = int(str(num)[-1])

        new_list.append(num)

    return new_list


def main() -> None:


    nums = [5, 7, 9, 8]

    new_list = inc_list(nums)

    print(new_list)



main()