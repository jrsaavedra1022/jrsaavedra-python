# -*- coding: utf-8 -*-
import csv

# class Contact(mdb.Model):
# 	name = mdb.StringProperty()
# 	phone = mdb.StringProperty()
# 	email = mdb.StringProperty()
# 	

class Contact():

	def __init__(self, uid, name, phone, email):
		self.uid = uid
		self.name = name
		self.phone = phone
		self.email = email

class ContactBookLibrary():

	def __init__(self):
		self._contacts = []

	def _add(self, uid, name, phone, email):
		contact = Contact(uid, name, phone, email)
		self._contacts.append(contact)

	def _save(self):
		with open('./contactos/contactos.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(('id', 'name', 'phone', 'email') )

			for contact in self._contacts:
				writer.writerow((contact.uid, contact.name, contact.phone, contact.email))


	def list_contacts(self):
		with open('./contactos/contactos.csv', 'r') as f:
			reader = csv.reader(f)
			for idx, row in enumerate(reader):
				if idx == 0:
					continue

				self._add(row[0], row[1], row[2], row[3])
		people = self._contacts
		return people

	def getLastestRegister(self):
		idLastest = 0
		contacts = self.list_contacts()
		idsContacts = []
		for contact in contacts:
			idsContacts.append(contact.uid)
		
		idLastest = max(idsContacts, key=int)

		return int(idLastest) + 1

	def saveContact(self,c=Contact):
		with open('./contactos/contactos.csv', 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow((c.uid, c.name, c.phone, c.email))
		return "File save successful !!"



	def search_contact(self, uid):
		contacts = self.list_contacts()
		contactSearch = []
		for contact in contacts:
			if contact.uid == uid:
				contactSearch = contact
				break
		return contactSearch

	def deleteContact(self, uid):
		deleteNumber = 0
		with open('./contactos/contactos.csv', 'r') as f:
			reader = csv.reader(f)
			for idx, row in enumerate(reader):
				if idx == 0:
					continue
				if row[0] == uid:
					deleteNumber = 1
					continue
				print(row[0], uid)	
				self._add(row[0], row[1], row[2], row[3])
				self._save()

		return deleteNumber







	
