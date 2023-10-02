from flask import render_template, request, url_for, Blueprint
from flask_login import current_user, login_required
from firestorm.models import User, Post
import pytz
from datetime import datetime, timedelta
from pytz import timezone
from sqlalchemy import func

import base64
from PIL import Image
from io import BytesIO




main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5) #5 posts per page 
    return render_template('home.html', posts=posts)


@main.route("/home")


def decode_base64_image(picture_data):
    decoded_data = base64.b64decode(picture_data)
    image = Image.open(BytesIO(decoded_data))
    return image


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/party", methods=['GET', 'POST'])
@login_required 
def party():
    # For user header, can be removed 
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

   #Select timezone 
    selected_timezone = pytz.timezone('America/Los_Angeles')

    # Calculate current time in timezone 
    current_time_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    current_time_in_zone = current_time_utc.astimezone(selected_timezone)
    current_date_in_zone = current_time_in_zone.date()      
    
    print("Selected_timezone:", selected_timezone)
    print("Current_time_in_zone:", current_time_in_zone)
    print("Current_date_in_zone:", current_date_in_zone)
    

    users = User.query.all()
    posts = Post.query.filter(func.date(Post.date_posted) == current_date_in_zone
    ).order_by(Post.date_posted.desc()).all()
    
    print("users: ", users)
    print("current user: ", current_user)

    
    return render_template('party.html', title='Account', 
                           image_file=image_file, posts=posts, users=users)


#def home():
 #   page = request.args.get('page', 1, type=int)
  #  posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

   # processed_posts = []
    #for post in posts.items:
     #   if post.picture_data:  # Check if the post has picture data
      #      picture_data = post.picture_data
       #     image = decode_base64_image(picture_data)
        #else:
         #   image = None  # If no picture data, set image to None
        #processed_posts.append((post, image))

    #return render_template('home.html', posts=processed_posts)