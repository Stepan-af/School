from string import ascii_lowercase, digits
for x in ascii_lowercase[:12] + digits:
    f = int(f"7418{x}{x}461", 22) + int(f"719625{x}4", 22) + int(f"396{x}99", 22)
    if f % 21 == 0:
        print(f // 21)
        break