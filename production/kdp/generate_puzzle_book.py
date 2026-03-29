"""
GENERATEUR DE PUZZLE BOOKS POUR AMAZON KDP
==========================================
Produit des livres de puzzles (Word Search + Sudoku) en PDF prêts pour KDP.

Usage:
    python generate_puzzle_book.py --type wordsearch --theme animals --title "Animal Word Search"
    python generate_puzzle_book.py --type sudoku --difficulty medium --title "Sudoku Challenge"
    python generate_puzzle_book.py --type wordsearch --theme all --puzzles 50 --large-print

Prérequis:
    pip install reportlab

Exécuter depuis : C:\\Users\\zapk\\OneDrive\\Jacky\\production\\kdp\\
"""

import argparse
import random
import string
import copy
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, black, white, lightgrey, grey

# =============================================================================
# WORD LISTS BY THEME (English — marché US/global)
# =============================================================================

THEMES = {
    "animals": {
        "name": "Animals",
        "words": [
            "ELEPHANT", "GIRAFFE", "PENGUIN", "DOLPHIN", "BUTTERFLY",
            "KANGAROO", "CHAMELEON", "OCTOPUS", "FLAMINGO", "CROCODILE",
            "GORILLA", "JELLYFISH", "LEOPARD", "PELICAN", "SEAHORSE",
            "TORTOISE", "ARMADILLO", "EAGLE", "PARROT", "PANTHER",
        ]
    },
    "space": {
        "name": "Space & Astronomy",
        "words": [
            "ASTEROID", "GALAXY", "NEBULA", "SATELLITE", "TELESCOPE",
            "ASTRONAUT", "BLACKHOLE", "COMET", "ECLIPSE", "GRAVITY",
            "JUPITER", "MERCURY", "NEPTUNE", "ORBIT", "PLANET",
            "QUASAR", "SATURN", "SUPERNOVA", "UNIVERSE", "METEOR",
        ]
    },
    "food": {
        "name": "Food & Cooking",
        "words": [
            "AVOCADO", "BROCCOLI", "CHOCOLATE", "CINNAMON", "CROISSANT",
            "ESPRESSO", "LASAGNA", "MUSHROOM", "PANCAKE", "PINEAPPLE",
            "RASPBERRY", "SPAGHETTI", "STRAWBERRY", "WATERMELON", "BLUEBERRY",
            "ARTICHOKE", "ASPARAGUS", "PEPPERONI", "ZUCCHINI", "MOZZARELLA",
        ]
    },
    "nature": {
        "name": "Nature & Outdoors",
        "words": [
            "AVALANCHE", "BLIZZARD", "CANYON", "DESERT", "EARTHQUAKE",
            "FOREST", "GLACIER", "HORIZON", "ISLAND", "JUNGLE",
            "LAGOON", "MEADOW", "MOUNTAIN", "PRAIRIE", "RAINBOW",
            "SUNRISE", "THUNDER", "TORNADO", "VOLCANO", "WATERFALL",
        ]
    },
    "sports": {
        "name": "Sports",
        "words": [
            "ARCHERY", "BASEBALL", "BASKETBALL", "BOXING", "CRICKET",
            "CYCLING", "FENCING", "FOOTBALL", "GYMNASTICS", "HANDBALL",
            "HOCKEY", "KARATE", "LACROSSE", "MARATHON", "SAILING",
            "SKIING", "SOCCER", "SWIMMING", "TENNIS", "VOLLEYBALL",
        ]
    },
    "travel": {
        "name": "Travel & Adventure",
        "words": [
            "ADVENTURE", "AIRPORT", "BACKPACK", "BOARDING", "CAMPING",
            "COMPASS", "CRUISE", "CUSTOMS", "EXPLORE", "HIGHWAY",
            "JOURNEY", "LUGGAGE", "PASSPORT", "RAILWAY", "RESORT",
            "SUITCASE", "TERMINAL", "TOURIST", "VACATION", "WANDERLUST",
        ]
    },
    "music": {
        "name": "Music",
        "words": [
            "ACOUSTIC", "AMPLIFIER", "BASSOON", "CLARINET", "CONCERT",
            "DRUMSTICK", "GUITAR", "HARMONICA", "KEYBOARD", "MANDOLIN",
            "MELODY", "ORCHESTRA", "PIANO", "RHYTHM", "SAXOPHONE",
            "SYMPHONY", "TAMBOURINE", "TROMBONE", "TRUMPET", "VIOLIN",
        ]
    },
    "ocean": {
        "name": "Ocean & Marine Life",
        "words": [
            "ANCHOR", "BARNACLE", "CAPTAIN", "CORAL", "CURRENT",
            "DOLPHIN", "FISHING", "HARBOR", "ICEBERG", "LIGHTHOUSE",
            "MERMAID", "NAUTICAL", "OYSTER", "PLANKTON", "SAILBOAT",
            "SEAGULL", "SHIPWRECK", "STARFISH", "SUBMARINE", "TREASURE",
        ]
    },
    "science": {
        "name": "Science",
        "words": [
            "ANATOMY", "BIOLOGY", "CATALYST", "CHEMISTRY", "CIRCUIT",
            "COMPOUND", "ELECTRON", "ELEMENT", "EQUATION", "EXPERIMENT",
            "FORMULA", "GENETICS", "HYDROGEN", "ISOTOPE", "LABORATORY",
            "MOLECULE", "NEUTRON", "NUCLEUS", "ORGANISM", "QUANTUM",
        ]
    },
    "holidays": {
        "name": "Holidays & Celebrations",
        "words": [
            "BIRTHDAY", "CANDY", "CARNIVAL", "CHRISTMAS", "COSTUME",
            "DECORATION", "FIREWORK", "GARLAND", "HALLOWEEN", "HARVEST",
            "LANTERN", "MISTLETOE", "ORNAMENT", "PARADE", "PUMPKIN",
            "REINDEER", "SNOWFLAKE", "SPARKLER", "VALENTINE", "WREATH",
        ]
    },
}

