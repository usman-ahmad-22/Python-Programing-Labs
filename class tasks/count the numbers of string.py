while True:
    import os
    os.system('cls')

    s=input('enter a string or number : ')
    o=s.count('')
    o-=1
    print(o)
    rerun = input("DO you want to count more? (yes/y): ")
    if rerun.lower() != "y" and rerun.lower() != "yes": # .lower() means it convert every upper/lower case word into lowercase
        break