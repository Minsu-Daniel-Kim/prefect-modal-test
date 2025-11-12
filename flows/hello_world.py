"""
Hello World Flow for Prefect + Modal integration test.

This is a simple flow to verify that Prefect Cloud can successfully
execute flows on Modal's serverless infrastructure.
"""

from prefect import flow, task


@task(log_prints=True)
def say_hello(name: str) -> str:
    """Print a greeting message."""
    message = f"Hello, {name}! This is running on Modal! 🚀"
    print(message)
    return message


@task(log_prints=True)
def say_goodbye(name: str) -> str:
    """Print a goodbye message."""
    message = f"Goodbye, {name}! Flow completed successfully! ✅"
    print(message)
    return message


@flow(name="hello-world-modal", log_prints=True)
def hello_world_flow(name: str = "World") -> dict:
    """
    A simple Hello World flow to test Prefect + Modal integration.

    Args:
        name: Name to greet (default: "World")

    Returns:
        Dictionary with greeting and goodbye messages
    """
    print(f"Starting Hello World flow for: {name}")

    # Execute tasks
    greeting = say_hello(name)
    goodbye = say_goodbye(name)

    result = {
        "greeting": greeting,
        "goodbye": goodbye,
        "status": "success"
    }

    print(f"Flow result: {result}")
    return result


if __name__ == "__main__":
    # For local testing
    result = hello_world_flow(name="Local Test")
    print(f"\n✅ Local test completed: {result}")
