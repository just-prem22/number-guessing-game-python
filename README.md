# 🎯 Number Guessing Game (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy%20%7C%20Hard-purple)
![Game Type](https://img.shields.io/badge/Game-CLI%20Based-informational)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

A fun and interactive **command-line number guessing game** built using Python.  
This project demonstrates **control flow, loops, conditional logic, and user interaction** in a clean and structured way.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🧠 Game Flow](#-game-flow-flowchart)
- [💡 Hint System](#-hint-system)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [▶️ How to Run](#️-how-to-run)
- [📸 Example Gameplay](#-example-gameplay)
- [🎯 Learning Outcomes](#-learning-outcomes)
- [🔄 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## 🚀 Features

| Feature | Description |
|--------|------------|
| Random Number | Generates a number between 1 and 100 |
| Difficulty Levels | Easy (10 lives), Hard (5 lives) |
| Smart Hints | Feedback based on guess accuracy |
| Replay Option | Play again after game ends |
| Input Handling | Interactive CLI-based input system |

---

## 🧠 Game Flow (Flowchart)

```mermaid
flowchart TD
    A[Start Game] --> B[Generate Random Number]
    B --> C[Choose Difficulty]
    C --> D[Set Lives]
    D --> E[Start Guess Loop]

    E --> F[User Enters Guess]
    F --> G{Is Guess Correct}

    G -->|Yes| H[Display Win Message]
    G -->|No| I{Lives Left}

    I -->|No| J[Game Over]
    I -->|Yes| K[Give Hint]

    K --> L[Decrease Lives]
    L --> E