# =============================================================================
# WORD SEARCH GENERATOR
# =============================================================================

# 8 directions : droite, bas, gauche, haut, et les 4 diagonales
DIRECTIONS = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1),
]


def generate_word_search(words, grid_size=15):
    """
    Génère une grille de mots mêlés.
    Retourne (grid, placed_words, word_positions).
    word_positions = {word: [(row, col), ...]}
    """
    grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    placed_words = []
    word_positions = {}

    # Trier par longueur décroissante (les longs mots d'abord = plus facile à placer)
    sorted_words = sorted(words, key=len, reverse=True)

    for word in sorted_words:
        if len(word) > grid_size:
            continue
        placed = False
        # Essayer 100 fois de placer le mot
        for _ in range(100):
            direction = random.choice(DIRECTIONS)
            dr, dc = direction
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)

            # Vérifier que le mot tient dans la grille
            end_row = row + dr * (len(word) - 1)
            end_col = col + dc * (len(word) - 1)
            if not (0 <= end_row < grid_size and 0 <= end_col < grid_size):
                continue

            # Vérifier qu'il n'y a pas de conflit
            positions = []
            conflict = False
            for i, letter in enumerate(word):
                r = row + dr * i
                c = col + dc * i
                if grid[r][c] != '' and grid[r][c] != letter:
                    conflict = True
                    break
                positions.append((r, c))

            if conflict:
                continue

            # Placer le mot
            for i, letter in enumerate(word):
                r = row + dr * i
                c = col + dc * i
                grid[r][c] = letter

            placed_words.append(word)
            word_positions[word] = positions
            placed = True
            break

    # Remplir les cases vides avec des lettres aléatoires
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == '':
                grid[r][c] = random.choice(string.ascii_uppercase)

    return grid, placed_words, word_positions


# =============================================================================
# SUDOKU GENERATOR
# =============================================================================

# Grille de base valide (on la transforme aléatoirement pour chaque puzzle)
BASE_SUDOKU = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

DIFFICULTY_CELLS_TO_REMOVE = {
    "easy": 35,
    "medium": 45,
    "hard": 53,
}


