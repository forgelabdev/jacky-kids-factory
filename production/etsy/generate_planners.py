"""
GENERATEUR DE PLANNERS PDF POUR ETSY
=====================================
Produit des planners imprimables (budget, quotidien, fitness, meal) en PDF.

Usage:
    python generate_planners.py --type budget --title "Monthly Budget Planner"
    python generate_planners.py --type daily --title "Daily Planner"
    python generate_planners.py --type fitness --title "Fitness Planner"
    python generate_planners.py --type meal --title "Weekly Meal Planner"
    python generate_planners.py --type all  (génère les 4)

Prérequis:
    pip install reportlab

Exécuter depuis : C:\\Users\\zapk\\OneDrive\\Jacky\\production\\etsy\\
"""

import argparse
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import (
    Color, black, white, lightgrey, grey, HexColor
)

# =============================================================================
# COULEURS & STYLE
# =============================================================================

ACCENT = HexColor("#2C3E50")       # Bleu foncé élégant
ACCENT_LIGHT = HexColor("#BDC3C7")  # Gris clair
LINE_COLOR = HexColor("#D5D8DC")    # Gris très clair pour les lignes
HEADER_BG = HexColor("#F2F3F4")     # Fond header ultra léger


class PlannerPDF:
    """Base class pour tous les planners."""

    def __init__(self, filename, title, subtitle="Undated · Print & Use"):
        self.filename = filename
        self.title = title
        self.subtitle = subtitle
        self.c = canvas.Canvas(filename, pagesize=letter)
        self.w, self.h = letter  # 612 x 792
        self.margin = 0.6 * inch
        self.page_num = 0

    def _footer(self):
        self.page_num += 1
        self.c.setFont("Helvetica", 8)
        self.c.setFillColor(ACCENT_LIGHT)
        self.c.drawCentredString(self.w / 2, 0.4 * inch, f"— {self.page_num} —")
        self.c.setFillColor(black)

    def _title_page(self):
        c = self.c
        # Fond blanc, cadre fin
        c.setStrokeColor(ACCENT)
        c.setLineWidth(2)
        c.rect(0.4 * inch, 0.4 * inch, self.w - 0.8 * inch, self.h - 0.8 * inch)

        # Ligne décorative au-dessus du titre
        y_center = self.h * 0.58
        c.setStrokeColor(ACCENT_LIGHT)
        c.setLineWidth(1)
        c.line(self.w * 0.2, y_center + 50, self.w * 0.8, y_center + 50)

        # Titre
        c.setFont("Helvetica-Bold", 32)
        c.setFillColor(ACCENT)
        # Wrap title
        words = self.title.split()
        lines = []
        current = ""
        for word in words:
            test = current + " " + word if current else word
            if c.stringWidth(test, "Helvetica-Bold", 32) < self.w - 2.5 * inch:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)

        y = y_center
        for line in lines:
            c.drawCentredString(self.w / 2, y, line)
            y -= 42

        # Sous-titre
        c.setFont("Helvetica", 14)
        c.setFillColor(grey)
        c.drawCentredString(self.w / 2, y - 20, self.subtitle)

        # Ligne décorative en dessous
        c.setStrokeColor(ACCENT_LIGHT)
        c.line(self.w * 0.2, y - 50, self.w * 0.8, y - 50)

        c.setFillColor(black)
        c.showPage()

    def _section_header(self, text, y=None):
        """Dessine un header de section."""
        c = self.c
        if y is None:
            y = self.h - self.margin
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, text)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.5)
        c.line(self.margin, y - 5, self.w - self.margin, y - 5)
        c.setFillColor(black)
        return y - 25

    def _draw_lines(self, start_y, num_lines, spacing=22):
        """Dessine des lignes horizontales (pour écrire)."""
        c = self.c
        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(0.5)
        for i in range(num_lines):
            y = start_y - i * spacing
            c.line(self.margin, y, self.w - self.margin, y)
        return start_y - num_lines * spacing

    def _draw_table(self, x, y, headers, rows, col_widths, row_height=22):
        """Dessine un tableau simple."""
        c = self.c
        total_width = sum(col_widths)

        # Header
        c.setFillColor(HEADER_BG)
        c.rect(x, y - row_height, total_width, row_height, fill=1, stroke=0)
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 9)
        cx = x
        for i, header in enumerate(headers):
            c.drawString(cx + 4, y - row_height + 6, header)
            cx += col_widths[i]

        # Lignes du tableau
        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(0.5)
        c.setFillColor(black)
        c.setFont("Helvetica", 9)

        for r in range(rows):
            ry = y - (r + 2) * row_height
            c.line(x, ry + row_height, x + total_width, ry + row_height)

        # Lignes verticales
        cx = x
        for w in col_widths:
            c.line(cx, y, cx, y - (rows + 1) * row_height)
            cx += w
        c.line(cx, y, cx, y - (rows + 1) * row_height)

        # Ligne du bas
        c.line(x, y - (rows + 1) * row_height, x + total_width, y - (rows + 1) * row_height)
        # Ligne du haut
        c.line(x, y, x + total_width, y)

        return y - (rows + 1) * row_height

    def _checkbox_row(self, x, y, text, box_size=10):
        """Dessine une ligne avec checkbox."""
        c = self.c
        c.setStrokeColor(ACCENT_LIGHT)
        c.setLineWidth(0.8)
        c.rect(x, y - 2, box_size, box_size, fill=0)
        c.setFont("Helvetica", 10)
        c.setFillColor(black)
        c.drawString(x + box_size + 6, y, text)

    def save(self):
        self.c.save()
        print(f"[OK] Planner sauvegardé : {self.filename}")
        print(f"     {self.page_num} pages")


