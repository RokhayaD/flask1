from flask import Blueprint, jsonify, request, send_from_directory,render_template
from app.models import db, User, Post
from app.schemas import UserSchema, PostSchema

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')
@bp.route('/users', methods=['POST'])
def create_user():
    user_schema = UserSchema()
    user_data = user_schema.load(request.json)
    user = User(**user_data)  # Créez une instance de User
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return user_schema.jsonify(users)

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    post_schema = PostSchema(many=True)
    return post_schema.jsonify(posts)

@bp.route('/posts', methods=['POST'])
def create_post():
    post_schema = PostSchema()
    post_data = post_schema.load(request.json)  
    db.session.add(post)
    db.session.commit()
    return post_schema.jsonify(post), 201

@bp.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found'}), 404

@bp.route('/swagger.json')
def swagger_json():
    return send_from_directory('static', 'swagger.json')
