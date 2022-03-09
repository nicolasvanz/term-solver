# Term solver

this is a simple solver for the puzzle available in [term.ooo](https://term.ooo/)

#### Usage
type the word followed by the info that is shown in the screen. Example:
```
termo rygrr
```
in this guess you are telling the program this:
```
t -> not present (red)
e -> present but in wrong position (yellow)
r -> present and in right position (green)
m -> not present (red)
o -> not present (red)
```

after a guess the program recomends a word

# Running code
#### Create virtual environment
```
python3 -m virtualenv venv
```
#### Activate environment
```
source venv/bin/activate
```
#### Install dependencies
```
pip3 install -r requirements.txt
```
#### Run code
```
python3 main.py
```

# Wordle Solver with GO

A simple [Woordle](https://www.nytimes.com/games/wordle/index.html) solver using Go Lang.

## How to user

Before the first tip, you need to input the first word by your own.

To type your guess you need to do like this, for example:

```
termo rygrr

t -> not present (red)
e -> present but in wrong position (yellow)
r -> present and in right position (green)
m -> not present (red)
o -> not present (red)
```
After the guess the programm recommends a suggest to you.

## Running code

In the root folder of your project:
```
go run *.go
```
