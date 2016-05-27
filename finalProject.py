# TODO:
# Animate flash message
# Make sure that deleting a restaurant deletes the menu as well
# Make variable names more meaningful(?)
# Make sure mobile experience is accepatble

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

import cgi

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine 

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant(): 
    if request.method == 'POST':
        newRestaurant = Restaurant(name = request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash(str(newRestaurant.name) + " successfully created!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash(str(editedRestaurant.name) + " successfully modified!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html',restaurant_id=restaurant_id, i=editedRestaurant)

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deletedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(deletedRestaurant)
        session.commit()
        flash(str(deletedRestaurant.name) + " successfully deleted!")
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html', restaurant_id=restaurant_id, i=deletedRestaurant)

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], description=request.form['description'], price=request.form['price'], restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()
        flash(str(newItem.name) + " successfully created!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return render_template('editmenuitem.html')


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    deletedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash(str(deletedItem.name) + " successfully deleted!")
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html',restaurant_id=restaurant_id, menu_id=menu_id, restaurant=restaurant, deletedItem=deletedItem)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)