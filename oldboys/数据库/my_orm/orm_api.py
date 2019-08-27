import orm_table

from sqlalchemy.orm import sessionmaker,relationship

Session_class = sessionmaker(bind=orm_table.engine)

session = Session_class()

# addr1 = orm_table.Address(street='TianTongyuan',city='Changping',state='BJ')
# addr2 = orm_table.Address(street='Wudaokou',city='Haidian',state='BJ')
# addr3 = orm_table.Address(street='Yanjiao',city='Langfang',state='HB')
# session.add_all([addr1,addr2,addr3])
# c1 = orm_table.Customer(name="alex",billing_address=addr1,shipping_address=addr1)
# c2 = orm_table.Customer(name="jack",billing_address=addr2,shipping_address=addr2)
# c3 = orm_table.Customer(name="Tom",billing_address=addr3,shipping_address=addr3)
# session.add_all([c1,c2,c3])

obj = session.query(orm_table.Customer).filter(orm_table.Customer.name=='alex').first()
print(obj.name,obj.billing_address,obj.shipping_address)
print(obj.billing)

session.commit()





