from pydantic import BaseModel, field_validator

class user(BaseModel):
    name: str
    email: str
    age: int
    employed : bool = False
    
    
    @field_validator('age')
    def check_age(cls, value):
        if value > 18:
            return value
        raise ValueError("Age should be greater than 18")
        
users = user(name="Bob",email = "bob@gmail.com", age=17, employed=True)
print("user Information", users)