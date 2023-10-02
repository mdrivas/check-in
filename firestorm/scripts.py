class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, taskname, status):
        task = {'taskname': taskname, 'status': status}
        self.tasks.append(task)

    def update_task_status(self, taskname, new_status):
        for task in self.tasks:
            if task['taskname'] == taskname:
                task['status'] = new_status
                break

    def get_tasks(self):
        return self.tasks

# Create a new User
user = User('Alex')

# Add tasks to the User
user.add_task('Gym', 'OFF')
user.add_task('Reading', 'OFF')
user.add_task('Cooking', 'ON')

# Update task status
user.update_task_status('Gym', 'ON')

# Get the list of tasks for the User
tasks = user.get_tasks()
for task in tasks:
    print(f"Task: {task['taskname']} - Status: {task['status']}")

# FROM DATABASE.PY [REMOVED]

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, taskname, status):
        task = {'taskname': taskname, 'status': status}
        self.tasks.append(task)

    def update_task_status(self, taskname, new_status):
        for task in self.tasks:
            if task['taskname'] == taskname:
                task['status'] = new_status
                break

    def get_tasks(self):
        return self.tasks

# Initialize users and tasks for demonstration
user1 = User('Alex')
user1.add_task('Gym', 'ON')
user1.add_task('Reading', 'OFF')
user1.add_task('Cooking', 'ON')

user2 = User('Matt')
user2.add_task('Gym', 'ON')
user2.add_task('Reading', 'OFF')
user2.add_task('Cooking', 'OFF')

user3 = User('Theo')
user3.add_task('Gym', 'ON')
user3.add_task('Reading', 'OFF')
user3.add_task('Cooking', 'OFF')

users = {user1.username: user1}
#users = {user1.username: user1, user2.username: user2, user3.username: user3}

@app.route('/')
def home():
    return render_template('index.html', users=users)

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    username = data['username']
    taskname = data['taskname']
    new_status = data['status']

    if username in users:
        users[username].update_task_status(taskname, new_status)

    return jsonify(success=True)

def update_status():
    data = request.get_json()
    username = data['username']
    taskname = data['taskname']
    new_status = data['status']

    if username in users and taskname in users[username].get_tasks():
        users[username].update_task_status(taskname, new_status)
        return jsonify(success=True)

    return jsonify(success=False)