# =============================================================================
# BUDGET PLANNER
# =============================================================================

class BudgetPlanner(PlannerPDF):

    def generate(self):
        self._title_page()
        self._annual_overview()
        for month_num in range(1, 13):
            self._monthly_budget_page(month_num)
            self._expense_tracker_page(month_num)
        self._savings_tracker()
        self._notes_pages(4)
        self.save()

    def _annual_overview(self):
        c = self.c
        y = self._section_header("Annual Overview")

        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                   "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

        headers = ["MONTH", "INCOME", "EXPENSES", "SAVINGS", "NOTES"]
        col_widths = [60, 100, 100, 100, 130]

        self._draw_table(self.margin, y, headers, 12, col_widths, row_height=24)

        # Pré-remplir les noms de mois
        c.setFont("Helvetica", 9)
        for i, month in enumerate(months):
            c.drawString(self.margin + 4, y - (i + 2) * 24 + 8, month)

        self._footer()
        c.showPage()

    def _monthly_budget_page(self, month_num):
        c = self.c
        month_names = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
        month_name = month_names[month_num - 1]

        y = self._section_header(f"{month_name} — Budget")

        # Section Revenus
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "INCOME")
        c.setFillColor(black)
        y -= 8

        headers = ["SOURCE", "EXPECTED", "ACTUAL", "DIFFERENCE"]
        col_widths = [150, 100, 100, 140]
        y = self._draw_table(self.margin, y, headers, 5, col_widths)

        y -= 20

        # Section Dépenses
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "EXPENSES")
        c.setFillColor(black)
        y -= 8

        headers = ["CATEGORY", "BUDGET", "ACTUAL", "DIFFERENCE"]
        expense_rows = [
            "Housing / Rent", "Utilities", "Groceries", "Transportation",
            "Insurance", "Subscriptions", "Entertainment", "Dining Out",
            "Health / Medical", "Clothing", "Personal Care", "Other"
        ]
        y = self._draw_table(self.margin, y, headers, len(expense_rows), col_widths)

        # Pré-remplir catégories
        c.setFont("Helvetica", 9)
        for i, cat in enumerate(expense_rows):
            table_y_start = y + (len(expense_rows) + 1) * 22
            c.drawString(self.margin + 4, table_y_start - (i + 2) * 22 + 6, cat)

        # Totaux
        y -= 15
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "TOTAL INCOME: __________")
        c.drawString(self.w / 2, y, "TOTAL EXPENSES: __________")
        y -= 20
        c.drawString(self.margin, y, "NET SAVINGS: __________")
        c.setFillColor(black)

        self._footer()
        c.showPage()

    def _expense_tracker_page(self, month_num):
        c = self.c
        month_names = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]

        y = self._section_header(f"{month_names[month_num - 1]} — Expense Tracker")

        headers = ["DATE", "DESCRIPTION", "CATEGORY", "AMOUNT", "PAID"]
        col_widths = [55, 165, 100, 80, 90]
        self._draw_table(self.margin, y, headers, 28, col_widths, row_height=20)

        self._footer()
        c.showPage()

    def _savings_tracker(self):
        c = self.c
        y = self._section_header("Savings Goals Tracker")

        # 3 objectifs d'épargne
        for goal_num in range(1, 4):
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(ACCENT)
            c.drawString(self.margin, y, f"Goal #{goal_num}: ___________________________")
            c.setFillColor(black)
            y -= 18

            c.setFont("Helvetica", 10)
            c.drawString(self.margin, y, "Target Amount: __________   Deadline: __________   Current: __________")
            y -= 18

            # Barre de progression (visuelle)
            c.setStrokeColor(ACCENT_LIGHT)
            c.setLineWidth(1)
            bar_width = self.w - 2 * self.margin
            c.rect(self.margin, y - 5, bar_width, 15, fill=0)
            # Graduations 10% / 25% / 50% / 75% / 100%
            c.setFont("Helvetica", 7)
            for pct in [10, 25, 50, 75, 100]:
                x_mark = self.margin + bar_width * pct / 100
                c.line(x_mark, y - 5, x_mark, y + 10)
                c.drawCentredString(x_mark, y - 15, f"{pct}%")

            y -= 40

            # Tableau de suivi
            headers = ["DATE", "DEPOSIT", "WITHDRAWAL", "BALANCE"]
            col_widths = [80, 120, 120, 170]
            y = self._draw_table(self.margin, y, headers, 5, col_widths, row_height=20)
            y -= 25

        self._footer()
        c.showPage()

    def _notes_pages(self, num_pages):
        for _ in range(num_pages):
            y = self._section_header("Notes")
            self._draw_lines(y, 28, spacing=24)
            self._footer()
            self.c.showPage()


