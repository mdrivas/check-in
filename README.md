# Set Up Guide

Welcome to the Setup Guide. Follow these steps every time you pull the branch to ensure you have the latest version of the code.

## Step 1: Fetch/Pull the Latest Changes

1. Open GitHub Desktop.
2. Fetch the latest changes from the remote repository.
3. Pull the branch you want to work on and save it to your local machine.

## Step 2: Open the Project in an Editor (e.g., VS Code)

Open your preferred code editor (e.g., VS Code) and load the project.

## Step 3: Create a Virtual Environment

We create a virtual environment to isolate project dependencies and keep the project folder clean.

1. Activate your virtual environment (create one if not already done).
2. In your command prompt or terminal, navigate to the directory containing the `requirements.txt` file.
3. Run the following command to install the necessary packages into your virtual environment:

   ```
   pip install -r requirements.txt
   ```

This command installs all the packages listed in the `requirements.txt` file into your virtual environment.

## Step 4: Run the Flask App Locally

1. Ensure Flask is installed in your virtual environment. You can check by running:

   ```
   pip list
   ```

   Verify that Flask is listed among the dependencies.

2. In your command prompt or terminal, navigate to the project's root folder.

3. Set the Flask app by running the following command:

   ```
   export FLASK_APP=run.py
   ```

4. Finally, run the app:

   ```
   python run.py
   ```

Now, the app should be running locally. Open your web browser and enter the local host URL to view the application.

## Step 5: Save and Push Your Changes

In GitHub Desktop, review the changes you've made.
Commit your changes with a descriptive message.
Push the changes to the branch you are working on or create a pull request to merge them into the main branch.