def transform_sudoku(base):
    """Applique des transformations aléatoires à une grille valide pour en créer une nouvelle."""
    grid = copy.deepcopy(base)

    # 1. Permuter les chiffres (ex: tous les 3 deviennent des 7, etc.)
    mapping = list(range(1, 10))
    random.shuffle(mapping)
    digit_map = {i + 1: mapping[i] for i in range(9)}
    for r in range(9):
        for c in range(9):
            grid[r][c] = digit_map[grid[r][c]]

    # 2. Permuter des lignes dans un même band (groupes de 3 lignes)
    for band in range(3):
        rows = [band * 3, band * 3 + 1, band * 3 + 2]
        random.shuffle(rows)
        new_rows = [grid[r] for r in rows]
        for i, r in enumerate(range(band * 3, band * 3 + 3)):
            grid[r] = new_rows[i]

    # 3. Permuter des colonnes dans un même stack (groupes de 3 colonnes)
    for stack in range(3):
        cols = [stack * 3, stack * 3 + 1, stack * 3 + 2]
        random.shuffle(cols)
        for r in range(9):
            new_vals = [grid[r][c] for c in cols]
            for i, c in enumerate(range(stack * 3, stack * 3 + 3)):
                grid[r][c] = new_vals[i]

    # 4. Permuter les bands entre eux
    bands = [0, 1, 2]
    random.shuffle(bands)
    new_grid = []
    for b in bands:
        for r in range(b * 3, b * 3 + 3):
            new_grid.append(grid[r])
    grid = new_grid

    # 5. Transposer (50% de chance)
    if random.random() > 0.5:
        grid = [[grid[r][c] for r in range(9)] for c in range(9)]

    return grid


def generate_sudoku(difficulty="medium"):
    """Génère un puzzle sudoku avec sa solution."""
    solution = transform_sudoku(BASE_SUDOKU)
    puzzle = copy.deepcopy(solution)

    cells_to_remove = DIFFICULTY_CELLS_TO_REMOVE.get(difficulty, 45)

    # Retirer des cellules aléatoirement
    all_cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(all_cells)

    removed = 0
    for r, c in all_cells:
        if removed >= cells_to_remove:
            break
        puzzle[r][c] = 0
        removed += 1

    return puzzle, solution


# =============================================================================
# PDF BUILDER
# =============================================================================

