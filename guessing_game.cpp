#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>

// Read the list of words from the file
std::vector<std::string> readWords(const std::string &filename) {
    std::vector<std::string> words;
    std::ifstream file(filename);
    std::string line;
    while (std::getline(file, line)) {
        words.push_back(line);
    }
    return words;
}

int main() {
    // Read the list of words from the file
    std::vector<std::string> words = readWords("words.txt");

    // Generate a random five-letter word
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, words.size() - 1);
    std::string word = words[dist(gen)];

    // Prompt the user to guess the word
    std::string guess;
    std::cout << "Guess a five-letter word: ";
    std::cin >> guess;

    // Keep track of the number of guesses
    int num_guesses = 1;

    // Keep looping until the user guesses the word or runs out of guesses
    while (guess != word && num_guesses < 6) {
        // Annotate the user's guess with correct letters and correct letters in the correct position
        std::string annotated_guess;
        for (int i = 0; i < guess.length(); i++) {
            if (guess[i] == word[i]) {
                annotated_guess += toupper(guess[i]);
            } else if (word.find(guess[i]) != std::string::npos) {
                annotated_guess += tolower(guess[i]);
            } else {
                annotated_guess += "*";
            }
        }
        std::cout << "Your guess: " << annotated_guess << std::endl;

        // Prompt the user to try again
        std::cout << "Guess a five-letter word: ";
        std::cin >> guess;
        num_guesses++;
    }

    // If the user guessed the word, let them know they won
    if (guess == word) {
        std::cout << "Correct! You won in " << num_guesses << " guesses." << std::endl;
    }

    // If the user ran out of guesses, let them know they lost
    else {
        std::cout << "Sorry, you ran out of guesses. The word was '" << word << "'" << std::endl;
    }

    return 0;
}
