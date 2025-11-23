# Text Analyzer Python

This is a simple text analysis program written in Python. It allows registered users to log in, select a text, and receive a detailed analysis of its content.

## Features

**User authentication**: Only registered users can access the app.

**Text selection**: Users can choose from multiple predefined texts for analysis.

**Word statistics**: The program calculates:
Total number of words  
Number of titlecase words  
Number of uppercase words  
Number of lowercase words  
Number of numeric strings  
Sum of all numeric values

**Word length histogram**: Displays the distribution of words based on their length using a simple histogram.

## Predefined Users

The app includes a small set of predefined users for testing:

- bob
- ann
- mike
- liz

Each user has a simple password (used for learning/testing purposes only).

## Predefined Texts

The program contains three texts, each used for analysis.

## How to Use

1. Run the program using Python 3:  
   `python main.py`
2. Enter your username and password when prompted.
3. Choose a text by entering a number.
4. The program will display word statistics and a word length histogram.

## Notes

- Only registered users can access the app; unregistered users are terminated immediately.
- The program is case-sensitive when checking usernames and passwords.
- Word counts ignore punctuation.

## Example Output

After selecting a text, the program shows basic statistics and a word length histogram:  
There are 42 words in the selected text.  
There are 5 titlecase words.  
There are 2 uppercase words.  
There are 35 lowercase words.  
There are 3 numeric strings.  
The sum of all the numbers 1000.  
LEN| OCCURRENCES |NR.  
1 |\* |1  
2 |** |2  
3 |\*** |3  
4 |**\*** |5  
5 |\***\* |4  
6 |** |2

- `LEN` → word length
- `OCCURRENCES` → visual representation with `*`
- `NR.` → exact count of words of that length
