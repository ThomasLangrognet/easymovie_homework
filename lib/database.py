class Database:

    WORKFLOW_DATABASE = []
    PROJECT_DATABASE = []
    USER_DATABASE = []

    def check_user_name(self, user_name):
        for user in Database.USER_DATABASE:
            if user.get_name() == user_name:
                raise Exception("User name {} already taken!".format(user_name))
    
    def check_project_name(self, project_name):
        for project in Database.PROJECT_DATABASE:
            if project.get_name() == project_name:
                raise Exception("Project name {} already taken!".format(project_name))
    
    def check_workflow_name(self, workflow_name):
        for workflow in Database.WORKFLOW_DATABASE:
            if workflow.get_name() == workflow_name:
                raise Exception("Workflow name {} already taken!".format(workflow_name))

    def store_user(self, user):
        self.check_user_name(user.get_name())
        Database.USER_DATABASE.append(user)
    
    def store_project(self, project):
        self.check_project_name(project.get_name())
        Database.PROJECT_DATABASE.append(project)
    
    def store_workflow(self, workflow):
        self.check_workflow_name(workflow.get_name())
        Database.WORKFLOW_DATABASE.append(workflow)
    
    def get_user(self, user_name):
        for user in Database.USER_DATABASE:
            if user.get_name() == user_name:
                return user
        raise Exception("User {} does not exist!".format(user_name))

    def get_project(self, project_name):
        for project in Database.PROJECT_DATABASE:
            if project.get_name() == project_name:
                return project
        raise Exception("Project {} does not exist!".format(project_name))

    def get_workflow(self, workflow_name):
        for workflow in Database.WORKFLOW_DATABASE:
            if workflow.get_name() == workflow_name:
                return workflow
        raise Exception("Workflow {} does not exist!".format(workflow_name))

    def update_user(self, user_up):
        user_name = user_up.get_name()
        user = self.get_user(user_name)
        self.USER_DATABASE.remove(user)
        self.USER_DATABASE.append(user_up)  

    def update_workflow(self, workflow_up):
        workflow_name = workflow_up.get_name()
        workflow = self.get_workflow(workflow_name)
        self.WORKFLOW_DATABASE.remove(workflow)
        self.WORKFLOW_DATABASE.append(workflow_up)  
    
    def update_project(self, project_up):
        project_name = project_up.get_name()
        project = self.get_project(project_name)
        self.PROJECT_DATABASE.remove(project)
        self.PROJECT_DATABASE.append(project_up)

        
    

