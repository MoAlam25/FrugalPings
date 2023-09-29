import json
import logging

def handle_amazon_entry(new_entry):
    ref = db.reference('Amazon')
    amazon_ref = ref.child(new_entry['ASIN'])
    amazon_ref_data = amazon_ref.get()
    if amazon_ref_data is None:
        add_new_amazon_entry(new_entry)
        create_notification_amazon(Notification_type.CREATION, new_entry, current_entry=None)
    else:
        if(discount_present(amazon_ref_data['price'], new_entry['finalPrice']['value'])):
            create_notification_amazon(Notification_type.UPDATE, new_entry, amazon_ref_data)
            update_amazon_entry(new_entry)