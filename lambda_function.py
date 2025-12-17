import json

def lambda_handler(event, context):
    try:
        records = event.get('Records', [])
        if not records:
             print("Error: No records found in event")
             return
             
        sns_message_str = records[0]['Sns']['Message']
        
        try:
            message = json.loads(sns_message_str)
        except json.JSONDecodeError:
             print("Error: Invalid JSON format in SNS message")
             return

        if 'op1' not in message:
            print("Error: Missing operand1")
            return
        if 'op2' not in message:
             print("Error: Missing operand2")
             return
        if 'operation' not in message:
             print("Error: Wrong operation")
             return

        op1 = message['op1']
        op2 = message['op2']
        operation = message['operation']

        if not isinstance(op1, (int, float)) or not isinstance(op2, (int, float)):
             print("Error: Operand must be a number")
             return

        result = None
        if operation == '+':
            result = op1 + op2
        elif operation == '-':
            result = op1 - op2
        elif operation == '*':
            result = op1 * op2
        elif operation == '/':
            if op2 == 0:
                print("Error: Division by zero")
                return
            result = op1 / op2
        else:
            print("Error: Wrong operation")
            return

        print(f"Result: {result}")
        return result

    except Exception as e:
        print(f"Unexpected error: {str(e)}")