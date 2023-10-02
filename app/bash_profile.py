# Add the path to your Flask app to PYTHONPATH export PYTHONPATH="${HOME}/my_flask_app:${PYTHONPATH}"


# Set environment variables for your Flask app
# export FLASK_APP=my_app   #Replace 'my_app' with the actual name of your app
#export FLASK_ENV=development  #Change to 'production' when deploying

# Add virtual environment to PATH (if you're using one)
# Replace 'venv' with the name of your virtual environment
export PATH="${HOME}/my_flask_app/venv/bin:${PATH}"

# Add any other environment variables specific to your app
export SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
export app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Alias to easily activate your virtual environment
alias activate_venv="source ${HOME}/my_flask_app/venv/bin/activate"

# Alias to start your Flask app
alias start_flask="flask run"

# Alias to stop your Flask app (assumes you're running it in the foreground)
alias stop_flask="killall flask"
