# Backtracking Search for Doctor Shift Scheduling Problem

SHIFTS = {1: "Morning", 2: "Afternoon", 3: "Night"}


def is_valid(assignment):
    """Checks whether the current partial or complete assignment satisfies all constraints."""
    d1 = assignment.get("D1")
    d2 = assignment.get("D2")
    d3 = assignment.get("D3")

    # Constraint i: D1 cannot work Night shift
    if d1 == 3:
        return False

    # Constraint iv: D3 cannot work Morning shift
    if d3 == 1:
        return False

    # Constraint ii: D2 must work before D3 (Morning < Afternoon < Night)
    if d2 is not None and d3 is not None:
        if not (d2 < d3):
            return False

    # Constraint iii & v: All assigned shifts must be unique (Only one doctor per shift)
    assigned_values = [v for v in assignment.values() if v is not None]
    if len(assigned_values) != len(set(assigned_values)):
        return False

    return True


def backtrack(assignment, variables, domains, step_counter):
    # Base Case: All variables are assigned
    if len(assignment) == len(variables):
        print(f"\n[GOAL REACHED] Valid Assignment Found: {assignment}")
        return assignment

    # Select unassigned variable
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for val in domains:
        step_counter[0] += 1
        print(f"Step {step_counter[0]}: Trying {var} = {SHIFTS[val]} ({val})")

        assignment[var] = val

        if is_valid(assignment):
            print(f"  -> Valid partial assignment: {assignment}")
            result = backtrack(assignment, variables, domains, step_counter)
            if result is not None:
                return result
        else:
            print(f"  -> [PRUNED / BACKTRACK] Constraint violation at {assignment}")

        # Undo assignment (Backtrack)
        del assignment[var]

    return None


if __name__ == "__main__":
    variables = ["D1", "D2", "D3"]
    domains = [1, 2, 3]  # 1: Morning, 2: Afternoon, 3: Night

    print("--- Starting Backtracking Search ---\n")
    step_counter = [0]
    solution = backtrack({}, variables, domains, step_counter)

    print("\n" + "=" * 35)
    print("       FINAL VALID SCHEDULE       ")
    print("=" * 35)
    if solution:
        for doc, shift in solution.items():
            print(f"  {doc} -> {SHIFTS[shift]}")
    else:
        print("No solution found.")
    print("=" * 35)