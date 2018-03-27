def friend(x):
    # Code
    names = x
    Output = []
    for name in names:
        if len(name) == 4:
            Output.append(name)
    return Output


print(friend(["Ryan", "Kieran", "Jason", "Yous"]))