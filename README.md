# 📚 English Fill-in-the-Blank Game

A fun and interactive English learning game built with Python and Tkinter! This application helps users practice English grammar and vocabulary through fill-in-the-blank exercises.

## ✨ Features

- 🎮 **Interactive Quiz Game** - Answer fill-in-the-blank questions
- 📊 **Detailed Score Report** - View your performance with detailed feedback
- 🖼️ **Image Support** - Display images to illustrate each question
- ⏱️ **Auto-progressing** - Questions automatically advance after answering
- 🔄 **Restart Function** - Play the game multiple times
- 🎯 **Progress Tracking** - See which question you're on
- 💾 **Answer History** - Review all your answers and correct answers

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sonviplm1-ops/english-game.git
   cd english-game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📋 Usage

1. Launch the game by running `python main.py`
2. Read the fill-in-the-blank question
3. Type your answer in the input field
4. Press **Submit** button or press **Enter** key
5. The game will automatically move to the next question after 1.5 seconds
6. After completing all questions, click **View Results** to see detailed feedback
7. Click **Restart** to play again with shuffled questions

## 📝 Adding Custom Questions

Edit `questions.json` to add your own questions:

```json
[
  { 
    "sentence": "I ___ to school every day.", 
    "answer": "go"
  },
  { 
    "sentence": "She ___ TV now.", 
    "answer": "is watching"
  }
]
```

### Adding Images to Questions

1. Create an `images/` folder in the project directory
2. Add your image files (PNG, JPG, JPEG)
3. Update `questions.json` with image paths:

```json
[
  { 
    "sentence": "I ___ to school every day.", 
    "answer": "go",
    "image": "images/school.jpg"
  }
]
```

## 📁 Project Structure

```
english-game/
├── main.py              # Main application file
├── questions.json       # Questions database
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
├── README.md           # This file
└── images/             # Folder for question images
    ├── school.jpg
    ├── coffee.jpg
    └── ...
```

## 🎨 GUI Components

- **Title** - "Fill in the Blank" header
- **Progress Bar** - Shows current question number
- **Image Display Area** - Shows illustration for each question
- **Question Label** - Displays the fill-in-the-blank sentence
- **Input Field** - Where users type their answer
- **Buttons**:
  - **Submit** - Check the answer
  - **View Results** - Show detailed results summary
  - **Restart** - Reset and play again
- **Result Label** - Shows if answer is correct or displays the correct answer
- **Score Label** - Displays current score

## 📊 Results Summary

After completing the game, you can view:
- Total score and percentage
- Each question with your answer
- Whether your answer was correct (green) or incorrect (red)
- The correct answer if you made a mistake

## 🔧 Customization

### Change Colors
Edit the color codes in `main.py`:
- `#f0f0f0` - Background color
- `#4CAF50` - Submit button (green)
- `#2196F3` - View Results button (blue)
- `#FF9800` - Restart button (orange)

### Change Font Size
Modify font tuples in the code:
```python
font=("Arial", 14, "bold")
```

## 📦 Dependencies

- **Pillow** (10.1.0) - For image handling

## 🐛 Troubleshooting

### Images not showing?
- Ensure the `images/` folder exists
- Check that image file paths in `questions.json` are correct
- Verify image files are in supported formats (PNG, JPG, JPEG)

### Entry field not responding?
- Make sure you're clicking on the entry field before typing
- Use Enter key or Submit button to submit your answer

### Questions not shuffling?
- The game shuffles questions on startup
- Restart the game to get a new shuffle order

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**sonviplm1-ops**

## 🙏 Contributing

Feel free to:
- Add more questions
- Improve the UI
- Add new features
- Report bugs

Fork the repository and submit a pull request!

## 📧 Contact

If you have any questions or suggestions, feel free to open an issue on GitHub.

---

**Happy Learning! 📚✨**