# =============================================================================
# DAILY PLANNER
# =============================================================================

class DailyPlanner(PlannerPDF):

    def generate(self):
        self._title_page()
        # 60 daily pages (2 mois d'utilisation)
        for day in range(1, 61):
            self._daily_page(day)
        # 8 weekly review pages
        for week in range(1, 9):
            self._weekly_review(week)
        self._habit_tracker()
        self._notes_pages(4)
        self.save()

    def _daily_page(self, day_num):
        c = self.c

        # Header
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, self.h - self.margin, f"Day {day_num}")
        c.setFont("Helvetica", 10)
        c.setFillColor(grey)
        c.drawRightString(self.w - self.margin, self.h - self.margin,
                           "Date: ___/___/______")
        c.setFillColor(black)

        c.setStrokeColor(ACCENT)
        c.setLineWidth(1)
        y = self.h - self.margin - 8
        c.line(self.margin, y, self.w - self.margin, y)
        y -= 20

        # Section : Top 3 Priorities
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "TOP 3 PRIORITIES")
        c.setFillColor(black)
        y -= 18

        for i in range(3):
            self._checkbox_row(self.margin, y, f"  {i+1}. _____________________________________________")
            y -= 20

        y -= 10

        # Section gauche : Schedule / Section droite : To-Do
        mid_x = self.w / 2 - 10

        # Schedule (gauche)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "SCHEDULE")
        c.setFillColor(black)
        y_schedule = y - 15

        c.setFont("Helvetica", 9)
        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(0.5)
        hours = ["6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00",
                 "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00"]

        for i, hour in enumerate(hours):
            hy = y_schedule - i * 22
            c.setFillColor(grey)
            c.drawString(self.margin, hy, hour)
            c.setFillColor(black)
            c.line(self.margin + 35, hy - 3, mid_x - 15, hy - 3)

        # To-Do list (droite)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(ACCENT)
        c.drawString(mid_x + 10, y, "TO-DO LIST")
        c.setFillColor(black)
        y_todo = y - 15

        for i in range(15):
            self._checkbox_row(mid_x + 10, y_todo - i * 22,
                                "________________________________")

        # Notes en bas
        y_bottom = y_schedule - 15 * 22 - 15
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y_bottom, "NOTES / GRATITUDE")
        c.setFillColor(black)
        self._draw_lines(y_bottom - 15, 3, spacing=22)

        self._footer()
        c.showPage()

    def _weekly_review(self, week_num):
        c = self.c
        y = self._section_header(f"Weekly Review — Week {week_num}")

        sections = [
            ("WINS THIS WEEK", 4),
            ("CHALLENGES / LESSONS", 4),
            ("GOALS FOR NEXT WEEK", 5),
            ("GRATITUDE", 3),
        ]

        for section_title, num_lines in sections:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColor(ACCENT)
            c.drawString(self.margin, y, section_title)
            c.setFillColor(black)
            y -= 12
            y = self._draw_lines(y, num_lines, spacing=22)
            y -= 15

        self._footer()
        c.showPage()

    def _habit_tracker(self):
        c = self.c
        y = self._section_header("Habit Tracker")

        # Tableau 31 jours x 10 habitudes
        c.setFont("Helvetica", 7)
        cell = 14
        start_x = self.margin + 100  # Espace pour les noms d'habitudes
        start_y = y - 5

        # Headers (jours 1-31)
        c.setFillColor(ACCENT)
        for day in range(1, 32):
            c.drawCentredString(start_x + (day - 1) * cell + cell / 2,
                                 start_y + 3, str(day))
        c.setFillColor(black)

        # Lignes pour 10 habitudes
        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(0.3)
        for row in range(10):
            ry = start_y - (row + 1) * cell * 1.8
            # Label
            c.setFont("Helvetica", 9)
            c.drawString(self.margin, ry + cell / 2, f"Habit {row + 1}: ________")
            # Cellules
            for day in range(31):
                cx = start_x + day * cell
                c.rect(cx, ry, cell, cell, fill=0)

        self._footer()
        c.showPage()

    def _notes_pages(self, num_pages):
        for _ in range(num_pages):
            y = self._section_header("Notes")
            self._draw_lines(y, 28, spacing=24)
            self._footer()
            self.c.showPage()


