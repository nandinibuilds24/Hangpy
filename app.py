from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import json

from words import questions
from syntax_words import syntax_questions


app = Flask(__name__)

app.secret_key = "python-hangman-secret-key"


# ============================================================
# PROGRESS FILE
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROGRESS_FILE = os.path.join(
    BASE_DIR,
    "progress.json"
)


# ============================================================
# QUESTION BANKS
# ============================================================

QUESTION_BANKS = {
    "basic": questions,
    "syntax": syntax_questions
}


# ============================================================
# LOAD PROGRESS
# ============================================================

def load_progress():

    if not os.path.exists(PROGRESS_FILE):

        return {}

    try:

        with open(
            PROGRESS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return {}


# ============================================================
# SAVE PROGRESS
# ============================================================

def save_progress(progress):

    with open(
        PROGRESS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            progress,
            file,
            indent=4
        )


# ============================================================
# GET LEVEL PROGRESS
# ============================================================

def get_level_progress(category, level):

    progress = load_progress()

    key = f"{category}_{level}"

    return progress.get(
        key,
        {
            "question_index": 0,
            "score": 0,
            "completed": False
        }
    )


# ============================================================
# SAVE LEVEL PROGRESS
# ============================================================

def save_level_progress(
    category,
    level,
    question_index,
    score,
    completed=False
):

    progress = load_progress()

    key = f"{category}_{level}"

    progress[key] = {

        "question_index":
            question_index,

        "score":
            score,

        "completed":
            completed
    }

    save_progress(progress)


# ============================================================
# CLEAR LEVEL PROGRESS
# ============================================================

def clear_level_progress(
    category,
    level
):

    progress = load_progress()

    key = f"{category}_{level}"

    if key in progress:

        del progress[key]

        save_progress(progress)


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# ABOUT
# ============================================================

@app.route("/about")
def about():

    all_questions = (
        questions +
        syntax_questions
    )

    return render_template(
        "about.html",
        all_questions=all_questions
    )


# ============================================================
# LEVELS
# ============================================================

@app.route("/levels")
def levels():

    return render_template(
        "level.html"
    )


# ============================================================
# START GAME
# ============================================================

@app.route("/start-game")
@app.route("/start-game/<category>")
def start_game(category=None):

    if category is None:

        category = session.get(
            "category",
            "basic"
        )

    if category not in [
        "basic",
        "syntax"
    ]:

        return "Category not found", 404

    session["category"] = category

    return redirect(
        url_for(
            "category_levels",
            category=category
        )
    )


# ============================================================
# CATEGORY SELECTION
# ============================================================

@app.route("/category/<category>")
def category_levels(category):

    if category not in [
        "basic",
        "syntax"
    ]:

        return "Category not found", 404

    session["category"] = category

    return render_template(
        "category_selected.html",
        category=category
    )


# ============================================================
# GET QUESTION BANK
# ============================================================

def get_question_bank(category):

    return QUESTION_BANKS.get(
        category
    )


# ============================================================
# START LEVEL
# ============================================================

@app.route(
    "/game/<category>/<int:level>"
)
def category_game(
    category,
    level
):

    question_bank = get_question_bank(
        category
    )

    if question_bank is None:

        return "Question bank not available yet.", 404


    level_questions = [

        question

        for question in question_bank

        if question.get("level") == level

    ]


    if not level_questions:

        return "Level not found", 404


    # ----------------------------------------
    # GET SAVED PROGRESS
    # ----------------------------------------

    saved = get_level_progress(
        category,
        level
    )


    start_index = int(
        saved.get(
            "question_index",
            0
        )
    )


    start_score = int(
        saved.get(
            "score",
            0
        )
    )


    completed = saved.get(
        "completed",
        False
    )


    # ----------------------------------------
    # IF ALREADY COMPLETED
    # START FRESH
    # ----------------------------------------

    if completed:

        start_index = 0

        start_score = 0

        clear_level_progress(
            category,
            level
        )


    # Safety check

    if start_index >= len(
        level_questions
    ):

        start_index = 0

        start_score = 0


    # ----------------------------------------
    # SESSION
    # ----------------------------------------

    session["category"] = category

    session["level"] = level

    session["question_index"] = start_index

    session["score"] = start_score

    session["wrong_attempts"] = 0


    # ----------------------------------------
    # GAME PAGE
    # ----------------------------------------

    return render_template(

        "game.html",

        questions=level_questions,

        level=level,

        category=category,

        start_index=start_index,

        start_score=start_score

    )


# ============================================================
# OLD GAME URL
# ============================================================

@app.route("/game/<int:level>")
def old_game(level):

    category = session.get(
        "category",
        "basic"
    )

    return redirect(
        url_for(
            "category_game",
            category=category,
            level=level
        )
    )


# ============================================================
# RESULT
# ============================================================

@app.route("/result")
def result():

    level = session.get(
        "level"
    )

    category = session.get(
        "category",
        "basic"
    )

    score = session.get(
        "score",
        0
    )


    if level is None:

        return "Game not started", 400


    question_bank = get_question_bank(
        category
    )


    if question_bank is None:

        return "Question bank not available", 404


    level_questions = [

        question

        for question in question_bank

        if question.get("level") == level

    ]


    total_questions = len(
        level_questions
    )

    total_score = (
        total_questions * 10
    )


    return render_template(

        "result.html",

        level=level,

        score=score,

        total_questions=total_questions,

        total_score=total_score,

        category=category

    )


# ============================================================
# CHECK ANSWER
# ============================================================

@app.route(
    "/check-answer",
    methods=["POST"]
)
def check_answer():

    category = session.get(
        "category",
        "basic"
    )

    level = session.get(
        "level"
    )

    question_index = session.get(
        "question_index",
        0
    )

    score = session.get(
        "score",
        0
    )

    wrong_attempts = session.get(
        "wrong_attempts",
        0
    )


    if level is None:

        return jsonify({
            "error":
                "Game not started"
        }), 400


    question_bank = get_question_bank(
        category
    )


    if question_bank is None:

        return jsonify({
            "error":
                "Question bank not available"
        }), 404


    level_questions = [

        question

        for question in question_bank

        if question.get("level") == level

    ]


    if question_index >= len(
        level_questions
    ):

        return jsonify({

            "finished": True,

            "score": score

        })


    current_question = (
        level_questions[
            question_index
        ]
    )


    data = request.get_json()

    if not data:

        data = {}


    user_answer = str(
        data.get(
            "answer",
            ""
        )
    ).strip()


    correct_answer = str(
        current_question.get(
            "answer",
            ""
        )
    ).strip()


    # ========================================================
    # CORRECT
    # ========================================================

    if (
        user_answer.lower()
        ==
        correct_answer.lower()
    ):

        score += 10

        next_index = (
            question_index + 1
        )


        finished = (
            next_index >=
            len(level_questions)
        )


        session["score"] = score

        session["question_index"] = (
            next_index
        )

        session["wrong_attempts"] = 0


        # ----------------------------------------
        # SAVE PROGRESS
        # ----------------------------------------

        save_level_progress(

            category,

            level,

            next_index,

            score,

            finished

        )


        return jsonify({

            "correct": True,

            "score": score,

            "wrong_attempts": 0,

            "chances_left": 6,

            "next_question": next_index,

            "next_question_text": (

                level_questions[
                    next_index
                ]["question"]

                if next_index <
                len(level_questions)

                else None

            ),

            "finished": finished,

            "topic":
                current_question.get(
                    "topic",
                    ""
                ),

            "syntax":
                current_question.get(
                    "answer",
                    ""
                ),

            "explanation":
                current_question.get(
                    "explanation",
                    ""
                ),

            "memory_line":
                current_question.get(
                    "memory_line",
                    ""
                )

        })


    # ========================================================
    # WRONG ANSWER
    # ========================================================

    wrong_attempts += 1


    if wrong_attempts >= 6:

        session["wrong_attempts"] = 0

        return jsonify({

            "correct": False,

            "game_over": False,

            "reset_chances": True,

            "score": score,

            "wrong_attempts": 0,

            "chances_left": 6,

            "message":
                "You used all 6 chances. "
                "Try the same question again."

        })


    session["wrong_attempts"] = (
        wrong_attempts
    )


    return jsonify({

        "correct": False,

        "game_over": False,

        "score": score,

        "wrong_attempts":
            wrong_attempts,

        "chances_left":
            6 - wrong_attempts

    })


# ============================================================
# HINT
# ============================================================

@app.route("/hint")
def hint():

    category = session.get(
        "category",
        "basic"
    )

    level = session.get(
        "level"
    )

    question_index = session.get(
        "question_index",
        0
    )


    if level is None:

        return jsonify({
            "error":
                "Game not started"
        }), 400


    question_bank = get_question_bank(
        category
    )


    if question_bank is None:

        return jsonify({
            "error":
                "Question bank not available"
        }), 404


    level_questions = [

        question

        for question in question_bank

        if question.get("level") == level

    ]


    if question_index >= len(
        level_questions
    ):

        return jsonify({
            "error":
                "No question available"
        }), 400


    current_question = (
        level_questions[
            question_index
        ]
    )


    return jsonify({

        "hint":
            current_question.get(
                "hint",
                ""
            )

    })


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0", port=5000, debug=True
    )