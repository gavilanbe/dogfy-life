#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗  ██████╗  ██████╗ ███████╗██╗   ██╗    ██╗     ██╗███████╗███████╗ ║
║   ██╔══██╗██╔═══██╗██╔════╝ ██╔════╝╚██╗ ██╔╝    ██║     ██║██╔════╝██╔════╝ ║
║   ██║  ██║██║   ██║██║  ███╗█████╗   ╚████╔╝     ██║     ██║█████╗  █████╗   ║
║   ██║  ██║██║   ██║██║   ██║██╔══╝    ╚██╔╝      ██║     ██║██╔══╝  ██╔══╝   ║
║   ██████╔╝╚██████╔╝╚██████╔╝██║        ██║       ███████╗██║██║     ███████╗ ║
║   ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝        ╚═╝       ╚══════╝╚═╝╚═╝     ╚══════╝ ║
║                                                                              ║
║                  🐕 Simulador Interactivo de Mascota 🐕                       ║
║                      Powered by Dogfy Diet - Barcelona                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import curses
import random
import time
import math
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from enum import Enum
import os

# ══════════════════════════════════════════════════════════════════════════════
# ARTE ASCII DE ALTA CALIDAD - PERRO GOLDEN RETRIEVER
# ══════════════════════════════════════════════════════════════════════════════

DOG_IDLE = [
    "                                                    ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ●       ●    ▀████▄█▀▀█        ",
    "       █  ████                    █████  █        ",
    "       ▀▄▄████       ▄███▄        ████▄▄▀         ",
    "          █████     ▀█████▀      █████            ",
    "          ██████▄     ▀▀▀      ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      ██████████▀▀▀████████▀▀▀█████████           ",
    "      █████████     ██████     ████████           ",
    "      █████████     ██████     ████████           ",
    "       ▀▀▀▀▀▀▀       ▀▀▀▀       ▀▀▀▀▀▀            ",
]

DOG_HAPPY = [
    "                     ★  ♥  ★                       ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ◕       ◕    ▀████▄█▀▀█        ",
    "       █  ████        ▄▄▄        █████  █         ",
    "       ▀▄▄████      ▀█████▀      ████▄▄▀          ",
    "          █████       ▀▀▀        █████   ♪        ",
    "          ██████▄              ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      ██████████▀▀▀████████▀▀▀█████████           ",
    "      █████████     ██████     ████████           ",
    "      █████████     ██████     ████████           ",
    "       ▀▀▀▀▀▀▀       ▀▀▀▀       ▀▀▀▀▀▀            ",
]

DOG_EATING = [
    "                                                    ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ◠       ◠    ▀████▄█▀▀█        ",
    "       █  ████         ▄         █████  █         ",
    "       ▀▄▄████      ███████      ████▄▄▀          ",
    "          █████    █████████    █████   ñam       ",
    "          ██████▄   ▀█████▀   ▄██████    ñam      ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      ██████████▀▀▀████████▀▀▀█████████           ",
    "      █████████     ██████     ████████           ",
    "      █████████     ██████     ████████           ",
    "       ▀▀▀▀▀▀▀       ▀▀▀▀       ▀▀▀▀▀▀            ",
]

DOG_SLEEPING = [
    "                         z z z                     ",
    "                        ▄▄▄▄▄▄    Z Z              ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   —       —    ▀████▄█▀▀█        ",
    "       █  ████                    █████  █        ",
    "       ▀▄▄████       ▄▄▄▄▄        ████▄▄▀         ",
    "          █████                  █████            ",
    "          ██████▄              ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        ████████████████████████████████████      ",
    "      ████████████████████████████████████████    ",
    "    █████████████████████████████████████████████ ",
    "   ██████████████████████████████████████████████ ",
    "   ██████████████████████████████████████████████ ",
    "   ██████████████████████████████████████████████ ",
    "    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ",
    "                                                   ",
    "                                                   ",
]

DOG_SAD = [
    "                                                    ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ◔       ◔    ▀████▄█▀▀█        ",
    "       █  ████         ▄         █████  █         ",
    "       ▀▄▄████      ▄█████▄      ████▄▄▀          ",
    "          █████    █▀▀▀▀▀▀▀█    █████             ",
    "          ██████▄              ▄██████    💧      ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      ██████████▀▀▀████████▀▀▀█████████           ",
    "      █████████     ██████     ████████           ",
    "      █████████     ██████     ████████           ",
    "       ▀▀▀▀▀▀▀       ▀▀▀▀       ▀▀▀▀▀▀            ",
]

DOG_PLAYING = [
    "                                                    ",
    "                        ▄▄▄▄▄▄        ★            ",
    "                   ▄▄█████████████▄    ●           ",
    "                ▄███████████████████▄  ★           ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ◕       ◕    ▀████▄█▀▀█        ",
    "       █  ████        ▄▄▄        █████  █         ",
    "       ▀▄▄████      ▀█████▀      ████▄▄▀          ",
    "          █████       ▀▀▀        █████            ",
    "          ██████▄              ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "   ●  ███████████████████████████████████         ",
    "  ★  █████████████████████████████████████        ",
    "    ████████████████████████████████████████      ",
    "      █████████████████████████████████           ",
    "      ██████████▀▀▀████████▀▀▀█████████           ",
    "      █████████     ██████     ████████           ",
    "        ▀▀█████▀▀▀▀▀██████▀▀▀▀▀█████▀▀            ",
    "                                                   ",
]

