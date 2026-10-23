import os
import threading

applications = [
    "order-service",
    "orchestrator-service",
    "product-validation-service",
    "payment-service",
    "inventory-service"
]

build_results = {}

def build_application(app):
    print("Building application {}".format(app))

    result = os.system("cd {} && mvnw.cmd clean package \"-Dmaven.test.skip=true\"".format(app))

    build_results[app] = result == 0

    if result == 0:
        print("Application {} built successfully!".format(app))
    else:
        print("Application {} failed to build!".format(app))

def docker_compose_up():
    print("Running containers!")
    os.system("docker compose up --build -d")
    print("Pipeline finished!")

def build_all_applications():
    print("Starting to build applications!")

    threads = []

    for app in applications:
        thread = threading.Thread(
            target=build_application,
            args=(app,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return all(build_results.values())

def remove_remaining_containers():
    print("Removing project containers.")
    os.system("docker compose down --remove-orphans")

if __name__ == "__main__":
    print("Pipeline started!")

    if build_all_applications():
        remove_remaining_containers()
        docker_compose_up()
    else:
        print("Build failed. Docker Compose will not start.")
