def chiffre_vigenere(plaintext, key):
    """
    Chiffre le texte en utilisant le chiffre de Vigenère.

    :param plaintext: Le texte à chiffrer.
    :param key: La clé de chiffrement.
    :return: Le texte chiffré.
    """
    ciphertext = ""
    key = key.upper()  # Convertir la clé en majuscules
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Déterminer le décalage en fonction de la lettre de la clé
            key_char = key[key_index]
            key_shift = ord(key_char) - ord('A')

            # Chiffrer la lettre
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

            ciphertext += encrypted_char

            # Passer à la lettre suivante de la clé
            key_index = (key_index + 1) % len(key)
        else:
            # Conserver les caractères non alphabétiques tels quels
            ciphertext += char

    return ciphertext


def dechiffre_vigenere(ciphertext, key):
    """
    Déchiffre le texte en utilisant le chiffre de Vigenère.

    :param ciphertext: Le texte chiffré.
    :param key: La clé de déchiffrement.
    :return: Le texte déchiffré.
    """
    plaintext = ""
    key = key.upper()  # Convertir la clé en majuscules
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            # Déterminer le décalage en fonction de la lettre de la clé
            key_char = key[key_index]
            key_shift = ord(key_char) - ord('A')

            # Déchiffrer la lettre
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

            plaintext += decrypted_char

            # Passer à la lettre suivante de la clé
            key_index = (key_index + 1) % len(key)
        else:
            # Conserver les caractères non alphabétiques tels quels
            plaintext += char

    return plaintext


# Exemple d'utilisation
print("Que voulez vous faire ??")
print("1. Chiffrer")
print("2. Déchiffrer")
choix = int(input("Veillez entrer 1 ou 2 --> "))

while choix != 1 and choix != 2:
    print("ERREUR...")
    choix = int(input("Veillez entrer 1 ou 2 --> "))

if choix == 1:
    texte_original = input("Entrez le texte à crypter : ")
    cle = input("Quel est votre clé ?? ")
    texte_chiffre = chiffre_vigenere(texte_original, cle)
    print("")
    print("Texte original:", texte_original)
    print("Texte chiffré:", texte_chiffre)
else:
    texte_chiffre = input("Entrez le texte à décrypter : ")
    cle = input("Quel est votre clé ?? ")
    texte_dechiffre = dechiffre_vigenere(texte_chiffre, cle)
    print("")
    print("Texte chiffré:", texte_chiffre)
    print("Texte déchiffré: ", texte_dechiffre)
