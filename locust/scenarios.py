from fluent import sender, event
from locust import HttpLocust, TaskSet, task, events

sender.setup('response', host='fluent', port=24224)


class MyTaskSet(TaskSet):

    @task
    def index(self):
        self.client.get("/")


class MyLocust(HttpLocust):
    task_set = MyTaskSet


def on_request_success(request_type, name, response_time, response_length):
    event.Event('success', {
        'request_type': request_type,
        'name': name,
        'response_time': response_time,
        'response_length': response_length,
    })


def on_request_failure(request_type, name, response_time, exception):
    event.Event('failure', {
        'request_type': request_type,
        'name': name,
        'response_time': response_time,
        'exception': repr(exception),
    })


events.request_success += on_request_success
events.request_failure += on_request_failure
