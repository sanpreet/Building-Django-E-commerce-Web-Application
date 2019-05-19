from django.shortcuts import render, redirect
from store_app.models import Products, order_details

# Create your views here.
# this function is used to store the cart items which user have added.
def cartitems(cart):
    # empty list is taken in which items will be appended.
    items=list()
    for item in cart:
        # Remeber that items so added in the database is by created using the object
        # so when id so recieved in the session is equated with item so that product 
        # corresponding to the id is reflected to the user when he/she will see the cart.

        items.append(Products.objects.get(id=item))
    # function return the variable and here the variable is items which is used in another functions    
    return items


# admin must know what is being purchased so that he/she can track the users in better way
def generateItemlist(cart):
    cart_items = cartitems(cart)
    item_list = ""
    for item in cart_items:
        item_list += str(item.name)
        item_list += ","
    return item_list    


# it is important to calculate the price of the items which is being added to the cart. This is simple mathematics and nothing special.
def pricecart(cart):
    cart_items = cartitems(cart)
    price = 0
    for item in cart_items:
        price= price + item.price
    return price    


# this is the view for the catalog.html
def catalog(request):
# if there is no item in the cart it must be blank and this function is used to empty the cart if nothing happens in the session or no value is there in the cart.    
    if 'cart' not in request.session:
        cart = list()
        request.session['cart']=[]
    # cart is the list which holdds the items which user has added in a session 
    cart = request.session['cart']
    # It contains the products which are added in the class products by creating the object for the class products. Please refer to the file Models.py for this.
    store_items = Products.objects.all()
    # to make the session not to expire
    request.session.set_expiry(0)
    # this is the context which will be passed to the catalog.html file.
    dictionary_items={'store_items':store_items, 'cart_size': len(cart)}
    
    main_page = render(request, "catalog.html", dictionary_items)
    
    # if the request so received is post then this part is executed.
    if request.method == "POST":
        cart.append(int(request.POST['obj_id']))
        return redirect('catalog')

    return main_page


# this is what is refletced in the cart.html file
def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx={
        'cart': cart, 'cart_size': len(cart),
        'cart_items': cartitems(cart),
        'total_price': pricecart(cart)
        }
    return render(request, "cart.html", ctx)


# if you want to remove the items from the cart please use this function. It is linked to remove button which is added to the cart.html. Please see the connectivity from it.
def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove = int(request.POST.get('obj_id'))
    # print("Show the object to remove +++:", obj_to_remove)
    obj_indx = request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_indx)
    return redirect('cart')


# function for checkout
def checkout(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    ctx={
        'cart': cart, 'cart_size': len(cart),
        'cart_items': cartitems(cart),
        'total_price': pricecart(cart)
        }
    
    return render(request, 'checkout.html', ctx)


# function for the completing the order
def completeorder(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    # Creating the object of the class will have the access to its functions as well as variables.
    order =order_details()
    order.first_name = request.POST.get('firstname')
    order.last_name = request.POST.get('lastname')
    order.address = request.POST.get('address')
    order.city = request.POST.get('city')
    order.payment_method = request.POST.get('payment')
    order.payment_data = request.POST.get('payment_data')
    order.items = generateItemlist(cart)
    request.session['cart']=list()
    return render(request, "complete_order.html", None)
    

