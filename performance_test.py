from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust starts """
        self.login()

    def login(self):
        # No es necesario iniciar sesión en esta aplicación
        pass

    @task
    def index(self):
        self.client.get("/")

    @task
    def people(self):
        self.client.get("/people")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000
