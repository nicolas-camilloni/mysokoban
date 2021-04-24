def bdd(value):
    host = "localhost"
    user = "root"
    password = ""
    database = "pokoban"

    if value == "getHost":
        return host
    if value == "getUser":
        return user
    if value == "getPassword":
        return password
    if value == "getDatabase":
        return database