# =============================================================================
# MEAL PLANNER
# =============================================================================

class MealPlanner(PlannerPDF):

    def generate(self):
        self._title_page()
        # 12 semaines de meal planning
        for week in range(1, 13):
            self._weekly_meal_page(week)
            self._grocery_list_page(week)
        self._favorite_recipes_page()
        self._notes_pages(4)
        self.save()

    def _weekly_meal_page(self, week_num):
        c = self.c
        y = self._section_header(f"Week {week_num} — Meal Plan")

        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        meals = ["Breakfast", "Lunch", "Dinner", "Snacks"]

        # Header row
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(ACCENT)
        col_width = (self.w - 2 * self.margin - 75) / len(meals)
        c.drawString(self.margin + 4, y + 3, "DAY")
        for i, meal in enumerate(meals):
            c.drawString(self.margin + 75 + i * col_width + 4, y + 3, meal.upper())

        c.setFillColor(black)
        row_height = 70

        c.setStrokeColor(LINE_COLOR)
        c.setLineWidth(0.5)

        for d, day in enumerate(days):
            ry = y - (d + 1) * row_height + row_height

            # Fond alternant
            if d % 2 == 0:
                c.setFillColor(HexColor("#FAFAFA"))
                c.rect(self.margin, ry - row_height, self.w - 2 * self.margin,
                       row_height, fill=1, stroke=0)
                c.setFillColor(black)

            # Nom du jour (vertical center)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(ACCENT)
            c.drawString(self.margin + 4, ry - row_height / 2 - 4, day)
            c.setFillColor(black)

            # Lignes verticales et cadre
            c.line(self.margin, ry, self.w - self.margin, ry)
            c.line(self.margin + 75, ry, self.margin + 75, ry - row_height)
            for i in range(1, len(meals)):
                cx = self.margin + 75 + i * col_width
                c.line(cx, ry, cx, ry - row_height)

        # Dernière ligne horizontale
        c.line(self.margin, y - len(days) * row_height, self.w - self.margin,
               y - len(days) * row_height)
        # Bordures extérieures
        c.line(self.margin, y, self.margin, y - len(days) * row_height)
        c.line(self.w - self.margin, y, self.w - self.margin, y - len(days) * row_height)

        self._footer()
        c.showPage()

    def _grocery_list_page(self, week_num):
        c = self.c
        y = self._section_header(f"Week {week_num} — Grocery List")

        categories = [
            "Fruits & Vegetables", "Meat & Protein",
            "Dairy & Eggs", "Grains & Bread",
            "Pantry Staples", "Frozen", "Beverages", "Other"
        ]

        col_width = (self.w - 2 * self.margin - 20) / 2
        items_per_cat = 6

        for i, cat in enumerate(categories):
            col = i % 2
            row = i // 2

            x = self.margin + col * (col_width + 20)
            cat_y = y - row * (items_per_cat * 16 + 30)

            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(ACCENT)
            c.drawString(x, cat_y, cat.upper())
            c.setFillColor(black)

            for j in range(items_per_cat):
                self._checkbox_row(x, cat_y - 16 - j * 16,
                                    " ___________________")

        self._footer()
        c.showPage()

    def _favorite_recipes_page(self):
        c = self.c
        y = self._section_header("Favorite Recipes")

        for i in range(4):
            c.setFont("Helvetica-Bold", 11)
            c.drawString(self.margin, y, f"Recipe {i + 1}: _________________________________")
            y -= 18

            c.setFont("Helvetica", 9)
            c.setFillColor(grey)
            c.drawString(self.margin, y, "Ingredients:")
            c.setFillColor(black)
            y -= 14
            y = self._draw_lines(y, 3, spacing=16)
            y -= 5
            c.setFillColor(grey)
            c.drawString(self.margin, y, "Instructions:")
            c.setFillColor(black)
            y -= 14
            y = self._draw_lines(y, 3, spacing=16)
            y -= 20

        self._footer()
        c.showPage()

    def _notes_pages(self, num_pages):
        for _ in range(num_pages):
            y = self._section_header("Notes")
            self._draw_lines(y, 28, spacing=24)
            self._footer()
            self.c.showPage()


