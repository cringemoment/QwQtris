def hold_reorders(queue):
    if len(queue) <= 1:
        return set(queue)  # base case

    result = set()

    a = hold_reorders(queue[1:])  # use first piece, work on the 2nd-rest
    for part in a:
        result.add(queue[0] + part)

    b = hold_reorders(queue[0] + queue[2:])  # use second piece, work on 1st + 3rd-rest
    for part in b:
        result.add(queue[1] + part)

    return list(result)

print(hold_reorders("IOSZJLT"))
