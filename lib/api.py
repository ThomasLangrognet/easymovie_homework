from lib.classes import User, Workflow, Project
from lib.database import Database

class API:

    def __init__(self):
        self.database_connection = Database()
    
    def create_user(self, user_name):
        new_user = User(user_name)
        self.database_connection.store_user(new_user)
    
    def create_workflow(self, user_name, workflow_name, process):
        user = self.database_connection.get_user(user_name)
        workflow = user.create_workflow(workflow_name, process)
        self.database_connection.update_user(user)
        self.database_connection.store_workflow(workflow)
    
    def create_project(self, user_name, project_name, workflow_name):
        user = self.database_connection.get_user(user_name)
        workflow = self.database_connection.get_workflow(workflow_name)
        project = user.create_project(project_name, workflow)
        self.database_connection.update_user(user)
        self.database_connection.store_project(project)
    
    def update_workflow_process(self, user_name, workflow_name, step_idx, step_name):
        user = self.database_connection.get_user(user_name)
        workflow = self.database_connection.get_workflow(workflow_name)
        workflow.change_process(user, step_idx, step_name)
        self.database_connection.update_workflow(workflow)
    
    def update_project_process_step(self, user_name, project_name, step_idx):
        user = self.database_connection.get_user(user_name)
        project = self.database_connection.get_project(project_name)
        project.change_process_step(user, step_idx)
        self.database_connection.update_project(project)
    
    def subscribe_user_to_workflow(self, user_name, workflow_name, right):
        user = self.database_connection.get_user(user_name)
        workflow = self.database_connection.get_workflow(workflow_name)
        workflow.add_subscriber(user, right)
        user.subscribe_workflow(workflow_name)
        self.database_connection.update_user(user)
        self.database_connection.update_workflow(workflow)
    
    def subscribe_user_to_project(self, user_name, project_name, right):
        user = self.database_connection.get_user(user_name)
        project = self.database_connection.get_project(project_name)
        project.add_subscriber(user, right)
        user.subscribe_project(project_name)
        self.database_connection.update_user(user)
        self.database_connection.update_project(project)
    
    def display_workflow(self, workflow_name):
        workflow = self.database_connection.get_workflow(workflow_name)
        workflow.to_string()

