# fun-with-ai

# Wordle

Wordle is a simple command line interface (CLI) guessing game where the user has to guess a five-letter word in six attempts. The game provides feedback to the user about the letters in their guess and annotates their guess with correct letters and correct letters in the correct position.

## How to Play

To play Wordle, clone this repository and run the `wordle.py` script in your terminal:

```
$ git clone https://github.com/[username]/wordle.git
$ cd wordle
$ python wordle.py
```
The game will generate a random five-letter word from a predetermined list of words and prompt the user to guess the word. The user has six chances to guess the word correctly. If they guess correctly, the program tells them they won and how many guesses it took. If they run out of guesses, the program tells them they lost and what the correct word was.

## Customizing the Word List

The list of words that the game uses can be easily customized by modifying the `words.txt` file. Simply add or remove words from the file as desired, and the game will automatically use the updated list of words the next time you run it.

## Requirements

Wordle requires Python 3.x to run. You can check which version of Python you have installed by running the following command in your terminal:
```
$ python --version
```

If you don't have Python 3.x installed, you can download it from the [Python website](https://www.python.org/).

## License

Wordle is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
