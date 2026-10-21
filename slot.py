def slot_machine(q,slot_1,slot_2,slot_3):

    plays = 0
    q = 48
    slot_1 = 3 
    slot_2 = 10
    slot_3 = 4
    while True:

        if q == 1:
            q = q - 1
            slot_1 + 1 == slot_1
            plays + 1 == plays
        elif slot_1 % 35 == 0:
            q = q + 30
        if q == 1:
            q = q - 1
            slot_2 + 1 == slot_2
            plays + 1 == plays
        elif slot_2 % 100 == 0:
            q = q + 60
        if q == 1:
            q = q - 1
            slot_3 + 1 == slot_3
            plays + 1 == plays
        elif slot_3 % 10 == 0:
            q = q + 9
        if q == 0:
            print("Martha plays", str(plays), "before going broke")
            break

