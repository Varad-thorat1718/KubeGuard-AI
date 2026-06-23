def analyze_prompt(pods_output):
    if "CrashLoopBackOff" in pods_output:
        return """
Problem: Application is crashing repeatedly.
Root Cause: Container starts but fails during execution.
Fix: Check application logs and missing dependencies.
"""

    elif "ImagePullBackOff" in pods_output or "ErrImageNeverPull" in pods_output:
        return """
Problem: Kubernetes cannot pull Docker image.
Root Cause: Image not available in Minikube or wrong image name.
Fix: Run 'minikube image load <image>' or fix image tag in deployment.
"""

    elif "Running" in pods_output:
        return """
System Status: Healthy
No critical issues detected in Kubernetes cluster.
"""

    else:
        return """
Problem: Unknown issue detected.
Fix: Run 'kubectl describe pods' for more details.
"""