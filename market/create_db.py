from market import app
from market.models import db, Item, User
import os



items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]

app.app_context().push()
db.drop_all()
db.create_all()

user1 = User(username = "soham", email_address = "xyz@abc.com", password_hash = "1234")
db.session.add(user1)

for item_dict in items:
   item = Item(name = item_dict['name'], price = item_dict['price'], barcode = item_dict['barcode'])        
    # item2 = Item(name="Samsungef", price=900, barcode="7894", description="desc5")
   # print(User.query.filter_by(username="soham").first())
   item.owner = User.query.filter_by(username="soham").first().id
   db.session.add(item)


# items = Item.query.filter_by(name="Phone").first()
# print(items.name)
# print(items.price)
# print(items.barcode)
# print(items.owner)
# print(items.owned_user)
db.session.commit()