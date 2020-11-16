from lib.api import API

api = API()

api.create_user("Thomas")
api.create_user("Vincent")

api.create_workflow("Thomas", "workflow_1", ["step_1", "step_2", "step_3"])
api.create_project("Thomas", "project_1", "workflow_1")

api.create_workflow("Vincent", "workflow_2", ["step_1", "step_2"])
api.create_project("Vincent", "project_2", "workflow_2")

api.display_workflow("workflow_2")

api.subscribe_user_to_workflow("Thomas", "workflow_2", "w")
api.update_workflow_process("Thomas", "workflow_2", 2, "new_step_2")

api.display_workflow("workflow_2")
