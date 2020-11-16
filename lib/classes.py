class Entity:

    def __init__(self, name, creator):
        self.__name = name
        self.__subscribers = [Subscriber(creator.get_name(), "o")]
    
    def get_subscriber_right(self, user):
        for subscriber in self.__subscribers:
            if subscriber.get_user_name() == user.get_name():
                return subscriber.get_right()

    def add_subscriber(self, user, right):
        self.__subscribers.append(Subscriber(user.get_name(), right))
    
    def change_right_subscriber(self, user, new_right):
        for subscriber in self.__subscribers:
            if subscriber.get_user_name() == user.get_name():
                subscriber.change_right(new_right)
                break
    
    def get_name(self):
        return self.__name
    
    def get_subscribers(self):
        return self.__subscribers

class Workflow(Entity):

    def __init__(self, name, creator, process):
        super().__init__(name, creator)
        self.__process = process
    
    def add_subscriber(self, user, right):
        super().add_subscriber(user, right)
    
    def change_right_subscriber(self, user, new_right):
        super().change_right_subscriber(user, new_right)
    
    def get_name(self):
        return super().get_name()
    
    def change_process(self, user, step_idx, step_name):
        user_right = super().get_subscriber_right(user)
        if user_right == "r":
            raise Exception("User {} can only read workflow {}!".format(user.get_name(), self.get_name()))
        self.__process[step_idx-1] = step_name
    
    def to_string(self):
        print("Workflow name is {}.".format(self.get_name()))
        print("Workflow process is {}.".format(self.__process))
        subscribers = super().get_subscribers()
        subs_to_string = []
        for subs in subscribers:
            subs_to_string.append(subs.get_user_name())
        print("Workflow subscribers are {}.".format(subs_to_string))

class Project(Entity):

    def __init__(self, name, creator, workflow):
        super().__init__(name, creator)
        self.__workflow = workflow
        self.__workflow_process_status = 0
    
    def add_subscriber(self, user, right):
        super().add_subscriber(user, right)
    
    def change_right_subscriber(self, user, right):
        super().change_right_subscriber(user, right)
    
    def get_name(self):
        return super().get_name()
    
    def change_process_step(self, user, step_idx):
        user_right = super().get_subscriber_right(user)
        if user_right == "r":
            raise Exception("User {} can only read project {}!".format(user.get_name(), self.get_name()))
        self.__workflow_process_status = step_idx

class Subscriber:

    RIGHTS = ["o", "r", "w"]

    def __init__(self, user_name, right):
        self.__user_name = user_name
        if right not in Subscriber.RIGHTS:
            raise Exception("Right {} does not exist!".format(right))
        self.__right = right
    
    def change_right(self, new_right):
        if right not in Subscriber.RIGHTS:
            raise Exception("Right {} does not exist!".format(right))
        self.__right = new_right
    
    def get_user_name(self):
        return self.__user_name
    
    def get_right(self):
        return self.__right

class User:

    def __init__(self, name):
        self.__name = name
        self.__workflows_subscribed = []
        self.__projects_subscribed = []
    
    def get_name(self):
        return self.__name
    
    def create_workflow(self, workflow_name, process):
        self.__workflows_subscribed.append(workflow_name)
        return Workflow(workflow_name, self, process)
    
    def create_project(self, project_name, workflow):
        self.__projects_subscribed.append(project_name)
        return Project(project_name, self, workflow)
    
    def subscribe_workflow(self, workflow_name):
        self.__workflows_subscribed.append(workflow_name)
    
    def subscribe_project(self, project_name):
        self.__projects_subscribed.append(project_name)