# =============================================================================
# FITNESS PLANNER
# =============================================================================

class FitnessPlanner(PlannerPDF):

    def generate(self):
        self._title_page()
        self._goals_page()
        self._body_measurements()
        # 12 semaines de workout logs
        for week in range(1, 13):
            self._workout_log(week)
        self._progress_photos_page()
        self._notes_pages(4)
        self.save()

    def _goals_page(self):
        c = self.c
        y = self._section_header("My Fitness Goals")

        goals = [
            "30-Day Goal",
            "60-Day Goal",
            "90-Day Goal",
            "6-Month Goal",
            "1-Year Goal",
        ]

        for goal in goals:
            c.setFont("Helvetica-Bold", 12)
            c.setFillColor(ACCENT)
            c.drawString(self.margin, y, goal)
            c.setFillColor(black)
            y -= 15
            y = self._draw_lines(y, 2, spacing=20)
            y -= 20

        # Motivation section
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(ACCENT)
        c.drawString(self.margin, y, "WHY I STARTED")
        c.setFillColor(black)
        y -= 15
        y = self._draw_lines(y, 5, spacing=22)

        self._footer()
        c.showPage()

    def _body_measurements(self):
        c = self.c
        y = self._section_header("Body Measurements Tracker")

        headers = ["DATE", "WEIGHT", "CHEST", "WAIST", "HIPS", "ARMS", "THIGHS", "NOTES"]
        col_widths = [55, 55, 50, 50, 50, 50, 55, 125]
        self._draw_table(self.margin, y, headers, 20, col_widths, row_height=22)

        self._footer()
        c.showPage()

    def _workout_log(self, week_num):
        c = self.c
        y = self._section_header(f"Week {week_num} — Workout Log")

        days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]
        exercises_per_day = 4

        for d, day in enumerate(days):
            c.setFont("Helvetica-Bold", 10)
            c.setFillColor(ACCENT)
            c.drawString(self.margin, y, f"{day}  —  Date: ________  Type: ________________")
            c.setFillColor(black)
            y -= 12

            headers = ["EXERCISE", "SETS", "REPS", "WEIGHT", "NOTES"]
            col_widths = [140, 50, 50, 60, 190]
            y = self._draw_table(self.margin, y, headers, exercises_per_day,
                                  col_widths, row_height=16)
            y -= 12

        self._footer()
        c.showPage()

    def _progress_photos_page(self):
        c = self.c
        y = self._section_header("Progress Photos Reference")

        c.setFont("Helvetica", 11)
        c.drawString(self.margin, y,
                     "Take photos on the same day each week. Paste or note them here.")
        y -= 25

        # 6 boxes pour les photos
        box_w = (self.w - 2 * self.margin - 30) / 3
        box_h = 200

        for row in range(2):
            for col in range(3):
                x = self.margin + col * (box_w + 15)
                by = y - row * (box_h + 40)
                c.setStrokeColor(ACCENT_LIGHT)
                c.setLineWidth(1)
                c.setDash(3, 3)
                c.rect(x, by - box_h, box_w, box_h)
                c.setDash()
                c.setFont("Helvetica", 9)
                c.setFillColor(grey)
                label = f"Week {row * 3 + col + 1}"
                c.drawCentredString(x + box_w / 2, by - box_h - 12, label)
                c.drawCentredString(x + box_w / 2, by - box_h / 2,
                                     "Paste photo here")
                c.setFillColor(black)

        self._footer()
        c.showPage()

    def _notes_pages(self, num_pages):
        for _ in range(num_pages):
            y = self._section_header("Notes")
            self._draw_lines(y, 28, spacing=24)
            self._footer()
            self.c.showPage()


