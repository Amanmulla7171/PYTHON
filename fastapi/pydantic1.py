from pydantic import BaseModel

class user(BaseModel):
    name:str
    age:int
    email:str

def insert_user(user:user):
    print(user.name)
    print(user.age)
    print(user.email)

user_info={"name":"aman","age":22,"email":"aman@gmail.com"}
user2=user(**user_info)
insert_user(user2)
