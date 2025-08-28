from db import engine
from models import Address, User
from sqlalchemy import select
from sqlalchemy.orm import Session

# Create:
with Session(engine) as session:
    user_01 = User(
        name='User 01',
        fullname='User 01 Fullname',
        addresses=[Address(email_address='user-01@email.01')],
    )
    user_02 = User(
        name='User 02',
        fullname='User 02 Fullname',
        addresses=[
            Address(email_address='user-02@email.01'),
            Address(email_address='user-02@email.02'),
        ],
    )
    user_02.addresses.append(Address(email_address='user-02@email.03'))
    session.add_all([user_01, user_02])
    session.commit()

# Read:
with Session(engine) as session:
    users = session.scalars(select(User)).all()
    for user in users:
        print(user)
        print(user.addresses)
        print('---')

# Update:
with Session(engine) as session:
    email = session.scalars(
        select(Address).where(Address.email_address == 'user-02@email.02')
    ).first()
    if email:
        email.email_address = 'user-02@email.02-updated'
        session.commit()

# Delete:
USER_ID = 1
with Session(engine) as session:
    get_user = session.get(User, USER_ID)
    # get_user = session.exec(select(User).where(User.id == USER_ID)).first()
    if get_user:
        session.delete(get_user)
        session.commit()

