










def ip_to_int32(ip : str) -> int:

    ip_nums : list[int] = [int(i) for i in ip.split(".")]

    number = int.from_bytes(bytes(ip_nums), "big")

    return number



def main() -> None:

    ip = "128.114.17.104"

    number = ip_to_int32(ip)

    print(number)
    

main()