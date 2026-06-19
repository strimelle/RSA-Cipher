
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number%2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True

def choose_e(phi):
    for e in range(2, phi):
        if is_valid_e(e, phi):
            return e
    raise ValueError("No valid e found")

def is_valid_e(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)
    if e>1 and e < phi and gcd_value == 1:
        return True
    else:
        return False

def param(p, q):
    if is_prime(p) and is_prime(q):
        n = p * q
        phi = (p - 1) * (q - 1)
        return phi, n
    else:
        raise ValueError("Invalid parameters")


def extended_gcd(e, phi):
    if phi == 0:
        gcd_value = e
        x = 1
        y = 0
        return gcd_value, x, y

    gcd_value, x1, y1 = extended_gcd(phi, e % phi)

    x = y1
    y = x1 - (e // phi) * y1

    return gcd_value, x, y

def mod_inverse(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist")

    d = x % phi
    return d


def encrypt(message, e, n):
    encrypted_message = []
    for symbol in message:
        m = ord(symbol) #pavercia i sk

        if m>=n:
            raise ValueError("Message must be less than n")
        c = pow(m, e, n) #RSA sifravimas
        encrypted_message.append(c)
    return encrypted_message


def decrypt(message, d, n):
    decrypted_message = ""
    for c in message:
        m = pow(c, d, n) #RSA desifravimas
        symbol = chr(m) #pavercia atgal i simboli
        decrypted_message += symbol

    return decrypted_message
