#! /usr/bin/env python3
# import
import classe
import random_passWord
import logIn
import maskpass

# main
if __name__ == '__main__':

    print("Bienvenue dans votre gestionnaire de mot de passe ! \nConnectez vous au programme :)\n")
    username = input("Enter username: ")
    connection_password = maskpass.askpass(mask='*')
    connection_to_the_program = logIn.connection(username, connection_password)

    while not connection_to_the_program:

        print('Identifiant ou mot de passe incorrecte. Veuillez réssayer.\n')
        username = input("Enter username: ")
        connection_password = maskpass.askpass(mask='*')
        connection_to_the_program = logIn.connection(username, connection_password)

    if connection_to_the_program:

        wallet = classe.Wallet()
        data = wallet.opening()
        condition = True

        while condition:

            question = input('\nQue voulez vous faire ?\n')
            print('Taper "nouveau" pour pouvoir ajouter un mot de passe\n')
            print('Taper "supprimer" pour supprimer un mot de passe\n')
            print('Taper "modifier" pour modifier un mot de passe \n')
            print('Taper "afficher" pour afficher un mot de passe \n')
            print('Taper "enregistrer" pour enregistrer et fermer le programme\n')
            print('Taper "fin" pour fermer le programme \n=>')

            match question:

                case "nouveau":

                    site = input('Entrez un nouveau site: ')
                    identify = input('Entrez votre identifiant: ')
                    password = input('Voulez vous un mot de passe généré automatiquement ? oui/non ')

                    if password == "non":
                        password = input('Entrez votre mot de passe: ')
                    else:
                        password = random_passWord.automatic_random_password()

                    wallet.logs(site, id, password)
                    print(f'\n---------- Le mot de passe du site "{site}" a bien été ajouté ----------\n')
                    print(f"- {site} | identifiant: {identify} | password: {password}\n")

                case "supprimer":

                    delete = input('Quelle mot de passe voulez vous supprimer ? Entrez le site en question ')
                    print(f'\n---------- Le mot de passe du site "{delete}" a bien été supprimé ----------\n')
                    wallet.delete_password(delete)

                case "modifier":

                    site = input('Quel mot de passe voulez vous modifier ? Entrez le site en question ')
                    password = wallet.edit(site)
                    print(f'\n---------- Le mot de passe du site "{site}" a bien été modifié ----------\n')
                    wallet.create_password(site, password)

                case "enregistrer":

                    wallet.save()
                    print('\n---------- Vos mots de passe ont bien été enregistrés ----------')

                case "afficher":

                    wallet.viewing()

                case "fin":

                    condition = False
