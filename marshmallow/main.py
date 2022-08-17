from marshmallow import Schema, fields, post_load, ValidationError, validates, validate


class Person:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"{self.name} is {self.age} years old."


class PersonSchema(Schema):
    name = fields.String(validate=validate.Length(max=5))
    age = fields.Integer()
    email = fields.Email()
    location = fields.String(required=True)

    @validates("age")
    def validate_age(self, age):
        if age < 18:
            raise ValidationError("The age is less than 18!")

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {
    "name": input("What is your name? "),
    "age": input("What is your age? "),
    "email": input("What is your email? "),
}

person_1 = Person(
    name=input_data["name"], age=input_data["age"], email=input_data["email"]
)
print(person_1)

person_schema = PersonSchema()
try:
    person_2 = person_schema.load(input_data)
    print(person_2)

    person_2_json = person_schema.dump(person_2)
    print(person_2_json)
except ValidationError as e:
    print(f"e: {e}")
    print(f"e.valid_data: {e.valid_data}")
