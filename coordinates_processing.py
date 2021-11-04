def check(cord):
    if len(cord.split(",")) != 2:
        return False
    for val in cord.split(","):
        try:
            x = float(val.strip())
        except Exception:
            return False
    return True
def cords(cord):
    res = []
    for val in cord.split(","):
        res.append(float(val.strip()))
    return res     