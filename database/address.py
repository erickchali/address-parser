from database.db_models import Address, AddressSchema, db


def save_parsed_address(address_data: dict):
    model = Address(**address_data)
    db.session.add(model)
    db.session.commit()


def get_parsed_address_history():
    serializer = AddressSchema(many=True)
    address_history = Address.query.all()
    return serializer.dump(address_history)
