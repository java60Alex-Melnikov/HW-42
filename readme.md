
1. Create SNS Topic “calculator_topic” publishing JSON with format:
a. {“op1”: <float value>, “op2”: <float value>, “operation”: <operation, like “+”,
“-”, “*”, “/”

2.Write lambda function that gets event from SNS topic described in #1 (learn format
of SNS event)
a. Computes a specified operation with two specified operands
b. In the case wrong JSON prints relevant message containing error explanation, like “Missing operand1”, “Missing operand2”, “Operand must be a number”, “Wrong operation”
c. Prints result in the case of a correct JSON

3. Send the link to GitHub repository containing the code of the lambda function