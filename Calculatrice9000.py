def calculator():
    history = []

    while True:
        try:
            num1 = float(input("Entrez le premier nombre: "))
            num2 = float(input("Entrez le deuxième nombre: "))
            operator = input("Entrez l'opérateur (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Erreur: Division par zéro")
                    continue
                result = num1 / num2
            else:
                print("Opérateur invalide")
                continue

            print(f"Résultat: {num1} {operator} {num2} = {result}")
            history.append((num1, operator, num2, result))

            while True:
                show_history = input("Voulez-vous afficher l'historique? (oui/non): ")
                if show_history.lower() == 'oui':
                    print("Historique des opérations:")
                    for entry in history:
                        print(f"{entry[0]} {entry[1]} {entry[2]} = {entry[3]}")
                    break
                elif show_history.lower() == 'non':
                    break
                else:
                    print("Veuillez répondre par 'oui' ou 'non'.")

            while True:
                clear_history = input("Voulez-vous effacer l'historique? (oui/non): ")
                if clear_history.lower() == 'oui':
                    history = []
                    print("Historique effacé.")
                    break
                elif clear_history.lower() == 'non':
                    break
                else:
                    print("Veuillez répondre par 'oui' ou 'non'.")

            continue_calc = input("Voulez-vous continuer? (oui/non): ")
            if continue_calc.lower() == 'non':
                break

        except ValueError:
            print("Veuillez entrer des nombres valides.")
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")


calculator()