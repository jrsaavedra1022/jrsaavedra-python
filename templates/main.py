from flask import Flask, render_template, request, flash, redirect
from contactModels import ContactBookLibrary
from contactModels import Contact
app = Flask(__name__) 
app.secret_key = 'some_secret'
app.debug = True


@app.route(r'/', methods=['GET'])
def contact_book():
	# contacts = Contact.query().fetch()
	c_book = ContactBookLibrary()
	contacts = c_book.list_contacts()

	return render_template('contact_book.html', contacts=contacts)

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
	c_book = ContactBookLibrary()
	idContact = c_book.getLastestRegister()

	if request.form:
		contact = Contact(uid=request.form.get('uid'),
						name=request.form.get('name'),
						phone=request.form.get('phone'),
						email=request.form.get('email'))
		print(request.form.get('uid'))
		print(request.form.get('name'))
		print(request.form.get('phone'))
		print(request.form.get('email'))
		c_book.saveContact(contact)
		flash("Se agrego el contacto Exitosamente !!")



	return render_template('add_contact.html', idContact=idContact)

@app.route(r'/contacts/<uid>', methods=['GET'])
def contact_details(uid):
	# contact = Contact.get_by_id(int(uid))
	c_book = ContactBookLibrary() 
	contact = c_book.search_contact(uid)

	return render_template('contact.html', contact=contact)


@app.route(r'/delete', methods=['POST'])
def delete_contact():
	c_book = ContactBookLibrary() 
	if request.form:
		uid = request.form.get('uid')
		validate = c_book.deleteContact(uid)

		if validate == 1:
			return redirect('/', code=301)

	return redirect('/contacts/{}'.format(uid))

if __name__ == '__main__':
	app.run()

