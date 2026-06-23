import subprocess

def run(cmd):
    return subprocess.getoutput(cmd)

def get_pods():
    return run("kubectl get pods")

def describe_pod():
    return run("kubectl describe pods")

def get_logs():
    return run("kubectl logs deployment/kubeguard-deployment")