T2X2 = {"HP": 100, "ST": 100, "DM": 10, "Mana": 50, "MD": 10}
Ct0m = {"HP": 100, "ST": 100, "DM": 10, "Mana": 50, "MD": 10}

def attack_DM(P1, P2):
    if P1["ST"] > 25:
        P2["HP"] -= P1["DM"]
        P1["ST"] -= 25
    elif P1["ST"] < -30:
        P1["HP"] -= 1000
    else:
        P1["HP"] -= 10
        P2["HP"] -= (P1["DM"] / 2)
        P1["ST"] -= 25
        P1["ST"] += 10

def attack_MD(P1, P2):
    if P1["Mana"] > 25:
        P2["HP"] -= P1["MD"]
        P1["Mana"] -= 25
    elif P1["Mana"] <= -25:
        P1["HP"] -= 1000
    else:
        P1["HP"] -= 10
        P2["HP"] -= (P1["MD"] / 2)
        P1["Mana"] -= 25
        P1["Mana"] += 10

def rest(P1):
    P1["ST"] += 10
    if P1["HP"] < 100:
        P1["HP"] += 4
    if P1["HP"] > 100:
        P1["HP"] = 100
    P1["Mana"] += 10

def show_info():
    print(f"T2X2 | HP - {T2X2["HP"]} | ST - {T2X2["ST"]} | DM - {T2X2["DM"]} | Mana - {T2X2["Mana"]} | MD - {T2X2["MD"]} ")
    print(f"Ct0m | HP - {Ct0m["HP"]} | ST - {Ct0m["ST"]} | DM - {Ct0m["DM"]} | Mana - {Ct0m["Mana"]} | MD - {Ct0m["MD"]} ")
    print("====================================================================================================")

def action(Niga_one_Niga_two):
    n = 'True'
    if Niga_one_Niga_two == 'c':
        while n == 'True':
            A1 = input('Выбери действие для Ct0m (d - attack_DM, m - attack_MD, r - rest): ')
            A2 = input('Выбери действие для T2X2 (d - attack_DM, m - attack_MD, r - rest): ')
            if A1 == 'd':
                attack_DM(Ct0m, T2X2)
            elif A1 == 'm':
                attack_MD(Ct0m, T2X2)
            elif A1 == 'r':
                rest(Ct0m)
            if A2 == 'd':
                attack_DM(T2X2, Ct0m)
            elif A2 == 'm':
                attack_MD(T2X2, Ct0m)
            elif A2 == 'r':
                rest(T2X2)
            show_info()
            if T2X2["HP"] < 0 or Ct0m["HP"] < 0:
                if T2X2["HP"] < 0:
                    print('WIN', 'Ct0m')
                    show_info()
                    n = 'False'
                    break
                else:
                    print('WIN', 'T2X2')
                    show_info()
                    n = 'False'
                    break
            if T2X2["HP"] < 0 and Ct0m["HP"] < 0:
                print('DRAW')
                show_info()
                n = 'False'
                break
    elif Niga_one_Niga_two == 't':
        while n == 'True':
            A1 = input('Выбери действие для T2X2 (d - attack_DM, m - attack_MD, r - rest): ')
            A2 = input('Выбери действие для Ct0m (d - attack_DM, m - attack_MD, r - rest): ')
            if A1 == 'd':
                attack_DM(T2X2, Ct0m)
            elif A1 == 'm':
                attack_MD(T2X2, Ct0m)
            elif A1 == 'r':
                rest(T2X2)
            if A2 == 'd':
                attack_DM(Ct0m, T2X2)
            elif A2 == 'm':
                attack_MD(Ct0m, T2X2)
            elif A2 == 'r':
                rest(Ct0m)
            show_info()
            if T2X2["HP"] < 0 or Ct0m["HP"] < 0:
                if T2X2["HP"] < 0:
                    print('WIN', 'Ct0m')
                    show_info()
                    n = 'False'
                    break
                else:
                    print('WIN', 'T2X2')
                    show_info()
                    n = 'False'
                    break
            if T2X2["HP"] < 0 and Ct0m["HP"] < 0:
                print('DRAW')
                show_info()
                n = 'False'
                break




Niga_one_Niga_two = input('Выбери кто ходит первый Ct0m или T2X2 (c(англ.яз) или t(англ.яз)): ')
action(Niga_one_Niga_two)