DOG_WALK_1 = [
    "                                                    ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ●       ●    ▀████▄█▀▀█        ",
    "       █  ████                    █████  █        ",
    "       ▀▄▄████       ▄███▄        ████▄▄▀         ",
    "          █████     ▀█████▀      █████            ",
    "          ██████▄     ▀▀▀      ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████▀▀▀▀████████▀▀▀▀████████           ",
    "      ████████       ████        ██████           ",
    "      ████████      ██████      ███████           ",
    "       ▀▀▀▀▀▀        ▀▀▀▀        ▀▀▀▀▀            ",
]

DOG_WALK_2 = [
    "                                                    ",
    "                        ▄▄▄▄▄▄                      ",
    "                   ▄▄█████████████▄                 ",
    "                ▄███████████████████▄               ",
    "              ▄██████▀▀▀▀▀▀▀▀████████▄             ",
    "        ▄▄   ████▀▀           ▀▀██████   ▄▄        ",
    "       █▀▀█▄███▀   ●       ●    ▀████▄█▀▀█        ",
    "       █  ████                    █████  █        ",
    "       ▀▄▄████       ▄███▄        ████▄▄▀         ",
    "          █████     ▀█████▀      █████            ",
    "          ██████▄     ▀▀▀      ▄██████            ",
    "          █████████▄▄▄▄▄▄▄▄▄████████              ",
    "         ████████████████████████████             ",
    "        █████████████████████████████             ",
    "       ███████████████████████████████            ",
    "       ████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      █████████████████████████████████           ",
    "      ████████▀▀▀▀█████████▀▀▀▀███████            ",
    "      ██████        ████       ████████           ",
    "      ███████      ██████       ███████           ",
    "        ▀▀▀▀        ▀▀▀▀         ▀▀▀▀             ",
]

# Perro más pequeño para minijuegos
DOG_MINI = [
    "  ▄▄██▄▄  ",
    " █◕  ◕ █ ",
    " ██▄▄▄██ ",
    "  █████  ",
    " ██   ██ ",
]

DOG_MINI_JUMP = [
    "  \\▄██▄/  ",
    "  █◕◕█   ",
    "  ██▄██  ",
    "   ███   ",
    "  ▀   ▀  ",
]

# Comida con arte detallado
FOOD_BOWL = [
    "      ╭──────────────╮      ",
    "     ╱                ╲     ",
    "    ╱   ░░░░░░░░░░░░   ╲    ",
    "   │   ░░░░░░░░░░░░░░   │   ",
    "   │   ░░░░░░░░░░░░░░   │   ",
    "    ╲                  ╱    ",
    "     ╰────────────────╯     ",
]

FOOD_BOWL_FULL = [
    "      ╭──────────────╮      ",
    "     ╱   ▄▄▄▄▄▄▄▄▄▄   ╲     ",
    "    ╱   █▓▓▓▓▓▓▓▓▓▓█   ╲    ",
    "   │   █▓▓▓▓▓▓▓▓▓▓▓▓█   │   ",
    "   │   █▓▓▓▓▓▓▓▓▓▓▓▓█   │   ",
    "    ╲   ▀▀▀▀▀▀▀▀▀▀▀▀   ╱    ",
    "     ╰────────────────╯     ",
]

DOGFY_BOX = [
    "    ╔══════════════════════╗    ",
    "    ║  ┌────────────────┐  ║    ",
    "    ║  │  DOGFY  DIET   │  ║    ",
    "    ║  │ ════════════   │  ║    ",
    "    ║  │  Comida        │  ║    ",
    "    ║  │  Natural       │  ║    ",
    "    ║  │  Cocinada  🐕   │  ║    ",
    "    ║  └────────────────┘  ║    ",
    "    ╚══════════════════════╝    ",
]

# Escenarios
LIVING_ROOM = [
    "┌────────────────────────────────────────────────────────────────────────────┐",
    "│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│",
    "│░░╔════════╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╔══════════╗░│",
    "│░░║ ◯    ◯ ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║          ║░│",
    "│░░║ WINDOW ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║  RELOJ   ║░│",
    "│░░║        ║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║   ⌚     ║░│",
    "│░░╚════════╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚══════════╝░│",
    "│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│",
    "│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│                                                                            │",
    "│   ╔════════════╗                                          ┌──────────┐    │",
    "│   ║            ║                                          │ 🦴 🦴 🦴 │    │",
    "│   ║   SOFÁ     ║                                          │  CAMA    │    │",
    "│   ║  ▓▓▓▓▓▓▓▓  ║                                          │  PERRO   │    │",
    "│   ╚════════════╝                                          └──────────┘    │",
    "├────────────────────────────────────────────────────────────────────────────┤",
    "│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│",
    "└────────────────────────────────────────────────────────────────────────────┘",
]

PARK = [
    "                    ☀                                                        ",
    "                   ╱│╲              ☁          ☁                             ",
    "          ☁                    ☁                          ☁                  ",
    "                                                                              ",
    "      🌳              🌳                    🌳              🌳                 ",
    "     ████            ████                  ████            ████               ",
    "      ██              ██                    ██              ██                ",
    "      ██              ██                    ██              ██                ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "                                                                              ",
    "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
    "██████████████████████████████████████████████████████████████████████████████",
    "██████████████████████████████████████████████████████████████████████████████",
    "██████████████████████████████████████████████████████████████████████████████",
]

