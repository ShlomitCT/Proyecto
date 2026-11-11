#!/usr/bin/env python3
"""
CYBER-TERMINAL HUB (v2.1)
Un panel interactivo para consola escrito en Python puro.
Incluye minijuego de hackeo interactivo en la Opción 5.
"""

import os
import sys
import time
import json
import random
import math
from datetime import datetime

# Colors & Formatting (ANSI Escape Codes)
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

class CyberTerminal:
    DATA_FILE = "hub_data.json"

    def __init__(self):
        self.running = True
        self.data = self._load_data()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        banner = rf"""{Colors.CYAN}{Colors.BOLD}
  ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
 ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
 ╚██████╗   ██║   ██████╔╝███████╗██║  ██║
  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ MATRIX HUB
{Colors.RESET}"""
        print(banner)

    # -------------------------------------------------------------------------
    # PERSISTENCIA DE DATOS
    # -------------------------------------------------------------------------
    def _load_data(self) -> dict:
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {"tasks": []}

    def _save_data(self):
        with open(self.DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=4)

    # -------------------------------------------------------------------------
    # MODULOS DEL SISTEMA
    # -------------------------------------------------------------------------

    def module_juego(self):
        """Mini-juego interactivo: Cyber Hack (Adivina la contraseña de acceso)."""
        self.clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}=== MINIJUEGO: CYBER HACK ==={Colors.RESET}\n")
        print(f"{Colors.YELLOW}Encuentra la contraseña correcta para vulnerar el sistema.{Colors.RESET}")
        print(f"{Colors.DIM}El sistema te dará coincidencias (letras en la misma posición correcta).\n{Colors.RESET}")

        dictionary = [
            "SECURITY", "TERMINAL", "OVERRIDE", "FIREWALL", 
            "HARDWARE", "PROTOCOL", "DATABASE", "ENCRYPTS", 
            "SOFTWARE", "PASSWORD", "NETWORKS", "ABSOLUTE"
        ]
        
        candidates = random.sample(dictionary, 6)
        secret = random.choice(candidates)
        attempts = 4

        print(f"{Colors.BOLD}Bloques de memoria detectados:{Colors.RESET}")
        for w in candidates:
            print(f"  > {Colors.CYAN}{w}{Colors.RESET}")
        print()

        while attempts > 0:
            print(f"Intentos de acceso restantes: {Colors.RED}{'█ ' * attempts}{Colors.RESET}")
            guess = input(f"{Colors.BOLD}Ingresa la clave > {Colors.RESET}").strip().upper()

            if guess not in candidates:
                print(f"{Colors.YELLOW}⚠ Palabra no válida en la memoria. Elige de la lista.{Colors.RESET}\n")
                continue

            if guess == secret:
                print(f"\n{Colors.GREEN}{Colors.BOLD}🔓 ¡ACCESO CONCEDIDO! Sistema hackeado con éxito. 🎉{Colors.RESET}")
                break
            else:
                attempts -= 1
                # Cuenta letras en la posición exactas
                matches = sum(1 for a, b in zip(guess, secret) if a == b)
                print(f"{Colors.RED}❌ Acceso denegado.{Colors.RESET} Coincidencias de posición: {Colors.CYAN}{matches}/{len(secret)}{Colors.RESET}\n")

        if attempts == 0:
            print(f"{Colors.RED}{Colors.BOLD}💥 ¡SISTEMA BLOQUEADO! La contraseña era: {secret}{Colors.RESET}")

        input(f"\n{Colors.DIM}Presiona Enter para volver al menú...{Colors.RESET}")

    def module_matrix_rain(self):
        """Efecto Matrix Rain en terminal."""
        self.clear_screen()
        print(f"{Colors.GREEN}Presiona Ctrl+C para salir del efecto Matrix...{Colors.RESET}\n")
        time.sleep(1)
        
        symbols = "011010101010010101⚡⚔️👾🌐💻🚀#$@%&*<=>"
        width = 80
        columns = [0] * width
        
        try:
            while True:
                line = ""
                for i in range(width):
                    if random.random() > 0.95:
                        columns[i] = random.randint(5, 15)
                    
                    if columns[i] > 0:
                        char = random.choice(symbols)
                        line += f"{Colors.GREEN}{char}{Colors.RESET}"
                        columns[i] -= 1
                    else:
                        line += " "
                print(line)
                time.sleep(0.04)
        except KeyboardInterrupt:
            pass

    def module_pomodoro_timer(self):
        """Temporizador Pomodoro configurable."""
        self.clear_screen()
        print(f"{Colors.YELLOW}{Colors.BOLD}=== MODULO POMODORO ==={Colors.RESET}\n")
        try:
            minutes = int(input(f"{Colors.CYAN}Duración del bloque (minutos) [25]: {Colors.RESET}") or 25)
        except ValueError:
            minutes = 25

        total_seconds = minutes * 60
        start_time = time.time()

        print(f"\n{Colors.GREEN}¡Timer iniciado por {minutes} minutos! Presiona Ctrl+C para interrumpir.{Colors.RESET}\n")

        try:
            while time.time() - start_time < total_seconds:
                elapsed = int(time.time() - start_time)
                remaining = total_seconds - elapsed
                
                mins, secs = divmod(remaining, 60)
                progress = elapsed / total_seconds
                bar_length = 30
                filled = int(bar_length * progress)
                bar = "█" * filled + "░" * (bar_length - filled)

                sys.stdout.write(f"\r{Colors.CYAN}[{bar}] {mins:02d}:{secs:02d} | Total: {minutes}m{Colors.RESET}")
                sys.stdout.flush()
                time.sleep(1)

            print(f"\n\n{Colors.GREEN}{Colors.BOLD}🎉 ¡Tiempo terminado! Excelente trabajo.{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Temporizador cancelado.{Colors.RESET}")
        
        input("\nPresiona Enter para continuar...")

    def module_task_manager(self):
        """Gestor de tareas rápido."""
        while True:
            self.clear_screen()
            print(f"{Colors.MAGENTA}{Colors.BOLD}=== GESTOR DE TAREAS ==={Colors.RESET}\n")
            
            tasks = self.data.get("tasks", [])
            if not tasks:
                print(f"{Colors.DIM}(No hay tareas guardadas){Colors.RESET}\n")
            else:
                for idx, t in enumerate(tasks, start=1):
                    status = f"{Colors.GREEN}[✓]{Colors.RESET}" if t["done"] else f"{Colors.RED}[ ]{Colors.RESET}"
                    print(f"{idx}. {status} {t['title']}")
                print()

            print(f"{Colors.CYAN}[A]ñadir  |  [C]ompletar  |  [E]liminar  |  [V]olver{Colors.RESET}")
            choice = input(f"{Colors.BOLD}> {Colors.RESET}").strip().lower()

            if choice == 'a':
                title = input("Nombre de la tarea: ").strip()
                if title:
                    tasks.append({"title": title, "done": False})
                    self._save_data()
            elif choice == 'c':
                try:
                    num = int(input("Número de tarea: ")) - 1
                    if 0 <= num < len(tasks):
                        tasks[num]["done"] = not tasks[num]["done"]
                        self._save_data()
                except ValueError:
                    pass
            elif choice == 'e':
                try:
                    num = int(input("Número de tarea a eliminar: ")) - 1
                    if 0 <= num < len(tasks):
                        tasks.pop(num)
                        self._save_data()
                except ValueError:
                    pass
            elif choice == 'v':
                break

    def module_system_scanner(self):
        """Diagnóstico de sistema."""
        self.clear_screen()
        print(f"{Colors.CYAN}{Colors.BOLD}=== DIAGNÓSTICO DE SISTEMA ==={Colors.RESET}\n")
        
        steps = [
            "Inicializando adaptadores de red...",
            "Analizando latencia a servidores locales...",
            "Verificando integridad del kernel...",
            "Optimizando espacio de memoria RAM..."
        ]

        for step in steps:
            sys.stdout.write(f"{Colors.YELLOW}[...] {step}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(random.uniform(0.3, 0.6))
            sys.stdout.write(f"\r{Colors.GREEN}[OK]  {step}{Colors.RESET}\n")
            sys.stdout.flush()

        print(f"\n{Colors.GREEN}{Colors.BOLD}✔ Diagnóstico completado.{Colors.RESET}")
        input("\nPresiona Enter para continuar...")

    # -------------------------------------------------------------------------
    # MENU PRINCIPAL & LOOP
    # -------------------------------------------------------------------------

    def run(self):
        options = {
            "1": ("Gestor de Tareas", self.module_task_manager),
            "2": ("Temporizador Pomodoro", self.module_pomodoro_timer),
            "3": ("Diagnóstico de Sistema", self.module_system_scanner),
            "4": ("Efecto Matrix Rain", self.module_matrix_rain),
            "5": ("Juego: Cyber Hack", self.module_juego),
            "6": ("Salir", None)
        }

        while self.running:
            self.clear_screen()
            self.print_banner()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{Colors.DIM}Fecha y hora: {now} | Modo: Developer{Colors.RESET}\n")
            
            for key, (label, _) in options.items():
                print(f"  {Colors.CYAN}{Colors.BOLD}[{key}]{Colors.RESET} {label}")
            print()

            cmd = input(f"{Colors.BOLD}Selecciona una opción (1-6): {Colors.RESET}").strip()

            if cmd in options:
                if cmd == "6":
                    self.clear_screen()
                    print(f"{Colors.CYAN}¡Hasta luego!{Colors.RESET}\n")
                    self.running = False
                else:
                    options[cmd][1]()
            else:
                print(f"{Colors.RED}Opción no válida.{Colors.RESET}")
                time.sleep(0.5)

if __name__ == "__main__":
    app = CyberTerminal()
    app.run()