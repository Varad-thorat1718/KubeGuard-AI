from k8s_tools import get_pods, describe_pod, get_logs

print("=== KubeGuard AI v8 (Agentic Loop) ===\n")

state = get_pods()
print("OBSERVATION:\n", state)

print("\n=== THINKING ===\n")

# Agent decision logic (we simulate reasoning loop)
if "ErrImageNeverPull" in state:
    print("Thought: Image issue detected → I should investigate deployment details...\n")

    detail = describe_pod()
    print("ACTION: Running describe pods...\n")
    print(detail)

elif "CrashLoopBackOff" in state:
    print("Thought: Crash detected → I should check logs...\n")

    logs = get_logs()
    print("ACTION: Fetching logs...\n")
    print(logs)

else:
    print("Thought: System seems healthy → no action needed.")