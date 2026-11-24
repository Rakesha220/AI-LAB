
import re

# Variables used in this program
VARIABLES = {'x', 'y', 'z', 'u', 'v', 'w'}

# Step 1: Parse expressions
def parse(expression):

    tokens = re.findall(r'[A-Za-z][A-Za-z0-9_]*|[(),]', expression)
    pos = 0

    def term():
        nonlocal pos

        if pos >= len(tokens):
            raise ValueError("Invalid expression")

        name = tokens[pos]
        pos += 1

        if pos < len(tokens) and tokens[pos] == '(':

            pos += 1
            args = []

            while True:
                args.append(term())

                if pos < len(tokens) and tokens[pos] == ',':
                    pos += 1
                    continue

                if pos < len(tokens) and tokens[pos] == ')':
                    pos += 1
                    break

                raise ValueError("Invalid expression")

            return (name, args)

        return name

    result = term()

    if pos != len(tokens):
        raise ValueError("Invalid expression")

    return result


# Step 2: Check whether a term is a variable
def is_variable(term):
    return isinstance(term, str) and term in VARIABLES


# Step 3: Apply substitutions
def apply_substitution(term, theta):

    if is_variable(term) and term in theta:
        return apply_substitution(theta[term], theta)

    if isinstance(term, tuple):
        name, args = term

        return (
            name,
            [apply_substitution(a, theta) for a in args]
        )

    return term


# Step 4: Occurs check
def occurs(variable, term, theta):

    term = apply_substitution(term, theta)

    if variable == term:
        return True

    if isinstance(term, tuple):

        return any(
            occurs(variable, arg, theta)
            for arg in term[1]
        )

    return False


# Step 5: Unification algorithm
def unify(expression1, expression2):

    theta = {}

    equations = [(expression1, expression2)]

    while equations:

        s, t = equations.pop(0)

        s = apply_substitution(s, theta)
        t = apply_substitution(t, theta)

        if s == t:
            continue

        # If s is a variable
        if is_variable(s):

            if occurs(s, t, theta):
                return None

            theta[s] = t

        # If t is a variable
        elif is_variable(t):

            if occurs(t, s, theta):
                return None

            theta[t] = s

        # If both are compound terms
        elif isinstance(s, tuple) and isinstance(t, tuple):

            name1, args1 = s
            name2, args2 = t

            if name1 != name2 or len(args1) != len(args2):
                return None

            equations.extend(zip(args1, args2))

        else:
            return None

    # Normalize substitutions
    for variable in theta:
        theta[variable] = apply_substitution(
            theta[variable], theta
        )

    return theta


# Step 6: Display terms
def display(term):

    if isinstance(term, tuple):

        name, args = term

        return name + "(" + ", ".join(
            display(a) for a in args
        ) + ")"

    return str(term)


# Step 7: Main program
print("FIRST ORDER LOGIC - UNIFICATION")

exp1 = input("Enter Expression 1: ")
exp2 = input("Enter Expression 2: ")

try:

    term1 = parse(exp1)
    term2 = parse(exp2)

    result = unify(term1, term2)

    if result is None:

        print("\nFAILURE")
        print("Unification is not possible.")

    else:

        print("\nMGU:")

        if result:
            substitutions = []

            for variable, value in result.items():
                substitutions.append(
                    variable + " / " + display(value)
                )

            print("{ " + ", ".join(substitutions) + " }")

        else:
            print("{}")

        print("Result: Unification successful.")

except ValueError as e:
    print("Invalid expression:", e)