class PuzzleBookPDF:
    """Construit un PDF de puzzle book prêt pour KDP."""

    def __init__(self, filename, title, subtitle="", author=""):
        self.filename = filename
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.c = canvas.Canvas(filename, pagesize=letter)
        self.width, self.height = letter  # 612 x 792 points
        self.margin = 0.75 * inch
        self.page_num = 0

    def _add_page_number(self):
        """Ajoute le numéro de page en bas."""
        self.page_num += 1
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(grey)
        self.c.drawCentredString(self.width / 2, 0.5 * inch, str(self.page_num))
        self.c.setFillColor(black)

    def add_title_page(self):
        """Page de titre du livre."""
        c = self.c
        # Cadre décoratif
        c.setStrokeColor(black)
        c.setLineWidth(3)
        c.rect(0.5 * inch, 0.5 * inch, self.width - 1 * inch, self.height - 1 * inch)
        c.setLineWidth(1.5)
        c.rect(0.6 * inch, 0.6 * inch, self.width - 1.2 * inch, self.height - 1.2 * inch)

        # Titre principal
        c.setFont("Helvetica-Bold", 36)
        y = self.height * 0.65
        # Découper le titre en lignes si trop long
        words = self.title.split()
        lines = []
        current_line = ""
        for word in words:
            test = current_line + " " + word if current_line else word
            if c.stringWidth(test, "Helvetica-Bold", 36) < self.width - 3 * inch:
                current_line = test
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        for line in lines:
            c.drawCentredString(self.width / 2, y, line)
            y -= 50

        # Sous-titre
        if self.subtitle:
            c.setFont("Helvetica", 18)
            c.setFillColor(grey)
            c.drawCentredString(self.width / 2, y - 20, self.subtitle)
            c.setFillColor(black)

        # Ligne décorative
        y_line = y - 60
        c.setLineWidth(2)
        c.line(self.width * 0.3, y_line, self.width * 0.7, y_line)

        # Auteur (optionnel)
        if self.author:
            c.setFont("Helvetica", 14)
            c.drawCentredString(self.width / 2, y_line - 40, self.author)

        c.showPage()

    def add_instructions_page_wordsearch(self):
        """Page d'instructions pour les mots mêlés."""
        c = self.c
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(self.width / 2, self.height - 1.5 * inch, "How to Play")
        c.setFont("Helvetica", 14)

        instructions = [
            "Find and circle each word from the word list in the grid.",
            "",
            "Words can be hidden in any direction:",
            "  • Horizontally (left to right or right to left)",
            "  • Vertically (top to bottom or bottom to top)",
            "  • Diagonally (in all four diagonal directions)",
            "",
            "Words may overlap and share letters with other words.",
            "",
            "When you find a word, circle it in the grid and",
            "cross it off the word list.",
            "",
            "Solutions are provided at the back of the book.",
            "",
            "Enjoy!",
        ]

        y = self.height - 2.5 * inch
        for line in instructions:
            c.drawString(1.5 * inch, y, line)
            y -= 24

        self._add_page_number()
        c.showPage()

    def add_instructions_page_sudoku(self):
        """Page d'instructions pour le sudoku."""
        c = self.c
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(self.width / 2, self.height - 1.5 * inch, "How to Play")
        c.setFont("Helvetica", 14)

        instructions = [
            "Fill in the grid so that every row, every column,",
            "and every 3x3 box contains the digits 1 through 9.",
            "",
            "Each digit can only appear once in each row,",
            "column, and 3x3 box.",
            "",
            "Some digits are already placed to get you started.",
            "",
            "Use logic and deduction — no guessing needed!",
            "",
            "Solutions are provided at the back of the book.",
            "",
            "Enjoy!",
        ]

        y = self.height - 2.5 * inch
        for line in instructions:
            c.drawString(1.5 * inch, y, line)
            y -= 24

        self._add_page_number()
        c.showPage()

    def add_word_search_page(self, puzzle_num, theme_name, grid, words):
        """Ajoute une page de mots mêlés."""
        c = self.c
        grid_size = len(grid)

        # Titre : numéro + thème
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(self.width / 2, self.height - self.margin - 10,
                            f"Puzzle #{puzzle_num}")
        c.setFont("Helvetica", 14)
        c.setFillColor(grey)
        c.drawCentredString(self.width / 2, self.height - self.margin - 32, theme_name)
        c.setFillColor(black)

        # Calculer la taille des cellules
        available_width = self.width - 2 * self.margin
        available_height = self.height - 2 * self.margin - 80 - 120  # 80 pour header, 120 pour word list
        cell_size = min(available_width / grid_size, available_height / grid_size)
        cell_size = min(cell_size, 30)  # Cap pour la lisibilité

        grid_width = cell_size * grid_size
        grid_height = cell_size * grid_size
        start_x = (self.width - grid_width) / 2
        start_y = self.height - self.margin - 55

        # Dessiner la grille
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)

        # Lignes horizontales et verticales
        for i in range(grid_size + 1):
            # Horizontale
            c.line(start_x, start_y - i * cell_size,
                   start_x + grid_width, start_y - i * cell_size)
            # Verticale
            c.line(start_x + i * cell_size, start_y,
                   start_x + i * cell_size, start_y - grid_height)

        # Remplir les lettres
        font_size = max(12, min(18, int(cell_size * 0.6)))
        c.setFont("Helvetica", font_size)
        c.setFillColor(black)

        for r in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size + cell_size / 2
                y = start_y - r * cell_size - cell_size / 2 - font_size * 0.3
                c.drawCentredString(x, y, grid[r][col])

        # Liste de mots (en bas, 3 colonnes)
        word_y = start_y - grid_height - 30
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(self.width / 2, word_y, "Find these words:")
        word_y -= 20

        c.setFont("Helvetica", 11)
        cols = 3
        col_width = (self.width - 2 * self.margin) / cols
        for i, word in enumerate(sorted(words)):
            col = i % cols
            row = i // cols
            x = self.margin + col * col_width + 10
            y = word_y - row * 18
            c.drawString(x, y, word)

        self._add_page_number()
        c.showPage()

    def add_word_search_solution_page(self, puzzle_num, theme_name, grid,
                                       word_positions):
        """Page de solution avec les mots surlignés."""
        c = self.c
        grid_size = len(grid)

        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(self.width / 2, self.height - self.margin - 10,
                            f"Solution — Puzzle #{puzzle_num}")
        c.setFont("Helvetica", 12)
        c.setFillColor(grey)
        c.drawCentredString(self.width / 2, self.height - self.margin - 30, theme_name)
        c.setFillColor(black)

        # Grille plus petite pour les solutions
        cell_size = min(22, (self.width - 2 * self.margin) / grid_size)
        grid_width = cell_size * grid_size
        grid_height = cell_size * grid_size
        start_x = (self.width - grid_width) / 2
        start_y = self.height - self.margin - 50

        # Collecter les positions des mots trouvés
        highlighted = set()
        for word, positions in word_positions.items():
            for pos in positions:
                highlighted.add(pos)

        # Dessiner les cellules
        for r in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size
                y = start_y - (r + 1) * cell_size

                # Surligner les cellules des mots trouvés
                if (r, col) in highlighted:
                    c.setFillColor(Color(0.85, 0.92, 1.0))
                    c.rect(x, y, cell_size, cell_size, fill=1, stroke=0)
                    c.setFillColor(black)

        # Grille
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.3)
        for i in range(grid_size + 1):
            c.line(start_x, start_y - i * cell_size,
                   start_x + grid_width, start_y - i * cell_size)
            c.line(start_x + i * cell_size, start_y,
                   start_x + i * cell_size, start_y - grid_height)
        grid_height = cell_size * grid_size

        # Lettres
        font_size = max(9, int(cell_size * 0.55))
        c.setFont("Helvetica", font_size)
        for r in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * cell_size + cell_size / 2
                y = start_y - r * cell_size - cell_size / 2 - font_size * 0.3
                c.drawCentredString(x, y, grid[r][col])

        self._add_page_number()
        c.showPage()

    def add_sudoku_page(self, puzzle_num, puzzle, difficulty):
        """Ajoute une page de sudoku."""
        c = self.c

        # Titre
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(self.width / 2, self.height - self.margin - 10,
                            f"Puzzle #{puzzle_num}")
        c.setFont("Helvetica", 14)
        c.setFillColor(grey)
        c.drawCentredString(self.width / 2, self.height - self.margin - 32,
                            f"Difficulty: {difficulty.capitalize()}")
        c.setFillColor(black)

        # Grille 9x9 centrée
        cell_size = 45
        grid_total = cell_size * 9
        start_x = (self.width - grid_total) / 2
        start_y = self.height - self.margin - 60

        # Fond blanc
        c.setFillColor(white)
        c.rect(start_x, start_y - grid_total, grid_total, grid_total, fill=1, stroke=0)
        c.setFillColor(black)

        # Lignes fines (cellules)
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        for i in range(10):
            c.line(start_x + i * cell_size, start_y,
                   start_x + i * cell_size, start_y - grid_total)
            c.line(start_x, start_y - i * cell_size,
                   start_x + grid_total, start_y - i * cell_size)

        # Lignes épaisses (blocs 3x3)
        c.setStrokeColor(black)
        c.setLineWidth(2.5)
        for i in range(4):
            c.line(start_x + i * 3 * cell_size, start_y,
                   start_x + i * 3 * cell_size, start_y - grid_total)
            c.line(start_x, start_y - i * 3 * cell_size,
                   start_x + grid_total, start_y - i * 3 * cell_size)

        # Chiffres
        c.setFont("Helvetica-Bold", 22)
        for r in range(9):
            for col in range(9):
                if puzzle[r][col] != 0:
                    x = start_x + col * cell_size + cell_size / 2
                    y = start_y - r * cell_size - cell_size / 2 - 8
                    c.drawCentredString(x, y, str(puzzle[r][col]))

        self._add_page_number()
        c.showPage()

    def add_sudoku_solution_page(self, puzzle_num, solution):
        """Page de solution sudoku."""
        c = self.c

        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(self.width / 2, self.height - self.margin - 10,
                            f"Solution — Puzzle #{puzzle_num}")

        cell_size = 35
        grid_total = cell_size * 9
        start_x = (self.width - grid_total) / 2
        start_y = self.height - self.margin - 45

        # Lignes fines
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        for i in range(10):
            c.line(start_x + i * cell_size, start_y,
                   start_x + i * cell_size, start_y - grid_total)
            c.line(start_x, start_y - i * cell_size,
                   start_x + grid_total, start_y - i * cell_size)

        # Lignes épaisses
        c.setStrokeColor(black)
        c.setLineWidth(2)
        for i in range(4):
            c.line(start_x + i * 3 * cell_size, start_y,
                   start_x + i * 3 * cell_size, start_y - grid_total)
            c.line(start_x, start_y - i * 3 * cell_size,
                   start_x + grid_total, start_y - i * 3 * cell_size)

        c.setFont("Helvetica", 16)
        for r in range(9):
            for col in range(9):
                x = start_x + col * cell_size + cell_size / 2
                y = start_y - r * cell_size - cell_size / 2 - 6
                c.drawCentredString(x, y, str(solution[r][col]))

        self._add_page_number()
        c.showPage()

    def add_solutions_divider(self):
        """Page séparatrice avant les solutions."""
        c = self.c
        c.setFont("Helvetica-Bold", 36)
        c.drawCentredString(self.width / 2, self.height / 2 + 20, "SOLUTIONS")
        c.setLineWidth(2)
        c.line(self.width * 0.3, self.height / 2 - 10,
               self.width * 0.7, self.height / 2 - 10)
        c.showPage()

    def save(self):
        self.c.save()
        print(f"[OK] PDF sauvegardé : {self.filename}")
        print(f"     {self.page_num} pages générées")


