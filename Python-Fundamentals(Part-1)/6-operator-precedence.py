#Operator Precedence in Python determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. Here is a list of some common operators in Python, ordered from highest to lowest precedence:
# 1. Parentheses: ()
# 2. Exponentiation: **
# 3. Unary plus and minus: +x, -x
# 4. Multiplication, Division, Floor Division, Modulus: *, /, //
# 5. Addition and Subtraction: +, -
# 6. Comparison Operators: ==, !=, >, <, >=, <=
# 7. Logical NOT: not
# 8. Logical AND: and
# 9. Logical OR: or

# Example to demonstrate operator precedence
result = 3 + 5 * 2 ** 2 - (4 / 2)
# Breakdown of the evaluation:
# Step 1: Exponentiation: 2 ** 2 = 4
# Step 2: Multiplication: 5 * 4 = 20
# Step 3: Division: 4 / 2 = 2.0
# Step 4: Addition and Subtraction from left to right: 3 + 20 - 2.0 = 21.0  