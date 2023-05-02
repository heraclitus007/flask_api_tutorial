from market import app, db, Item
import os

if os.path.exists('instance/market.db'):
   os.remove('instance/market.db')

items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]

app.app_context().push()
db.create_all()

for item_dict in items:
   item = Item(name = item_dict['name'], price = item_dict['price'], barcode = item_dict['barcode'])        
    # item2 = Item(name="Samsungef", price=900, barcode="7894", description="desc5")
   db.session.add(item)

db.session.commit()