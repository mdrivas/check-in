import os # move to users route? 
import secrets # where is this used? 
from PIL import Image
from flask import current_app

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext 
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    # image resizing 
    output_size = (125, 125) 
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # Save picture
    i.save(picture_path)

    return picture_fn

# Add send and resend email routes 
# reset password, reset password token

def save_post_image(image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image.filename)
    image_filename = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static/profile_pics', image_filename)
    
    i = Image.open(image)
    i.save(image_path)

    return image_filename
    