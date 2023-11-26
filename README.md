# Algorithme du chiffrement de Vigenère en Python

Le chiffrement de Vigenère est une méthode de chiffrement par substitution polyalphabétique. Il utilise une clé pour déterminer le décalage à appliquer à chaque lettre du texte. Voici une implémentation simple en Python.

## Code Python

### Chiffrement

```python
def chiffre_vigenere(plaintext, key):
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
```

### Déchiffrement

```python
def dechiffre_vigenere(ciphertext, key):
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
```

## Explication du Code

Le code est divisé en deux fonctions principales : `chiffre_vigenere` et `dechiffre_vigenere`, qui effectuent respectivement le chiffrement et le déchiffrement du texte.

1. **Chiffrement (`chiffre_vigenere`)**:
   - La fonction prend en entrée le texte à chiffrer (`plaintext`) et la clé de chiffrement (`key`).
   - Les lettres de la clé sont converties en majuscules pour assurer la cohérence.
   - Pour chaque lettre du texte à chiffrer, le code détermine le décalage en fonction de la lettre correspondante dans la clé.
   - Les lettres du texte à chiffrer sont déplacées circulairement en fonction du décalage pour obtenir la lettre chiffrée.
   - Les caractères non alphabétiques du texte d'origine sont conservés tels quels dans le texte chiffré.

2. **Déchiffrement (`dechiffre_vigenere`)**:
   - La fonction prend en entrée le texte chiffré (`ciphertext`) et la clé de déchiffrement (`key`).
   - Les lettres de la clé sont converties en majuscules.
   - Pour chaque lettre du texte chiffré, le code détermine le décalage en fonction de la lettre correspondante dans la clé.
   - Les lettres du texte chiffré sont déplacées circulairement en sens inverse du décalage pour obtenir la lettre déchiffrée.
   - Les caractères non alphabétiques du texte chiffré sont conservés tels quels dans le texte déchiffré.

## Exemple d'utilisation

Voici un exemple d'utilisation de l'algorithme ci-dessous :

```python
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
```

Dans ce exemple, il est demandé à l'utilisateur ce qu'il veut faire.
Il a deux choix :
- Chiffrer 
  > On lui demande de fournir le texte qu'il veut chiffrer puis la clé de chiffrement
  >
  > Le texte est alors chiffrer et on le lui affiche.
- Déchiffrer 
  > On lui demande de fournir le texte qu'il veut déchiffrer puis la clé de chiffrement
  >
  > Le texte est alors déchiffrer et on le lui affiche.
