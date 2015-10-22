# Burmese word segmentation program using Foma-generated Finite State Automata

## How to compile

### Requirements

- [Foma library](https://code.google.com/p/foma/)
- Cmake

You will need to have cmake version greater than or equal to 3.2.

Compile with the command in the working directory:

    cmake ..

## How to run

    ./segment burmese.foma 'ကလေးများကျောင်းသို့သွားကြသည်။'

## How to compile a new finite state automata with a different word list

Create a file called ``burmese.txt``. There is a ``template.txt`` in the folder. Here is the content:

    define words [these|are|burmese|words|separated|by|pipe];
    regex words @> "|" ... ;

Your word list will go in the first line. Words are separated by "|". You can also replace the separator "|" from the regular expression with anything you like. And then you will have to compile the FSA using ``foma`` command:

    foma -l burmese.txt

You will then be in ``foma`` command prompt. You can save the FSA by:

    save stack burmese.foma