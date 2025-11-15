from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, computed_field, model_validator

class Department(str, Enum):
    IT = "IT"
    HR = "Human Resources"
    FINANCE = "Finance"
    SALES = "Sales"
    MARKETING = "Marketing"

class Employee(BaseModel):
    firstName: str = Field(
        ...,
        max_length=50,
        description="Name of the employee",
        example="John"
    ) # .... Means is required
    
    department: Department = Field(
        ...,
        description="Department of the employee",
        example=Department.IT
    )


    userName: str = Field(
        ...,
        max_length=50,
        min_length=5,
        description="Name of the user",
        example="John"
    )

    lastName: str = Field(
        ...,
        max_length=50,
        min_length=5,
        description="Name of the user",
        example="John"
    )

    password: str = Field(
        ...,
        max_length=50,
        min_length=5,
        pattern="^[a-zA-Z0-9_]*$",
        description="Password of the user",
        example="John"
    )
    confirmPassword: str = Field(
        ...,
        max_length=50,
        min_length=5,
        pattern="^[a-zA-Z0-9_]*$",
        description="Confirm Password of the user",
        example="John"
    )
    # Custom validator Run before pydantic
    @Field_validator("userName")
    def validate_user_name(cls, v):
        if "admin" in v:
            raise ValueError("Admin is not allowed")
        return v

    @model_validator(mode="after")
    def validate_password(cls, v):
        if v.password != v.confirmPassword:
            raise ValueError("Password does not match")
        return v


    @computed_field
    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"


class Comment(BaseModel):
    id: int = Field(
        ...,
        description="Id of the comment",
        example=1
    )
    constent: str = Field(
        ...,
        description="Content of the comment",
        example="Hello World"
    )
    reply: list["Comment"] = Field(
        default_factory=list,
        description="List of replies to the comment"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Timestamp of the comment"
    )

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat()
        }
    )

Comment.model_validate_json() # importent to add