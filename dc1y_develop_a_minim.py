Python
class DevOpsPipeline:
    def __init__(self, name, stages):
        self.name = name
        self.stages = stages

class Stage:
    def __init__(self, name, tools):
        self.name = name
        self.tools = tools

class Tool:
    def __init__(self, name, command):
        self.name = name
        self.command = command

class Integrator:
    def __init__(self, pipelines):
        self.pipelines = pipelines

    def integrate(self):
        for pipeline in self.pipelines:
            print(f"Integrating pipeline: {pipeline.name}")
            for stage in pipeline.stages:
                print(f"  Stage: {stage.name}")
                for tool in stage.tools:
                    print(f"    Running tool: {tool.name} - {tool.command}")

# Example usage
pipeline1 = DevOpsPipeline("Pipeline 1", [
    Stage("Build", [Tool("Git", "git pull"), Tool("Maven", "mvn clean package")]),
    Stage("Test", [Tool("JUnit", "java -jar junit.jar")]),
    Stage("Deploy", [Tool("Ansible", "ansible-playbook deploy.yml")])
])

pipeline2 = DevOpsPipeline("Pipeline 2", [
    Stage("Build", [Tool("Git", "git pull"), Tool("Gradle", "gradle build")]),
    Stage("Test", [Tool("PyUnit", "python -m unittest")]),
    Stage("Deploy", [Tool("Kubernetes", "kubectl apply -f deploy.yaml")])
])

integrator = Integrator([pipeline1, pipeline2])
integrator.integrate()