from prefect import Flow, task

@task
def get_param():
    return "world"

#@task
#def hello(param_):
#    return print(f'{param_}')

with Flow("HelloWorld") as flow:
    param = get_param()
#    hello_world = hello(param)

flow.run()