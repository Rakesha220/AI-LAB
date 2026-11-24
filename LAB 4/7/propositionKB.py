
from itertools import product
import re

# Evaluate a propositional logic expression
def evaluate(expression, values):

    expression = expression.replace("<->", "==")
    expression = expression.replace("->", "<=")
    expression = expression.replace("&", " and ")
    expression = expression.replace("|", " or ")
    expression = expression.replace("~", " not ")

    for symbol, value in values.items():
        expression = re.sub(
            r'\b' + re.escape(symbol) + r'\b',
            str(value),
            expression
        )

    # Handle implication: A <= B means (not A) or B
    expression = re.sub(
        r'(True|False)\s*<=\s*(True|False)',
        lambda m: str((not eval(m.group(1))) or eval(m.group(2))),
        expression
    )

    return bool(eval(expression))


# Extract propositional symbols
def extract_symbols(kb, query):

    text = " ".join(kb) + " " + query

    text = text.replace("<->", " ")
    text = text.replace("->", " ")
    
    symbols = re.findall(r'\b[A-Z]\w*\b', text)

    operators = {"AND", "OR", "NOT", "TRUE", "FALSE"}

    return sorted(set(
        s for s in symbols if s not in operators
    ))


# Check entailment
def check_entailment(kb, query):

    symbols = extract_symbols(kb, query)

    assignments = product([False, True], repeat=len(symbols))

    found_model = False

    for values in assignments:

        assignment = dict(zip(symbols, values))

        # Check whether entire KB is true
        kb_true = all(
            evaluate(statement, assignment)
            for statement in kb
        )

        if kb_true:

            found_model = True

            query_value = evaluate(query, assignment)

            if not query_value:

                print("\nNOT ENTAILED")
                print("Counterexample:")

                for symbol, value in assignment.items():
                    print(symbol, "=", value)

                return False

    if not found_model:
        print("\nENTAILED (KB has no satisfying assignments)")
    else:
        print("\nENTAILED")

    return True


# Main program
print("PROPOSITIONAL LOGIC ENTAILMENT")

n = int(input("Enter number of KB statements: "))

kb = []

for i in range(n):
    statement = input("Enter KB statement " + str(i + 1) + ": ")
    kb.append(statement)

query = input("Enter query: ")

check_entailment(kb, query)
