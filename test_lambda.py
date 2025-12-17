import json
from lambda_function import lambda_handler

def run_test(description, message_dict):
    print(f"\nTest: {description}")
    event = {
        'Records': [
            {
                'Sns': {
                    'Message': json.dumps(message_dict) if message_dict else "invalid-json"
                }
            }
        ]
    }
    lambda_handler(event, None)

if __name__ == "__main__":
    # Valid Tests
    run_test("Addition (10 + 5)", {'op1': 10, 'op2': 5, 'operation': '+'})
    run_test("Division (10 / 2)", {'op1': 10, 'op2': 2, 'operation': '/'})

    # Error Tests
    run_test("Missing op1", {'op2': 5, 'operation': '+'})
    run_test("Wrong type", {'op1': "ten", 'op2': 5, 'operation': '+'})
    run_test("Division by Zero", {'op1': 10, 'op2': 0, 'operation': '/'})

