def balance_check(input):
    stack = []

    for char in input:
        if char in ["(", "[", "{"]:
            stack.append(char)

        else:
            if not stack:
                return "Not balanced"
            current = stack.pop()
            if current == "(":
                if char != ")":
                    return "Not balanced"
            if current == "[":
                if char != "]":
                    return "Not balanced"
            if current == "{":
                if char != "}":
                    return "Not balanced"

    if stack:
        return "Not balanced"
    return "Balanced"

print(balance_check("()"))
print(balance_check("())"))
print(balance_check(")("))
print(balance_check("([])"))
print(balance_check("([{}])"))
print(balance_check("([{]})"))
print(balance_check("[(){}[]]()"))

# () balanced
# ()) not balanced
# )( not balanced
# ([]) balanced
# ([{}]) balanced
# ([{]}) not balanced
# [(){}[]]() balanced