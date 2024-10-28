from locust import HttpUser, TaskSet, task

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

class WebsiteUser(HttpUser):
    host = "http://localhost:5000"
    tasks = [UserBehavior]
    min_wait = 0
    max_wait = 0
    users = 1
    spawn_rate = 1
    run_time = 1  # tiempo de ejecución de la prueba en segundos
