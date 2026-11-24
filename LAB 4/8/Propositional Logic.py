
import re
from itertools import product

# Step 1: Tokenize expression
def tokenize(s):
    pattern = r'<->|->|[()~&|]|[A-Za-z][A-Za-z0-9_]*'
    tokens = re.findall(pattern, s)

    if ''.join(tokens).replace('AND', '').replace('OR', '').replace('NOT', '') == '':
        pass

    return tokens


# Step 2: Parse logical expression
def parse(s):
    tokens = tokenize(s)
    pos = 0

    def atom():
        nonlocal pos

        if pos >= len(tokens):
            raise ValueError("Invalid expression")

        t = tokens[pos]

        if t == '~':
            pos += 1
            return ('not', atom())

        if t == '(':
            pos += 1
            result = iff()
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return result

        if t.upper() == 'NOT':
            pos += 1
            return ('not', atom())

        if t.upper() in ('AND', 'OR'):
            raise ValueError("Invalid expression")

        if t in ('&', '|', '->', '<->', ')'):
            raise ValueError("Invalid expression")

        pos += 1
        return ('var', t)

    def conjunction():
        nonlocal pos
        left = atom()

        while pos < len(tokens) and tokens[pos] in ('&', 'AND'):
            pos += 1
            left = ('and', left, atom())

        return left

    def disjunction():
        nonlocal pos
        left = conjunction()

        while pos < len(tokens) and tokens[pos] in ('|', 'OR'):
            pos += 1
            left = ('or', left, conjunction())

        return left

    def implication():
        nonlocal pos
        left = disjunction()

        if pos < len(tokens) and tokens[pos] == '->':
            pos += 1
            return ('imp', left, implication())

        return left

    def iff():
        nonlocal pos
        left = implication()

        while pos < len(tokens) and tokens[pos] == '<->':
            pos += 1
            left = ('iff', left, implication())

        return left

    result = iff()

    if pos != len(tokens):
        raise ValueError("Invalid expression")

    return result


# Step 3: Eliminate implication and biconditional
def eliminate(node):

    op = node[0]

    if op == 'var':
        return node

    if op == 'not':
        return ('not', eliminate(node[1]))

    a = eliminate(node[1])
    b = eliminate(node[2])

    if op == 'imp':
        return ('or', ('not', a), b)

    if op == 'iff':
        return (
            'and',
            ('or', ('not', a), b),
            ('or', ('not', b), a)
        )

    return (op, a, b)


# Step 4: Convert to Negation Normal Form
def nnf(node, neg=False):

    op = node[0]

    if op == 'var':
        return ('not', node) if neg else node

    if op == 'not':
        return nnf(node[1], not neg)

    if op == 'and':
        new_op = 'or' if neg else 'and'
        return (
            new_op,
            nnf(node[1], neg),
            nnf(node[2], neg)
        )

    if op == 'or':
        new_op = 'and' if neg else 'or'
        return (
            new_op,
            nnf(node[1], neg),
            nnf(node[2], neg)
        )


# Step 5: Convert NNF to CNF
# Literal format: (symbol, positive/negative)
def to_cnf(node):

    op = node[0]

    if op == 'var':
        return [frozenset([(node[1], True)])]

    if op == 'not':
        return [frozenset([(node[1][1], False)])]

    left = to_cnf(node[1])
    right = to_cnf(node[2])

    if op == 'and':
        return left + right

    if op == 'or':
        result = []

        for c1 in left:
            for c2 in right:
                result.append(c1 | c2)

        return result


# Step 6: Convert expression into clauses
def convert_cnf(expression):

    tree = parse(expression)
    tree = eliminate(tree)
    tree = nnf(tree)

    clauses = to_cnf(tree)

    # Remove tautological clauses
    return {
        c for c in clauses
        if not any((s, not p) in c for s, p in c)
    }


# Step 7: Apply resolution rule
def resolve(c1, c2):

    results = set()

    for literal in c1:

        symbol, positive = literal
        opposite = (symbol, not positive)

        if opposite in c2:

            new_clause = (c1 - {literal}) | (c2 - {opposite})

            # Remove tautological resolvents
            if not any(
                (s, not p) in new_clause
                for s, p in new_clause
            ):
                results.add(new_clause)

    return results


# Step 8: Resolution algorithm
def resolution(kb, query):

    clauses = set()

    # Convert KB into CNF
    for statement in kb:
        clauses.update(convert_cnf(statement))

    # Negate query and convert into CNF
    negated_query = '~(' + query + ')'
    clauses.update(convert_cnf(negated_query))

    print("\nInitial Clauses:")
    for c in clauses:
        print(c)

    # Apply resolution
    while True:

        new_clauses = set()
        current = list(clauses)

        for i in range(len(current)):
            for j in range(i + 1, len(current)):

                resolvents = resolve(
                    current[i],
                    current[j]
                )

                for r in resolvents:

                    if len(r) == 0:
                        print("\nEmpty Clause Derived!")
                        print("PROVED")
                        return True

                    if r not in clauses:
                        new_clauses.add(r)

        if not new_clauses:
            print("\nNo new clauses generated.")
            print("NOT PROVED")
            return False

        clauses.update(new_clauses)


# Step 9: Main program
print("PROPOSITIONAL LOGIC - RESOLUTION")

n = int(input("Enter number of KB statements: "))

kb = []

for i in range(n):
    statement = input(
        "Enter KB statement " + str(i + 1) + ": "
    )
    kb.append(statement)

query = input("Enter query: ")

resolution(kb, query)
