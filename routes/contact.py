from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts',__name__)

@contacts.route("/")
def index():
    contacts = Contact.query.all()
    db.session.close()
    return render_template('index.html', contacts=contacts, contact = "")

@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    print(fullname, " ", email, " ", phone)

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()
    flash("contact added successfully!")
    return redirect(url_for('contacts.index'))


@contacts.route('/update/<id>', methods= ['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        print("metodo get")
        contact = Contact.query.get(id)
        db.session.close()
        flash("contact found successfully!")
        return render_template('index.html', contacts="", contact_update = contact)

    if request.method == 'POST':
        print("metodo post")
        contact = Contact.query.get(id)
        
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()
        db.session.close()
        flash("contact update successfully!")
        return redirect(url_for('contacts.index'))


@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    db.session.close()
    flash("contact deleted successfully!")
    return redirect(url_for('contacts.index'))


@contacts.route("/about")
def about():

    return render_template('about.html')