# =============================================================================
# GENERATION DES LIVRES
# =============================================================================

def generate_wordsearch_book(title, subtitle, themes_to_use, num_puzzles=50,
                              grid_size=15, output_dir="."):
    """Génère un livre complet de mots mêlés."""
    filename = os.path.join(output_dir, f"{title.replace(' ', '_')}_Interior.pdf")
    book = PuzzleBookPDF(filename, title, subtitle)
    book.add_title_page()
    book.add_instructions_page_wordsearch()

    # Stocker puzzles et solutions
    puzzles_data = []

    for i in range(1, num_puzzles + 1):
        # Choisir un thème au hasard parmi ceux sélectionnés
        theme_key = random.choice(themes_to_use)
        theme = THEMES[theme_key]

        # Sélectionner 12-15 mots du thème
        num_words = min(random.randint(12, 15), len(theme["words"]))
        selected_words = random.sample(theme["words"], num_words)

        # Générer le puzzle
        grid, placed_words, word_positions = generate_word_search(selected_words, grid_size)

        # Ajouter la page du puzzle
        book.add_word_search_page(i, theme["name"], grid, placed_words)

        # Sauvegarder pour les solutions
        puzzles_data.append({
            "num": i,
            "theme": theme["name"],
            "grid": grid,
            "word_positions": word_positions,
        })

        print(f"  Puzzle {i}/{num_puzzles} ({theme['name']}) — {len(placed_words)} mots placés")

    # Section solutions
    book.add_solutions_divider()
    for data in puzzles_data:
        book.add_word_search_solution_page(
            data["num"], data["theme"], data["grid"], data["word_positions"]
        )

    book.save()
    return filename