# ══════════════════════════════════════════════════════════════════════════════
# COLORES
# ══════════════════════════════════════════════════════════════════════════════

class Colors(Enum):
    DOGFY_ORANGE = 1
    WHITE = 2
    GREEN = 3
    RED = 4
    YELLOW = 5
    CYAN = 6
    BROWN = 7
    GOLD = 8
    BLUE = 9
    GRAY = 10

# ══════════════════════════════════════════════════════════════════════════════
# DATOS DEL JUEGO
# ══════════════════════════════════════════════════════════════════════════════

RECIPES = {
    'pollo_premium': {
        'name': '🍗 Pollo Premium Dogfy',
        'ingredients': ['Pollo fresco', 'Zanahoria', 'Patata', 'Aceite de oliva'],
        'nutrition': 95,
        'happiness': 20,
        'description': 'Receta estrella con pollo de corral'
    },
    'ternera_gourmet': {
        'name': '🥩 Ternera Gourmet',
        'ingredients': ['Ternera gallega', 'Calabacín', 'Arroz integral', 'Espinacas'],
        'nutrition': 100,
        'happiness': 25,
        'description': 'Para los paladares más exigentes'
    },
    'salmon_omega': {
        'name': '🐟 Salmón Omega-3',
        'ingredients': ['Salmón noruego', 'Boniato', 'Brócoli', 'Aceite de pescado'],
        'nutrition': 98,
        'happiness': 22,
        'description': 'Rico en ácidos grasos esenciales'
    },
    'cordero_mediterraneo': {
        'name': '🍖 Cordero Mediterráneo',
        'ingredients': ['Cordero', 'Calabaza', 'Guisantes', 'Romero'],
        'nutrition': 92,
        'happiness': 23,
        'description': 'Sabores del mediterráneo'
    },
    'pavo_ligero': {
        'name': '🦃 Pavo Ligero',
        'ingredients': ['Pavo', 'Manzana', 'Avena', 'Albahaca'],
        'nutrition': 88,
        'happiness': 18,
        'description': 'Ideal para perros con sobrepeso'
    }
}

ACTIVITIES = {
    'paseo': {'energy': -15, 'happiness': 25, 'health': 5, 'duration': 3},
    'jugar': {'energy': -20, 'happiness': 30, 'health': 3, 'duration': 2},
    'entrenar': {'energy': -25, 'happiness': 15, 'health': 8, 'duration': 4},
    'dormir': {'energy': 40, 'happiness': 5, 'health': 10, 'duration': 5},
    'caricias': {'energy': 5, 'happiness': 20, 'health': 2, 'duration': 1},
}

@dataclass
class Pet:
    name: str
    health: float = 100.0
    happiness: float = 100.0
    energy: float = 100.0
    hunger: float = 0.0
    age_days: int = 0
    meals_eaten: int = 0
    walks_taken: int = 0
    games_played: int = 0
    level: int = 1
    xp: int = 0
    coins: int = 100

@dataclass
class Particle:
    x: float
    y: float
    char: str
    vx: float
    vy: float
    life: int
    color: int

# ══════════════════════════════════════════════════════════════════════════════
# CLASE PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

