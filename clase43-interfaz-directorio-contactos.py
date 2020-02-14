# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        #print('name: {}, phone: {}, email: {}'.format(name, phone, email))
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print("--- * --- * --- * --- * --- * --- * --- * --- * --- * ---")
        print("Nombre: {}".format(contact.name))
        print("Telefono: {}".format(contact.phone))
        print("Email: {}".format(contact.email))
        print("--- * --- * --- * --- * --- * --- * --- * --- * --- * ---")

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update_contact(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                print("Contacto a actualizar: ")
                nameUP = str(input("Ingresa el nuevo nombre del contacto: "))
                phoneUP = str(input("Ingresa el nuevo Telefono del contacto: "))
                emailUP = str(input("Ingresa el amail del contacto: "))
                contactNew = Contact(nameUP, phoneUP, emailUP)
                self._contacts[idx] = contactNew
                self._save()
                print("Contacto Actualizado !!")
                break
        else:
            self._not_found()

    def _save(self):
        with open('./contactos/contacts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(( 'name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


    def _not_found(self):
        print("*********************")
        print("No encotnrado !!!")
        print("*********************")


def run():
    c_book = ContactBook()

    with open('./contactos/contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            c_book.add(row[0], row[1], row[2])


    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input("Escribe el nombre del contacto: "))
            phone = str(input("Escribre el telefono del contacto: "))
            email = str(input("Escribe el email del contacto: "))

            c_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input("Escribe el nombre del contacto: "))
            c_book.update_contact(name)

        elif command == 'b':
            name = str(input("Escribe el nombre del contacto: "))
            c_book.search(name)

        elif command == 'e':
            name = str(input("Escribe el nombre del contacto: "))
            c_book.delete(name)

        elif command == 'l':
            print('listar contactos: ')
            c_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print("B I E N V E N I D O S  A  L A  A G E N D A")
    run()