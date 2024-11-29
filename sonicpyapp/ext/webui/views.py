from flask import abort, render_template
from flask_simplelogin import login_required

from sonicpyapp.models import Product
from sonicpyapp.models import Rotation

def index():
    products = Product.query.all()
    rotations = Rotation.query.all() 
    
    for i in rotations:
        print(i.person)
    
    #sonic: create rotation query referring to product
  #  return render_template("index.html", products=products) #sonic: create rotation query referring to product
    return render_template("index.html", products=products, rotations=rotations) #sonic: create rotation query referring to product

def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(
        404, "wtf?!"
    )
    return render_template("product.html", product=product)

def rotation(rotation_id):
    print("rotation_id test:can access here:"+rotation_id)
    rotation = Rotation.query.filter_by(id=rotation_id).first() or abort(
        404, "wtf?!"
    )
    return render_template("rotation.html", rotation=rotation)



@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
