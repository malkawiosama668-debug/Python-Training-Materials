'''
Task 2.2: Global Configuration Manager
Objective: Master variable scoping, the LEGB rule, and the global keyword to modify script-level state safely.

You are building a mock deployment script. The system starts in a "Development" state, and a function must safely transition it to "Production".

Where to write your code: Navigate to the task_2_2_config_manager directory and write your solution inside the config_manager.py file.
Requirements:
Define a global variable named system_env and set it to the string "Development".
Define a function named deploy_to_production().
Inside the function, use the global keyword to claim access to system_env and change its value to "Production".
Create a nested function (a function inside deploy_to_production) named log_deployment(). Have it print: "Deploying from Development to Production..." using variables from the Enclosing scope if possible.
Execution: Print the system_env variable, call the deploy_to_production() function, and then print system_env again to prove the global state was permanently changed.
'''

system_env="Development"

def log_deployment():
    print(f"Deploying from Development to Production...")

def deploy_to_production():
    global system_env 
    system_env="Production"
    return log_deployment()

print(system_env)
print(deploy_to_production())
print(system_env)
