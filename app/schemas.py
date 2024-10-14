from app import ma
from app.models import User, Post

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
