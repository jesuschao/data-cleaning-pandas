def quitar_a(x):
    if ".a" in str(x):
        return x.replace(".a", "")
    else:
        return x

def quitar_b(x):
    if ".b" in str(x):
        return x.replace(".b", "")
    else:
        return x

def quitar_c(x):
    if ".c" in str(x):
        return x.replace(".c", "")
    else:
        return x

def quitar_d(x):
    if ".c" in str(x):
        return x.replace(".d", "")
    else:
        return x

def quitar_R(x):
    if ".R" in str(x):
        return x.replace(".R", "")
    else:
        return x

def year_(x):
    if ".0" in str(x):
        return str(x).replace(".0", "")
    else:
        return x

def type_(x):
    if "Unprovoked" in str(x):
        return x.replace("Unprovoked", "Accidental")
    else:
        return x

def type_1(x):
    if "Boatomg" in str(x):
        return x.replace("Boatomg", "Boat")
    else:
        return x

def type_2(x):
    if "Invalid" in str(x):
        return x.replace("Invalid", "Injured/Fatal")
    else:
        return x

def upper_c(x):
    return str(x).upper()

def england_(x):
    if "ENGLAND" in str(x):
        return x.replace("ENGLAND", "UNITED KINGDOM")
    else:
        return x

def question_(x):
    if "?" in str(x):
        return x.replace("?", "")
    else:
        return x

def gender_(x):
    special_characters = 'FM'
    if str(x) in special_characters:
        return x
    else:
        return str(x).replace(str(x), "None")

def fatal_(x):
    special_characters = 'NYy'
    if str(x) in special_characters:
        return x.upper()
    else:
        return str(x).replace(str(x), "None")