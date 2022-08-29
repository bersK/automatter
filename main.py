from program import Program

def main():
    program = Program("json/sc.json")
    scenarios = program.getScenarios()

    if False: # print the scenario scripts with their arguments
        for scenario, _ in scenarios.items():
            print()
            print(f"Scenario: {scenario}")
            for script in scenarios[scenario]["scripts"]:
                print(script, end=" ")
                for arg in scenarios[scenario]["arguments"][script]:
                    print(arg, end=" ")
                print()
                print(program.getScriptPath(script))

if __name__ == "__main__":
    main()