def generate_sudoku_book(title, subtitle, difficulty="medium", num_puzzles=50,
                          output_dir="."):
    """Génère un livre complet de sudoku."""
    filename = os.path.join(output_dir, f"{title.replace(' ', '_')}_Interior.pdf")
    book = PuzzleBookPDF(filename, title, subtitle)
    book.add_title_page()
    book.add_instructions_page_sudoku()

    puzzles_data = []

    for i in range(1, num_puzzles + 1):
        puzzle, solution = generate_sudoku(difficulty)
        book.add_sudoku_page(i, puzzle, difficulty)
        puzzles_data.append({"num": i, "solution": solution})
        print(f"  Sudoku {i}/{num_puzzles} ({difficulty})")

    # Section solutions
    book.add_solutions_divider()
    for data in puzzles_data:
        book.add_sudoku_solution_page(data["num"], data["solution"])

    book.save()
    return filename


# =============================================================================
# MAIN — point d'entrée du script
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Générateur de puzzle books pour Amazon KDP",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python generate_puzzle_book.py --type wordsearch --theme animals --title "Animal Word Search Fun"
  python generate_puzzle_book.py --type wordsearch --theme all --puzzles 80 --large-print
  python generate_puzzle_book.py --type sudoku --difficulty easy --title "Easy Sudoku for Beginners"
  python generate_puzzle_book.py --type sudoku --difficulty hard --puzzles 100
        """,
    )
    parser.add_argument("--type", choices=["wordsearch", "sudoku"], required=True,
                        help="Type de puzzle book")
    parser.add_argument("--title", type=str, default=None,
                        help="Titre du livre")
    parser.add_argument("--subtitle", type=str, default="",
                        help="Sous-titre")
    parser.add_argument("--theme", type=str, default="all",
                        help="Thème (animals, space, food, nature, sports, travel, music, ocean, science, holidays, all)")
    parser.add_argument("--puzzles", type=int, default=50,
                        help="Nombre de puzzles (défaut: 50)")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium",
                        help="Difficulté sudoku (défaut: medium)")
    parser.add_argument("--large-print", action="store_true",
                        help="Mode gros caractères (grille 12x12 au lieu de 15x15)")
    parser.add_argument("--output", type=str, default=".",
                        help="Dossier de sortie")

    args = parser.parse_args()

    print("=" * 60)
    print("GENERATEUR DE PUZZLE BOOKS KDP")
    print("=" * 60)

    if args.type == "wordsearch":
        grid_size = 12 if args.large_print else 15
        mode_label = "LARGE PRINT" if args.large_print else "Standard"

        if args.theme == "all":
            themes_to_use = list(THEMES.keys())
        else:
            if args.theme not in THEMES:
                print(f"[ERREUR] Thème inconnu: {args.theme}")
                print(f"Thèmes disponibles: {', '.join(THEMES.keys())}")
                return
            themes_to_use = [args.theme]

        title = args.title or f"Word Search Puzzle Book"
        subtitle = args.subtitle or f"{args.puzzles} Puzzles · {mode_label}"

        print(f"Type: Word Search ({mode_label})")
        print(f"Grille: {grid_size}x{grid_size}")
        print(f"Thèmes: {', '.join(themes_to_use)}")
        print(f"Puzzles: {args.puzzles}")
        print(f"Titre: {title}")
        print("-" * 60)

        filepath = generate_wordsearch_book(
            title=title,
            subtitle=subtitle,
            themes_to_use=themes_to_use,
            num_puzzles=args.puzzles,
            grid_size=grid_size,
            output_dir=args.output,
        )

    elif args.type == "sudoku":
        title = args.title or f"Sudoku Puzzle Book"
        subtitle = args.subtitle or f"{args.puzzles} Puzzles · {args.difficulty.capitalize()}"

        print(f"Type: Sudoku")
        print(f"Difficulté: {args.difficulty}")
        print(f"Puzzles: {args.puzzles}")
        print(f"Titre: {title}")
        print("-" * 60)

        filepath = generate_sudoku_book(
            title=title,
            subtitle=subtitle,
            difficulty=args.difficulty,
            num_puzzles=args.puzzles,
            output_dir=args.output,
        )

    print("=" * 60)
    print(f"TERMINE ! Le PDF est prêt pour upload sur KDP.")
    print(f"Fichier : {filepath}")
    print()
    print("Prochaines étapes :")
    print("  1. Créer la cover dans Canva (utiliser le KDP Cover Calculator)")
    print("  2. Aller sur kdp.amazon.com > Bookshelf > Create")
    print("  3. Uploader l'intérieur (ce PDF) + la cover")
    print("  4. Mettre le prix entre 6.99$ et 9.99$")
    print("  5. Publier !")
    print("=" * 60)


if __name__ == "__main__":
    main()
