from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    is_active: bool


user = User(name="John", age=30, is_active=True)
print(user)
print(user.dict())
print(user.json())
