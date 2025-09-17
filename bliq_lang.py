import sys
import re

variables = {}
functions = {}

def get_value(token):
    """Zahl oder Variablenwert zurückgeben"""
    if token.isdigit():
        return int(token)
    return variables.get(token, 0)

def check_condition(var, op, val):
    left = get_value(var)
    val = get_value(val)
    if op == "equals":
        return left == val
    elif op == "bigger":
        return left > val
    elif op == "smaller":
        return left < val
    else:
        raise ValueError(f"Unknown operator: {op}")

def run(code):
    lines = code.strip().splitlines()
    i = 0
    while i < len(lines):
        parts = lines[i].strip().split()
        if not parts:
            i += 1
            continue

        # Kommentar ignorieren
        if parts[0].startswith("#"):
            i += 1
            continue

        # "end" außerhalb eines Blocks ignorieren
        if parts[0] == "end":
            i += 1
            continue

        cmd = parts[0]

        if cmd == "set":
            name, val = parts[1], get_value(parts[2])
            variables[name] = val

        elif cmd == "add":
            name, val = parts[1], get_value(parts[2])
            variables[name] += val

        elif cmd == "sub":
            name, val = parts[1], get_value(parts[2])
            variables[name] -= val

        elif cmd == "mul":
            name, val = parts[1], get_value(parts[2])
            variables[name] *= val

        elif cmd == "div":
            name, val = parts[1], get_value(parts[2])
            variables[name] //= val

        elif cmd == "print":
            name = parts[1]
            print(variables.get(name, 0))

        elif cmd == "say":
            text = " ".join(parts[1:])
            # Variablen im Text ersetzen, nur !VAR!
            def replace_var(match):
                var_name = match.group(1)
                return str(variables.get(var_name, match.group(0)))
            text = re.sub(r'!(\w+)!', replace_var, text)
            print(text)

        elif cmd == "input":
            var_name = parts[1]
            variables[var_name] = input()

        elif cmd == "repeat":
            count = get_value(parts[1])
            block = []
            i += 1
            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1
            for _ in range(count):
                run("\n".join(block))

        elif cmd == "if":
            branches = []
            else_block = []

            cond_var, cond_op, cond_val = parts[1], parts[2], parts[3]
            current_cond = (cond_var, cond_op, cond_val)
            current_block = []

            i += 1
            while i < len(lines) and lines[i].strip() != "end":
                line = lines[i].strip()
                if line.startswith("else if"):
                    branches.append((current_cond, current_block))
                    tokens = line.split()
                    if len(tokens) < 5:
                        raise SyntaxError(f"Invalid else if: {line}")
                    var, op, val = tokens[2], tokens[3], tokens[4]
                    current_cond = (var, op, val)
                    current_block = []
                elif line == "else":
                    branches.append((current_cond, current_block))
                    current_cond = None
                    current_block = else_block
                else:
                    current_block.append(lines[i])
                i += 1
            if current_cond:
                branches.append((current_cond, current_block))

            executed = False
            for cond, block in branches:
                if check_condition(*cond):
                    run("\n".join(block))
                    executed = True
                    break
            if not executed and else_block:
                run("\n".join(else_block))

        elif cmd == "function":
            func_name = parts[1]
            block = []
            i += 1
            while i < len(lines) and lines[i].strip() != "end":
                block.append(lines[i])
                i += 1
            functions[func_name] = "\n".join(block)

        elif cmd == "call":
            func_name = parts[1]
            if func_name not in functions:
                raise ValueError(f"Function {func_name} not defined")
            run(functions[func_name])

        else:
            raise ValueError(f"Unknown command: {cmd}")

        i += 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python toy_lang.py programm.bliq")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.endswith(".bliq"):
        print("Bitte eine .bliq-Datei angeben")
        sys.exit(1)

    with open(filename, "r") as f:
        code = f.read()

    run(code)
