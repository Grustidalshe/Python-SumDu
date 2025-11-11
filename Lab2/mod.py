def athlet(m, k):
    day = 0
    percent = k / 100

    max_km = 50
    while not (m > max_km):
        delta = m * percent
        m += delta
        day += 1

    return day
