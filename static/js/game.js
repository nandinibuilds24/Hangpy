// ============================================
// PYTHON HANGMAN - GAME.JS
// ============================================

document.addEventListener("DOMContentLoaded", function () {

    // =========================================
    // LOAD GAME DATA
    // =========================================

    const gameDataElement =
        document.getElementById("game-data");

    if (!gameDataElement) {
        console.error("Game data not found.");
        return;
    }

    const gameData =
        JSON.parse(gameDataElement.textContent);

    const questions =
        gameData.questions || [];

    const category =
        gameData.category || "basic";


    // =========================================
    // RESUME PROGRESS
    // =========================================

    let currentQuestionIndex =
        Number(gameData.start_index || 0);

    let score =
        Number(gameData.start_score || 0);

    let wrongAttempts = 0;

    let pendingNextQuestion = null;

    let gameFinished = false;


    // =========================================
    // GET ELEMENTS
    // =========================================

    const scoreElement =
        document.getElementById("score");

    const chancesElement =
        document.getElementById("chances");

    const questionNumberElement =
        document.getElementById("question-number");

    const questionElement =
        document.getElementById("question");

    const answerElement =
        document.getElementById("answer");

    const syntaxEditorContainer =
        document.getElementById(
            "syntax-editor-container"
        );

    const syntaxAnswer =
        document.getElementById("syntax-answer");

    const checkButton =
        document.getElementById("check-answer");

    const hintButton =
        document.getElementById("hint-button");

    const hintElement =
        document.getElementById("hint");

    const hangmanImage =
        document.getElementById("hangman-image");

    const gameMessage =
        document.getElementById("game-message");

    const celebration =
        document.getElementById("celebration");

    const learningScreen =
        document.getElementById("learning-screen");

    const learningTopic =
        document.getElementById("learning-topic");

    const learningExplanation =
        document.getElementById(
            "learning-explanation"
        );

    const learningMemory =
        document.getElementById(
            "learning-memory"
        );

    const doneLearning =
        document.getElementById(
            "done-learning"
        );


    // =========================================
    // INITIAL DISPLAY
    // =========================================

    scoreElement.textContent = score;

    chancesElement.textContent = 6;

    updateQuestion();


    // =========================================
    // UPDATE QUESTION
    // =========================================

    function updateQuestion() {

        if (
            currentQuestionIndex >=
            questions.length
        ) {

            finishGame();

            return;
        }


        const currentQuestion =
            questions[currentQuestionIndex];


        // Question

        questionElement.textContent =
            currentQuestion.question;


        // Question number

        questionNumberElement.textContent =
            `${currentQuestionIndex + 1} / ${questions.length}`;


        // Reset answer

        if (answerElement) {
            answerElement.value = "";
            answerElement.disabled = false;
        }


        if (syntaxAnswer) {
            syntaxAnswer.value = "";
            syntaxAnswer.disabled = false;
        }


        // Reset chances

        wrongAttempts = 0;

        chancesElement.textContent = 6;


        // Reset hint

        hintElement.textContent = "";


        // Reset message

        if (gameMessage) {
            gameMessage.textContent = "";
            gameMessage.className =
                "game-message";
        }


        // Reset Hangman image

        if (hangmanImage) {

            hangmanImage.src =
                "/static/images/stage1.png";

        }


        // =====================================
        // BASIC / SYNTAX INPUT
        // =====================================

        if (category === "syntax") {

            if (syntaxEditorContainer) {
                syntaxEditorContainer.style.display =
                    "block";
            }

            if (answerElement) {
                answerElement.style.display =
                    "none";
            }

            if (syntaxAnswer) {
                syntaxAnswer.focus();
            }

        } else {

            if (syntaxEditorContainer) {
                syntaxEditorContainer.style.display =
                    "none";
            }

            if (answerElement) {
                answerElement.style.display =
                    "block";
                answerElement.focus();
            }

        }

    }


    // =========================================
    // HANGMAN IMAGE
    // =========================================

    function updateHangman() {

        if (!hangmanImage) {
            return;
        }


        const stage =
            Math.min(
                wrongAttempts + 1,
                6
            );


        hangmanImage.src =
            `/static/images/stage${stage}.png`;

    }


    // =========================================
    // GET USER ANSWER
    // =========================================

    function getUserAnswer() {

        if (category === "syntax") {

            if (!syntaxAnswer) {
                return "";
            }

            return syntaxAnswer.value.trim();

        }


        if (!answerElement) {
            return "";
        }


        return answerElement.value.trim();

    }


    // =========================================
    // CHECK ANSWER
    // =========================================

    async function checkAnswer() {

        if (gameFinished) {
            return;
        }


        const userAnswer =
            getUserAnswer();


        if (!userAnswer) {

            showMessage(
                "⚠️ Please enter an answer."
            );

            return;
        }


        checkButton.disabled = true;


        try {

            const response =
                await fetch(
                    "/check-answer",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            answer: userAnswer
                        })
                    }
                );


            const data =
                await response.json();


            // =================================
            // CORRECT ANSWER
            // =================================

            if (data.correct) {

                score =
                    Number(data.score);


                scoreElement.textContent =
                    score;


                wrongAttempts = 0;

                chancesElement.textContent =
                    6;


                updateHangman();


                pendingNextQuestion =
                    data.next_question;


                showLearningScreen(data);


                return;
            }


            // =================================
            // SIX CHANCES USED
            // =================================

            if (data.reset_chances) {

                wrongAttempts = 0;

                chancesElement.textContent =
                    6;


                updateHangman();


                showMessage(
                    "😮 You used all 6 chances! Try the same question again."
                );


                if (answerElement) {
                    answerElement.value = "";
                }


                if (syntaxAnswer) {
                    syntaxAnswer.value = "";
                }


                return;
            }


            // =================================
            // WRONG ANSWER
            // =================================

            wrongAttempts =
                Number(
                    data.wrong_attempts || 0
                );


            chancesElement.textContent =
                data.chances_left;


            updateHangman();


            showMessage(
                `❌ Wrong answer! ${data.chances_left} chances left.`
            );


        }

        catch (error) {

            console.error(
                "Error checking answer:",
                error
            );


            showMessage(
                "⚠️ Something went wrong. Please try again."
            );

        }

        finally {

            checkButton.disabled = false;

        }

    }


    // =========================================
    // LEARNING SCREEN
    // =========================================

    function showLearningScreen(data) {

        if (learningTopic) {

            learningTopic.textContent =
                data.topic || "";

        }


        if (learningExplanation) {

            learningExplanation.textContent =
                data.explanation || "";

        }


        if (learningMemory) {

            learningMemory.textContent =
                data.memory_line || "";

        }


        if (data.finished) {

            gameFinished = true;

            doneLearning.textContent =
                "SEE RESULT →";

        } else {

            doneLearning.textContent =
                "NEXT QUESTION →";

        }


        learningScreen.classList.add(
            "show"
        );


        if (celebration) {

            celebration.textContent =
                "🎉";

            celebration.classList.add(
                "show"
            );

        }

    }


    // =========================================
    // NEXT QUESTION
    // =========================================

    function nextQuestion() {

        learningScreen.classList.remove(
            "show"
        );


        if (celebration) {

            celebration.classList.remove(
                "show"
            );

            celebration.textContent = "";

        }


        // Level completed

        if (gameFinished) {

            window.location.href =
                "/result";

            return;
        }


        // Move to next question

        if (
            pendingNextQuestion !== null &&
            pendingNextQuestion !== undefined
        ) {

            currentQuestionIndex =
                Number(
                    pendingNextQuestion
                );

        } else {

            currentQuestionIndex++;

        }


        pendingNextQuestion = null;


        updateQuestion();

    }


    // =========================================
    // HINT
    // =========================================

    async function showHint() {

        try {

            const response =
                await fetch("/hint");


            const data =
                await response.json();


            if (data.hint) {

                hintElement.textContent =
                    `💡 ${data.hint}`;

            } else {

                hintElement.textContent =
                    "No hint available.";

            }

        }

        catch (error) {

            console.error(
                "Error loading hint:",
                error
            );


            hintElement.textContent =
                "⚠️ Unable to load hint.";

        }

    }


    // =========================================
    // SHOW MESSAGE
    // =========================================

    function showMessage(message) {

        if (!gameMessage) {
            return;
        }


        gameMessage.textContent =
            message;


        gameMessage.className =
            "game-message show";


        setTimeout(
            function () {

                gameMessage.className =
                    "game-message";

            },
            2500
        );

    }


    // =========================================
    // FINISH GAME
    // =========================================

    function finishGame() {

        gameFinished = true;


        if (questionElement) {

            questionElement.textContent =
                "🎉 Level completed!";

        }


        if (questionNumberElement) {

            questionNumberElement.textContent =
                `${questions.length} / ${questions.length}`;

        }


        if (checkButton) {
            checkButton.disabled = true;
        }


        if (answerElement) {
            answerElement.disabled = true;
        }


        if (syntaxAnswer) {
            syntaxAnswer.disabled = true;
        }

    }


    // =========================================
    // BUTTON EVENTS
    // =========================================

    if (checkButton) {

        checkButton.addEventListener(
            "click",
            checkAnswer
        );

    }


    if (hintButton) {

        hintButton.addEventListener(
            "click",
            showHint
        );

    }


    if (doneLearning) {

        doneLearning.addEventListener(
            "click",
            nextQuestion
        );

    }


    // =========================================
    // ENTER KEY - BASIC
    // =========================================

    if (answerElement) {

        answerElement.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key === "Enter"
                ) {

                    event.preventDefault();

                    checkAnswer();

                }

            }
        );

    }


    // =========================================
    // CTRL + ENTER - SYNTAX
    // =========================================

    if (syntaxAnswer) {

        syntaxAnswer.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key === "Enter" &&
                    event.ctrlKey
                ) {

                    event.preventDefault();

                    checkAnswer();

                }

            }
        );

    }

});