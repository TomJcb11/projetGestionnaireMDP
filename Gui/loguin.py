import json
from tkinter import messagebox
from tkinter import simpledialog
from classes import *


class LogGuiIn:
    def __init__(self):
        self.login()

    @staticmethod
    def login():
        with open('connexionId.json', 'r') as user_data:
            data_json = json.load(user_data)

        firstname = data_json["firstname"]
        while firstname == "":
            firstname = simpledialog.askstring("Input", "Entrer votre prénom")
        lastname = data_json["lastname"]
        while lastname == "":
            lastname = simpledialog.askstring("Input", "Entrer votre nom")
        security_question = data_json["question"]
        while security_question == "":
            security_question = simpledialog.askstring("Input", "Dans quel ville êtes vous né "
                                                                "(cette question sera une question de "
                                                                "sécurité au cas ou"
                                                                " vous oublieriez votre mot de passe)?")
        User.write_names(firstname, lastname, security_question)

        new_password = ""
        while new_password == "":
            new_password = simpledialog.askstring("Input", "Veuillez vous créer un mot de passe")
        Account.create_account(new_password)

        connection_password = simpledialog.askstring("Input",
                                                     "Bienvenue dans votre gestionnaire de "
                                                     "mot de passe ! \nConnectez vous au programme \n")
        # hide password while writing
        connection_to_the_program = Account.verify_account(connection_password)

        while not connection_to_the_program:

            connection_password = simpledialog.askstring("Input", "Mot de passe incorrect. Veuillez réssayer, "
                                                                  "si vous avez oublié votre mot de passe taper f.\n")
            if connection_password == "f":
                connection_password = simpledialog.askstring("Input", "Dans quel ville êtes vous né ? ")
                with open("connexionId.json") as verify_question:
                    question = json.load(verify_question)
                if question["question"] != connection_password:
                    while question["question"] != connection_password:
                        messagebox.showerror(title="Erreur", message="Mauvaise réponse")
                        connection_password = simpledialog.askstring("Input", "Dans quel ville êtes vous né ? ")
                    connection_password = question["user"]["password"]
                else:
                    connection_password = question["user"]["password"]
            connection_to_the_program = Account.verify_account(connection_password)
