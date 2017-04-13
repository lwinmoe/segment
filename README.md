# Burmese word segmentation program using Foma-generated Finite State Automata

## How to compile

### Requirements

- [Foma library](https://code.google.com/p/foma/)
- Cmake

You will need to have cmake version greater than or equal to 3.2.

Compile with the command in the working directory:

    cmake ..

## How to run

    ./segment burmese.fst 'ကလေးများကျောင်းသို့သွားကြသည်။'

## How to compile a new finite state automata with a different word list

Create a file called ``burmese.scr``. There is a ``template.txt`` in the folder. Here is the content:

    define words [these|are|burmese|words|separated|by|pipe];
    regex words @> "|" ... ;
    save stack burmese.fst

Your word list will go in the first line. Words are separated by "|". You can also replace the separator "|" from the regular expression with anything you like. And then you will have to compile the FSA using ``foma`` command:

    foma -f burmese.scr

### Using Foma script generator to create burmese.scr

If you have a word list, you can generate a Foma script using `generateFomaTemplate.py`. Your word list will be in a text file with each word in separate lines. If the file name of the word list is `burmese.txt`, the following commands will create `burmese.scr` and then compile it into `burmese.fst`:

    python3 generateFomaTemplate.py burmese.txt burmese.scr
    foma -f burmese.scr
