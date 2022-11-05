import re
from itertools import product


def solve_the_task(s):
    while len(s) != 1:
        i = 0
        r = ''
        while i < len(s):
            if s[i] == '!' and s[i + 1] != '(' and s[i + 1] != '!':
                l = -(int(s[i + 1]) - 1)
                r = r + str(l)
                i = i + 1
            else:
                r = r + s[i]
            i = i + 1
        s = r
        i = 0
        while i + 2 < len(s):
            if s[i] != ')' and s[i + 1] == '&' and s[i + 2] != '(':
                l = int(s[i]) * int(s[i + 2])
                left = s[:i]
                if i + 3 >= len(s):
                    right = ""
                else:
                    right = s[i + 3:]
                s = left + str(l) + right
                i = i - 1
            i = i + 1
        i = 0
        while i + 2 < len(s):
            if s[i] != ')' and s[i + 1] == '|' and s[i + 2] != '(':
                l = int(s[i]) + int(s[i + 2]) - (int(s[i]) * int(s[i + 2]))
                left = s[:i]
                if i + 3 >= len(s):
                    right = ""
                else:
                    right = s[i + 3:]
                s = left + str(l) + right
                i = i - 1
            i = i + 1
        i = 0
        while i + 3 < len(s):
            if s[i] != ')' and s[i + 1] == '-' and s[i + 2] == '>' and s[i + 3] != '(':
                if (int(s[i]) == 1 and int(s[i + 3]) == 0):
                    l = 0
                else:
                    l = 1
                left = s[:i]
                if i + 3 >= len(s):
                    right = ""
                else:
                    right = s[i + 4:]
                s = left + str(l) + right
            i = i + 1
        i = 0
        while i + 2 < len(s):
            if s[i] == '(' and s[i + 2] == ')':
                left = s[:i]
                if i + 3 >= len(s):
                    right = ""
                else:
                    right = s[i + 3:]
                s = left + s[i + 1] + right
            i = i + 1
    return int(s)


if __name__ == '__main__':
    s = input()
    s = s.replace(" ", "")
    variables = re.findall(r'[^\!\&\|\(\)\-\>]+', s)
    variables = list(set(variables))
    alphabet = "01"
    comb = list(map("".join, product(*[list(alphabet)] * len(variables))))
    true = 0
    false = 0
    for i in range(len(comb)):
        line = s
        for l in range(len(variables)):
            line = line.replace(variables[l], comb[i][l])
        sol = solve_the_task(line)
        if sol == 1:
            true = true + 1
        else:
            false = false + 1
    if false == 2 ** len(variables):
        print("Unsatisfiable")
    elif true == 2 ** len(variables):
        print("Valid")
    else:
        print("Satisfiable and invalid, " + str(true) + " true and " + str(false) + " false cases")
