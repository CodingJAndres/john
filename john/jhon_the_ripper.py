import os

def show_menu():
    print("\033[1;32m--- Menú de Comandos de John ---\033[0m")
    print("\033[1;36m1. Ejecutar John con lista de palabras")
    print("2. Ejecutar John con ataque incremental")
    print("3. Ejecutar John con reglas")
    print("4. Mostrar resultados de John")
    print("5. Mostrar configuración actual de John")
    print("6. Ejecutar John con un ataque específico")
    print("7. Salir\033[0m")

def main():
    try:
        while True:
            try:
                show_menu()
                choice = input("Selecciona una opción (1-7): ")

                if choice == '1':
                    hashfile = input("Introduce el nombre del archivo hash: ")
                    wordlist = input("Introduce el nombre del archivo de lista de palabras: ")
                    os.system(f"john --wordlist={wordlist} {hashfile}")
                elif choice == '2':
                    hashfile = input("Introduce el nombre del archivo hash: ")
                    os.system(f"john --incremental {hashfile}")
                elif choice == '3':
                    hashfile = input("Introduce el nombre del archivo hash: ")
                    os.system(f"john --rules {hashfile}")
                elif choice == '4':
                    hashfile = input("Introduce el nombre del archivo hash: ")
                    os.system(f"john --show {hashfile}")
                elif choice == '5':
                    os.system("john --test")
                elif choice == '6':
                    hashfile = input("Introduce el nombre del archivo hash: ")
                    attack_type = input("Selecciona el tipo de ataque (brute/mask/dictionary): ").lower()
                    if attack_type == "brute":
                        os.system(f"john --incremental {hashfile}")
                    elif attack_type == "mask":
                        mask = input("Introduce la máscara de ataque: ")
                        os.system(f"john --mask={mask} {hashfile}")
                    elif attack_type == "dictionary":
                        wordlist = input("Introduce el nombre del archivo de lista de palabras: ")
                        os.system(f"john --wordlist={wordlist} {hashfile}")
                    else:
                        print("Tipo de ataque no válido.")
                elif choice == '7':
                    print("¡Adiós!")
                    break
                else:
                    print("Opción inválida. Por favor, selecciona una opción válida (1-7).")
            except KeyboardInterrupt:
                print("\nPrograma cerrado.")
                break
            except FileNotFoundError:
                print("Error: Archivo no encontrado.")
            except Exception as e:
                print(f"Se produjo un error: {str(e)}")
    except KeyboardInterrupt:
        print("\nPrograma cerrado.")

if __name__ == "__main__":
    main()
