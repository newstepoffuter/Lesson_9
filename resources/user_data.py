from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_number: str
    month: str
    year: str
    day: str
    gender: str
    subjects: str
    hobbies: str
    images: str
    current_address: str
    state: str
    city: str


new_user = User(
    first_name='Alexandro',
    last_name='Gonzales',
    user_email='Agonzales@gmal.com',
    user_number='1234567890',
    month='April',
    year='2001',
    day='7',
    gender='Male',
    hobbies='Music',
    images='123.png',
    current_address='India',
    subjects='Computer Science',
    state='Uttar Pradesh',
    city='Merrut',
)