# =============================================================================
# MAIN
# =============================================================================

PLANNER_TYPES = {
    "budget": (BudgetPlanner, "Monthly Budget Planner", "Track Your Finances · Undated"),
    "daily": (DailyPlanner, "Daily Planner", "Organize Your Day · Undated"),
    "meal": (MealPlanner, "Weekly Meal Planner", "Plan · Shop · Cook · Repeat"),
    "fitness": (FitnessPlanner, "Fitness Planner", "12-Week Workout & Progress Tracker"),
}


def main():
    parser = argparse.ArgumentParser(
        description="Générateur de planners PDF pour Etsy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python generate_planners.py --type budget
  python generate_planners.py --type daily --title "My Daily Organizer"
  python generate_planners.py --type all --output ./planners/
        """,
    )
    parser.add_argument("--type", choices=list(PLANNER_TYPES.keys()) + ["all"],
                        required=True, help="Type de planner")
    parser.add_argument("--title", type=str, default=None, help="Titre personnalisé")
    parser.add_argument("--output", type=str, default=".", help="Dossier de sortie")

    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    types_to_generate = list(PLANNER_TYPES.keys()) if args.type == "all" else [args.type]

    for ptype in types_to_generate:
        cls, default_title, default_subtitle = PLANNER_TYPES[ptype]
        title = args.title if (args.title and len(types_to_generate) == 1) else default_title
        filename = os.path.join(args.output, f"{title.replace(' ', '_')}.pdf")

        print(f"\nGénération : {title}")
        print(f"  Type: {ptype}")
        print(f"  Fichier: {filename}")

        planner = cls(filename, title, default_subtitle)
        planner.generate()

    print("\n" + "=" * 60)
    print("TERMINE ! Les planners sont prêts pour upload sur Etsy.")
    print("=" * 60)


if __name__ == "__main__":
    main()
