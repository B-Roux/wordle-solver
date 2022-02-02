# wordle-solver
A fun little challenge I made for myself: A python script that helps you solve wordle puzzles!

This script contains a single function named `print_wordle_matches`, which takes three arguments:
* The first argument must be string of length 5 containing lower-case alpha characters (a-z) for locations with a known character (green squares), or an underscore(\_) for locations without a known character (gray or yellow squares).
* The second argument is a string containing lower-case alpha characters that do appear in the word, but in an unknown location (yellow letters).
* The third argument is a string containing lower-case alpha characters that do not appear in the word (gray letters).

I have also attatched a convenient file that should contain all of the words acceptable to wordle, but I have not tested every single one. I have been using this script to play wordle though, and have found all of them so far.

## Example:

### Step 1:

First, I enter a complete guess (in my case, "could"):

![Step one of playing Wordle: Entered word 'could'](/images/step1.png)

Then I take this image to craft the first function call:
```
  print_wordle_matches ('_o___', '', 'culd')
```

Which outputs:
```
  SOWER
  BOOBY
  FORTH
  TOTEM
  WOOER
  GONER
  FORGE
  MOTOR
  BOOZY
  BOOST
  GORGE
  ...
```

### Step 2:

I enter guess from the list (in my case, "roast"):

![Step two of playing Wordle: Entered word 'roast'](/images/step1.png)

Then I take this image to craft the first function call:
```
  print_wordle_matches ('_o_st', '', 'culdra')
```

Which outputs:
```
  BOOST
  MOIST
  HOIST
  JOIST
  FOIST
  GOEST
  ZOIST
```

### Step 3:

I enter guess from the list (in my case, "moist"):

![Step three of playing Wordle: Entered word 'moist' and won](/images/step1.png)

which turns out to be correct!

## Note:
Wordle (the game) will mark duplicate letters gray if one has been solved already. Any word may contain duplicates - do not put a letter in the third argument which already appears in either the first or the second, you will get nothing back!