class DogfyLife:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.setup_curses()

        self.height, self.width = stdscr.getmaxyx()
        self.pet = Pet(name="Max")
        self.current_screen = 'home'
        self.current_animation = 'idle'
        self.animation_frame = 0
        self.frame_counter = 0
        self.particles: List[Particle] = []
        self.notifications: List[Dict] = []
        self.selected_option = 0
        self.last_feed_time = time.time()
        self.game_time = 0

        # Minijuego
        self.minigame_active = False
        self.minigame_type = None
        self.minigame_score = 0
        self.minigame_data = {}

    def setup_curses(self):
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)

        # Colores Dogfy Diet
        curses.init_pair(Colors.DOGFY_ORANGE.value, curses.COLOR_YELLOW, -1)
        curses.init_pair(Colors.WHITE.value, curses.COLOR_WHITE, -1)
        curses.init_pair(Colors.GREEN.value, curses.COLOR_GREEN, -1)
        curses.init_pair(Colors.RED.value, curses.COLOR_RED, -1)
        curses.init_pair(Colors.YELLOW.value, curses.COLOR_YELLOW, -1)
        curses.init_pair(Colors.CYAN.value, curses.COLOR_CYAN, -1)
        curses.init_pair(Colors.BROWN.value, curses.COLOR_YELLOW, -1)
        curses.init_pair(Colors.GOLD.value, curses.COLOR_YELLOW, -1)
        curses.init_pair(Colors.BLUE.value, curses.COLOR_BLUE, -1)
        curses.init_pair(Colors.GRAY.value, curses.COLOR_WHITE, -1)

        if curses.can_change_color() and curses.COLORS >= 256:
            try:
                curses.init_color(20, 933, 412, 282)  # #ee6948
                curses.init_pair(Colors.DOGFY_ORANGE.value, 20, -1)
            except:
                pass

    def add_notification(self, text: str, color: int = Colors.WHITE.value):
        self.notifications.append({
            'text': text,
            'color': color,
            'life': 120
        })

    def add_particles(self, x: int, y: int, count: int, color: int, chars: List[str] = None):
        if chars is None:
            chars = ['✦', '★', '•', '·', '+']
        for _ in range(count):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(0.5, 2.0)
            self.particles.append(Particle(
                x=x, y=y,
                char=random.choice(chars),
                vx=math.cos(angle) * speed,
                vy=math.sin(angle) * speed * 0.5 - 0.5,
                life=random.randint(15, 30),
                color=color
            ))

    def update_pet_stats(self):
        """Actualizar estadísticas del perro con el tiempo"""
        self.game_time += 1

        # Hambre aumenta con el tiempo
        if self.game_time % 300 == 0:  # Cada ~5 segundos
            self.pet.hunger = min(100, self.pet.hunger + 2)
            self.pet.energy = max(0, self.pet.energy - 1)

            # Si tiene hambre, baja felicidad
            if self.pet.hunger > 70:
                self.pet.happiness = max(0, self.pet.happiness - 2)
                if self.pet.hunger > 90:
                    self.pet.health = max(0, self.pet.health - 1)

        # Determinar animación según estado
        if self.pet.energy < 20:
            self.current_animation = 'sleeping'
        elif self.pet.hunger > 80:
            self.current_animation = 'sad'
        elif self.pet.happiness > 80:
            self.current_animation = 'happy'
        else:
            self.current_animation = 'idle'

    def feed_pet(self, recipe_key: str):
        """Alimentar al perro con una receta Dogfy"""
        if recipe_key not in RECIPES:
            return

        recipe = RECIPES[recipe_key]
        self.pet.hunger = max(0, self.pet.hunger - 50)
        self.pet.health = min(100, self.pet.health + recipe['nutrition'] * 0.2)
        self.pet.happiness = min(100, self.pet.happiness + recipe['happiness'])
        self.pet.meals_eaten += 1
        self.pet.xp += 25

        self.current_animation = 'eating'
        self.add_notification(f"¡{self.pet.name} disfrutó {recipe['name']}!", Colors.GREEN.value)
        self.add_particles(self.width // 2, self.height // 2, 20, Colors.DOGFY_ORANGE.value,
                          ['♥', '★', '✦', '🍖', '🦴'])

        self.check_level_up()

    def do_activity(self, activity_key: str):
        """Realizar una actividad con el perro"""
        if activity_key not in ACTIVITIES:
            return

        activity = ACTIVITIES[activity_key]

        # Verificar energía
        if self.pet.energy + activity['energy'] < 0:
            self.add_notification(f"¡{self.pet.name} está muy cansado!", Colors.RED.value)
            return

        self.pet.energy = max(0, min(100, self.pet.energy + activity['energy']))
        self.pet.happiness = min(100, self.pet.happiness + activity['happiness'])
        self.pet.health = min(100, self.pet.health + activity['health'])
        self.pet.xp += 15

        if activity_key == 'paseo':
            self.pet.walks_taken += 1
            self.current_animation = 'walking'
        elif activity_key == 'jugar':
            self.pet.games_played += 1
            self.current_animation = 'playing'
        elif activity_key == 'dormir':
            self.current_animation = 'sleeping'
        elif activity_key == 'caricias':
            self.current_animation = 'happy'

        self.add_notification(f"¡{self.pet.name} está feliz!", Colors.GREEN.value)
        self.check_level_up()

    def check_level_up(self):
        """Verificar si sube de nivel"""
        xp_needed = self.pet.level * 100
        if self.pet.xp >= xp_needed:
            self.pet.level += 1
            self.pet.xp = 0
            self.pet.coins += 50
            self.add_notification(f"¡NIVEL {self.pet.level}! +50 monedas", Colors.GOLD.value)
            self.add_particles(self.width // 2, 10, 50, Colors.GOLD.value,
                              ['★', '✦', '◆', '●'])

    def start_minigame(self, game_type: str):
        """Iniciar un minijuego"""
        self.minigame_active = True
        self.minigame_type = game_type
        self.minigame_score = 0

        if game_type == 'catch':
            self.minigame_data = {
                'dog_x': self.width // 2,
                'dog_y': self.height - 10,
                'treats': [],
                'timer': 600,  # 10 segundos a 60fps
                'spawn_timer': 0
            }
        elif game_type == 'memory':
            cards = ['🍗', '🥩', '🐟', '🥕', '🥦', '🎃', '🥚', '🍖'] * 2
            random.shuffle(cards)
            self.minigame_data = {
                'cards': cards,
                'revealed': [False] * 16,
                'matched': [False] * 16,
                'selected': [],
                'moves': 0,
                'matches': 0
            }

    def update_minigame(self):
        """Actualizar minijuego activo"""
        if not self.minigame_active:
            return

        if self.minigame_type == 'catch':
            data = self.minigame_data
            data['timer'] -= 1

            # Spawn treats
            data['spawn_timer'] += 1
            if data['spawn_timer'] > 30:
                data['spawn_timer'] = 0
                data['treats'].append({
                    'x': random.randint(5, self.width - 10),
                    'y': 5,
                    'type': random.choice(['🍗', '🥩', '🐟', '🥕', '💀']),
                })

            # Move treats
            for treat in data['treats'][:]:
                treat['y'] += 0.5
                if treat['y'] > self.height - 5:
                    data['treats'].remove(treat)

                # Collision
                if abs(treat['x'] - data['dog_x']) < 5 and abs(treat['y'] - data['dog_y']) < 3:
                    data['treats'].remove(treat)
                    if treat['type'] == '💀':
                        self.minigame_score -= 10
                        self.add_particles(int(treat['x']), int(treat['y']), 10, Colors.RED.value)
                    else:
                        self.minigame_score += 10
                        self.add_particles(int(treat['x']), int(treat['y']), 10, Colors.GREEN.value)

            # End game
            if data['timer'] <= 0:
                self.end_minigame()

    def end_minigame(self):
        """Terminar minijuego"""
        self.minigame_active = False
        reward = max(0, self.minigame_score // 5)
        self.pet.coins += reward
        self.pet.happiness = min(100, self.pet.happiness + 15)
        self.pet.xp += self.minigame_score

        self.add_notification(f"¡Juego terminado! +{reward} monedas", Colors.GOLD.value)
        self.check_level_up()

    def handle_input(self) -> bool:
        """Procesar entrada"""
        try:
            key = self.stdscr.getch()
        except:
            return True

        if key == ord('q') or key == 27:
            if self.minigame_active:
                self.end_minigame()
            elif self.current_screen != 'home':
                self.current_screen = 'home'
            else:
                return False

        elif self.minigame_active:
            # Controles del minijuego
            if self.minigame_type == 'catch':
                if key == curses.KEY_LEFT or key == ord('a'):
                    self.minigame_data['dog_x'] = max(5, self.minigame_data['dog_x'] - 4)
                elif key == curses.KEY_RIGHT or key == ord('d'):
                    self.minigame_data['dog_x'] = min(self.width - 10, self.minigame_data['dog_x'] + 4)
        else:
            # Navegación normal
            if key == curses.KEY_UP or key == ord('w'):
                self.selected_option = max(0, self.selected_option - 1)
            elif key == curses.KEY_DOWN or key == ord('s'):
                self.selected_option = min(self.get_max_options() - 1, self.selected_option + 1)
            elif key == ord('\n') or key == ord(' '):
                self.select_option()
            elif key == ord('1'):
                self.current_screen = 'feed'
                self.selected_option = 0
            elif key == ord('2'):
                self.current_screen = 'activities'
                self.selected_option = 0
            elif key == ord('3'):
                self.current_screen = 'games'
                self.selected_option = 0
            elif key == ord('4'):
                self.current_screen = 'stats'
            elif key == ord('h'):
                self.current_screen = 'home'

        return True

    def get_max_options(self) -> int:
        if self.current_screen == 'home':
            return 4
        elif self.current_screen == 'feed':
            return len(RECIPES)
        elif self.current_screen == 'activities':
            return len(ACTIVITIES)
        elif self.current_screen == 'games':
            return 2
        return 0

    def select_option(self):
        if self.current_screen == 'home':
            screens = ['feed', 'activities', 'games', 'stats']
            self.current_screen = screens[self.selected_option]
            self.selected_option = 0
        elif self.current_screen == 'feed':
            recipe_key = list(RECIPES.keys())[self.selected_option]
            self.feed_pet(recipe_key)
        elif self.current_screen == 'activities':
            activity_key = list(ACTIVITIES.keys())[self.selected_option]
            self.do_activity(activity_key)
        elif self.current_screen == 'games':
            if self.selected_option == 0:
                self.start_minigame('catch')

    def update(self):
        """Actualizar juego"""
        self.frame_counter += 1

        # Animación
        if self.frame_counter % 15 == 0:
            self.animation_frame = (self.animation_frame + 1) % 2

        # Estadísticas del perro
        self.update_pet_stats()

        # Minijuego
        self.update_minigame()

        # Partículas
        for particle in self.particles[:]:
            particle.x += particle.vx
            particle.y += particle.vy
            particle.vy += 0.05
            particle.life -= 1
            if particle.life <= 0:
                self.particles.remove(particle)

        # Notificaciones
        for notif in self.notifications[:]:
            notif['life'] -= 1
            if notif['life'] <= 0:
                self.notifications.remove(notif)

    def draw(self):
        """Renderizar juego"""
        self.stdscr.erase()

        if self.minigame_active:
            self.draw_minigame()
        else:
            self.draw_main_screen()

        # Partículas siempre visibles
        self.draw_particles()

        # Notificaciones
        self.draw_notifications()

        self.stdscr.refresh()

    def draw_main_screen(self):
        """Dibujar pantalla principal"""
        # Header con logo Dogfy
        self.draw_header()

        # Barras de estado
        self.draw_status_bars()

        # Perro
        self.draw_dog()

        # Menú según pantalla
        if self.current_screen == 'home':
            self.draw_home_menu()
        elif self.current_screen == 'feed':
            self.draw_feed_menu()
        elif self.current_screen == 'activities':
            self.draw_activities_menu()
        elif self.current_screen == 'games':
            self.draw_games_menu()
        elif self.current_screen == 'stats':
            self.draw_stats_screen()

        # Footer
        self.draw_footer()

    def draw_header(self):
        """Dibujar header con logo"""
        header = "═" * (self.width - 2)
        self.safe_addstr(0, 1, header, curses.color_pair(Colors.DOGFY_ORANGE.value))

        logo = f" 🐕 DOGFY LIFE - {self.pet.name} "
        logo_x = (self.width - len(logo)) // 2
        self.safe_addstr(1, logo_x, logo,
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        # Monedas y nivel
        coins_text = f" 💰 {self.pet.coins} "
        level_text = f" ⭐ Nivel {self.pet.level} "
        xp_text = f" XP: {self.pet.xp}/{self.pet.level * 100} "

        self.safe_addstr(1, 2, coins_text, curses.color_pair(Colors.GOLD.value) | curses.A_BOLD)
        self.safe_addstr(1, self.width - len(level_text) - len(xp_text) - 2, level_text,
                        curses.color_pair(Colors.YELLOW.value) | curses.A_BOLD)
        self.safe_addstr(1, self.width - len(xp_text) - 2, xp_text,
                        curses.color_pair(Colors.CYAN.value))

        self.safe_addstr(2, 1, header, curses.color_pair(Colors.DOGFY_ORANGE.value))

    def draw_status_bars(self):
        """Dibujar barras de estado"""
        bar_width = 20
        start_y = 4

        stats = [
            ('❤️  Salud', self.pet.health, Colors.RED.value),
            ('😊 Felicidad', self.pet.happiness, Colors.YELLOW.value),
            ('⚡ Energía', self.pet.energy, Colors.CYAN.value),
            ('🍖 Hambre', 100 - self.pet.hunger, Colors.GREEN.value),
        ]

        for i, (label, value, color) in enumerate(stats):
            y = start_y + i
            filled = int((value / 100) * bar_width)
            empty = bar_width - filled

            self.safe_addstr(y, 3, f"{label}: ", curses.color_pair(Colors.WHITE.value))
            self.safe_addstr(y, 17, "[", curses.color_pair(Colors.WHITE.value))
            self.safe_addstr(y, 18, "█" * filled, curses.color_pair(color) | curses.A_BOLD)
            self.safe_addstr(y, 18 + filled, "░" * empty, curses.color_pair(Colors.GRAY.value))
            self.safe_addstr(y, 18 + bar_width, f"] {int(value)}%",
                           curses.color_pair(Colors.WHITE.value))

    def draw_dog(self):
        """Dibujar el perro con animación"""
        # Seleccionar frame según animación
        if self.current_animation == 'happy':
            frames = DOG_HAPPY
        elif self.current_animation == 'eating':
            frames = DOG_EATING
        elif self.current_animation == 'sleeping':
            frames = DOG_SLEEPING
        elif self.current_animation == 'sad':
            frames = DOG_SAD
        elif self.current_animation == 'playing':
            frames = DOG_PLAYING
        elif self.current_animation == 'walking':
            frames = DOG_WALK_1 if self.animation_frame == 0 else DOG_WALK_2
        else:
            frames = DOG_IDLE

        # Centrar perro
        dog_width = max(len(line) for line in frames)
        dog_x = (self.width - dog_width) // 2
        dog_y = 10

        # Color según estado
        if self.pet.health < 30:
            color = Colors.RED.value
        elif self.pet.happiness > 80:
            color = Colors.DOGFY_ORANGE.value
        else:
            color = Colors.BROWN.value

        for i, line in enumerate(frames):
            self.safe_addstr(dog_y + i, dog_x, line,
                           curses.color_pair(color) | curses.A_BOLD)

    def draw_home_menu(self):
        """Dibujar menú principal"""
        menu_y = self.height - 12
        menu_items = [
            ('1', '🍗 Alimentar', 'Comida natural Dogfy Diet'),
            ('2', '🎾 Actividades', 'Paseo, jugar, entrenar...'),
            ('3', '🎮 Minijuegos', 'Gana monedas jugando'),
            ('4', '📊 Estadísticas', 'Ver progreso de tu mascota'),
        ]

        self.safe_addstr(menu_y - 2, 3, "═══════════ MENÚ ═══════════",
                        curses.color_pair(Colors.DOGFY_ORANGE.value))

        for i, (key, title, desc) in enumerate(menu_items):
            y = menu_y + i
            if i == self.selected_option:
                attr = curses.A_REVERSE | curses.A_BOLD
                prefix = "▶ "
            else:
                attr = curses.A_NORMAL
                prefix = "  "

            self.safe_addstr(y, 3, f"{prefix}[{key}] {title}",
                           curses.color_pair(Colors.DOGFY_ORANGE.value) | attr)
            self.safe_addstr(y, 30, desc, curses.color_pair(Colors.GRAY.value))

    def draw_feed_menu(self):
        """Dibujar menú de alimentación"""
        menu_y = 10
        self.safe_addstr(menu_y - 2, 3, "═══════════ MENÚ DOGFY DIET ═══════════",
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        for i, (key, recipe) in enumerate(RECIPES.items()):
            y = menu_y + i * 2
            if i == self.selected_option:
                attr = curses.A_REVERSE | curses.A_BOLD
                prefix = "▶ "
            else:
                attr = curses.A_NORMAL
                prefix = "  "

            self.safe_addstr(y, 3, f"{prefix}{recipe['name']}",
                           curses.color_pair(Colors.DOGFY_ORANGE.value) | attr)
            self.safe_addstr(y + 1, 5, f"  {recipe['description']}",
                           curses.color_pair(Colors.GRAY.value))

        # Mostrar caja Dogfy
        box_x = self.width - 35
        for i, line in enumerate(DOGFY_BOX):
            self.safe_addstr(menu_y + i, box_x, line,
                           curses.color_pair(Colors.DOGFY_ORANGE.value))

        self.safe_addstr(self.height - 5, 3, "[ENTER] Seleccionar   [Q] Volver",
                        curses.color_pair(Colors.WHITE.value))

    def draw_activities_menu(self):
        """Dibujar menú de actividades"""
        menu_y = 10
        self.safe_addstr(menu_y - 2, 3, "═══════════ ACTIVIDADES ═══════════",
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        activity_names = {
            'paseo': '🚶 Paseo',
            'jugar': '🎾 Jugar',
            'entrenar': '🏋️ Entrenar',
            'dormir': '😴 Dormir',
            'caricias': '🤗 Caricias',
        }

        for i, (key, activity) in enumerate(ACTIVITIES.items()):
            y = menu_y + i * 2
            if i == self.selected_option:
                attr = curses.A_REVERSE | curses.A_BOLD
                prefix = "▶ "
            else:
                attr = curses.A_NORMAL
                prefix = "  "

            name = activity_names.get(key, key)
            effects = []
            if activity['energy'] != 0:
                effects.append(f"Energía: {activity['energy']:+d}")
            if activity['happiness'] != 0:
                effects.append(f"Felicidad: {activity['happiness']:+d}")

            self.safe_addstr(y, 3, f"{prefix}{name}",
                           curses.color_pair(Colors.DOGFY_ORANGE.value) | attr)
            self.safe_addstr(y + 1, 5, f"  {' | '.join(effects)}",
                           curses.color_pair(Colors.GRAY.value))

        self.safe_addstr(self.height - 5, 3, "[ENTER] Seleccionar   [Q] Volver",
                        curses.color_pair(Colors.WHITE.value))

    def draw_games_menu(self):
        """Dibujar menú de juegos"""
        menu_y = 10
        self.safe_addstr(menu_y - 2, 3, "═══════════ MINIJUEGOS ═══════════",
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        games = [
            ('🎯 Atrapa Premios', 'Atrapa la comida que cae, evita lo malo'),
            ('🧠 Memoria', 'Encuentra las parejas de ingredientes'),
        ]

        for i, (name, desc) in enumerate(games):
            y = menu_y + i * 3
            if i == self.selected_option:
                attr = curses.A_REVERSE | curses.A_BOLD
                prefix = "▶ "
            else:
                attr = curses.A_NORMAL
                prefix = "  "

            self.safe_addstr(y, 3, f"{prefix}{name}",
                           curses.color_pair(Colors.DOGFY_ORANGE.value) | attr)
            self.safe_addstr(y + 1, 5, f"  {desc}",
                           curses.color_pair(Colors.GRAY.value))

        self.safe_addstr(self.height - 5, 3, "[ENTER] Jugar   [Q] Volver",
                        curses.color_pair(Colors.WHITE.value))

    def draw_stats_screen(self):
        """Dibujar pantalla de estadísticas"""
        menu_y = 10
        self.safe_addstr(menu_y - 2, 3, "═══════════ ESTADÍSTICAS ═══════════",
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        stats = [
            f"🐕 Nombre: {self.pet.name}",
            f"⭐ Nivel: {self.pet.level}",
            f"📈 XP: {self.pet.xp}/{self.pet.level * 100}",
            f"💰 Monedas: {self.pet.coins}",
            "",
            f"🍗 Comidas servidas: {self.pet.meals_eaten}",
            f"🚶 Paseos dados: {self.pet.walks_taken}",
            f"🎾 Juegos jugados: {self.pet.games_played}",
            "",
            "════════════════════════════════════",
            "",
            "Powered by Dogfy Diet",
            "Comida natural cocinada para perros",
            "dogfydiet.com - Barcelona, España",
        ]

        for i, line in enumerate(stats):
            color = Colors.DOGFY_ORANGE.value if '═' in line or 'Dogfy' in line else Colors.WHITE.value
            self.safe_addstr(menu_y + i, 3, line, curses.color_pair(color))

        self.safe_addstr(self.height - 5, 3, "[Q] Volver",
                        curses.color_pair(Colors.WHITE.value))

    def draw_minigame(self):
        """Dibujar minijuego activo"""
        if self.minigame_type == 'catch':
            self.draw_catch_game()

    def draw_catch_game(self):
        """Dibujar juego de atrapar"""
        data = self.minigame_data

        # Fondo
        self.safe_addstr(0, 0, "═" * self.width, curses.color_pair(Colors.DOGFY_ORANGE.value))
        title = f" 🎯 ATRAPA PREMIOS - Puntos: {self.minigame_score} - Tiempo: {data['timer'] // 60}s "
        self.safe_addstr(1, (self.width - len(title)) // 2, title,
                        curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)
        self.safe_addstr(2, 0, "═" * self.width, curses.color_pair(Colors.DOGFY_ORANGE.value))

        # Treats
        for treat in data['treats']:
            self.safe_addstr(int(treat['y']), int(treat['x']), treat['type'],
                           curses.color_pair(Colors.GREEN.value if treat['type'] != '💀' else Colors.RED.value))

        # Perro mini
        dog_y = data['dog_y']
        dog_x = data['dog_x']
        for i, line in enumerate(DOG_MINI):
            self.safe_addstr(dog_y + i, dog_x, line,
                           curses.color_pair(Colors.DOGFY_ORANGE.value) | curses.A_BOLD)

        # Suelo
        self.safe_addstr(self.height - 3, 0, "▓" * self.width,
                        curses.color_pair(Colors.GREEN.value))

        # Instrucciones
        self.safe_addstr(self.height - 1, 3, "← → Mover   [Q] Salir",
                        curses.color_pair(Colors.WHITE.value))

    def draw_particles(self):
        """Dibujar partículas"""
        for p in self.particles:
            self.safe_addstr(int(p.y), int(p.x), p.char,
                           curses.color_pair(p.color) | curses.A_BOLD)

    def draw_notifications(self):
        """Dibujar notificaciones"""
        for i, notif in enumerate(self.notifications[-3:]):  # Máx 3 notificaciones
            y = self.height - 8 + i
            alpha = min(1.0, notif['life'] / 60)
            attr = curses.A_BOLD if alpha > 0.5 else curses.A_DIM

            # Fondo
            text = f" {notif['text']} "
            x = (self.width - len(text)) // 2
            self.safe_addstr(y, x, text, curses.color_pair(notif['color']) | attr | curses.A_REVERSE)

    def draw_footer(self):
        """Dibujar footer"""
        footer = "═" * (self.width - 2)
        self.safe_addstr(self.height - 2, 1, footer, curses.color_pair(Colors.DOGFY_ORANGE.value))

        help_text = " [1-4] Menú | [↑↓] Navegar | [ENTER] Seleccionar | [Q] Salir/Volver | [H] Inicio "
        help_x = (self.width - len(help_text)) // 2
        self.safe_addstr(self.height - 1, help_x, help_text,
                        curses.color_pair(Colors.GRAY.value))

    def safe_addstr(self, y: int, x: int, text: str, attr=0):
        try:
            if 0 <= y < self.height and 0 <= x < self.width:
                max_len = self.width - x - 1
                if max_len > 0:
                    self.stdscr.addstr(y, x, text[:max_len], attr)
        except curses.error:
            pass

    def run(self):
        """Bucle principal"""
        self.show_intro()

        while True:
            if not self.handle_input():
                break

            self.update()
            self.draw()

            time.sleep(1/60)

    def show_intro(self):
        """Mostrar pantalla de introducción"""
        intro = [
            "",
            "╔══════════════════════════════════════════════════════════════╗",
            "║                                                              ║",
            "║   ██████╗  ██████╗  ██████╗ ███████╗██╗   ██╗                ║",
            "║   ██╔══██╗██╔═══██╗██╔════╝ ██╔════╝╚██╗ ██╔╝                ║",
            "║   ██║  ██║██║   ██║██║  ███╗█████╗   ╚████╔╝                 ║",
            "║   ██║  ██║██║   ██║██║   ██║██╔══╝    ╚██╔╝                  ║",
            "║   ██████╔╝╚██████╔╝╚██████╔╝██║        ██║                   ║",
            "║   ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝        ╚═╝                   ║",
            "║                                                              ║",
            "║              ██╗     ██╗███████╗███████╗                     ║",
            "║              ██║     ██║██╔════╝██╔════╝                     ║",
            "║              ██║     ██║█████╗  █████╗                       ║",
            "║              ██║     ██║██╔══╝  ██╔══╝                       ║",
            "║              ███████╗██║██║     ███████╗                     ║",
            "║              ╚══════╝╚═╝╚═╝     ╚══════╝                     ║",
            "║                                                              ║",
            "║          🐕 Simulador de Mascota Virtual 🐕                   ║",
            "║                                                              ║",
            "║              Powered by Dogfy Diet                           ║",
            "║          Comida natural cocinada para perros                 ║",
            "║                  Barcelona, España                           ║",
            "║                                                              ║",
            "╚══════════════════════════════════════════════════════════════╝",
            "",
            "              Presiona ESPACIO para comenzar                    ",
            "",
        ]

        while True:
            self.stdscr.erase()

            start_y = max(0, (self.height - len(intro)) // 2)
            for i, line in enumerate(intro):
                x = max(0, (self.width - len(line)) // 2)
                color = Colors.DOGFY_ORANGE.value if '═' in line or '║' in line or '╔' in line or '╚' in line else Colors.WHITE.value
                self.safe_addstr(start_y + i, x, line,
                               curses.color_pair(color) | curses.A_BOLD)

            self.stdscr.refresh()

            try:
                key = self.stdscr.getch()
                if key == ord(' '):
                    break
                elif key == ord('q'):
                    raise KeyboardInterrupt
            except:
                pass

            time.sleep(1/30)


def main(stdscr):
    game = DogfyLife(stdscr)
    game.run()


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    🐕 DOGFY LIFE 🐕                           ║
║                                                              ║
║         Simulador de mascota virtual premium                 ║
║              Powered by Dogfy Diet                           ║
║                                                              ║
║         Cargando experiencia interactiva...                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ¡Gracias por jugar DOGFY LIFE!                             ║
║                                                              ║
║   🐕 Tu mascota virtual te extrañará...                       ║
║                                                              ║
║   ─────────────────────────────────────────────              ║
║                                                              ║
║   Dogfy Diet - Comida natural cocinada para perros           ║
║   🌐 dogfydiet.com                                            ║
║   📍 Barcelona, España                                        ║
║                                                              ║
║   "Alimenta a tu mejor amigo como se merece"                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """)
