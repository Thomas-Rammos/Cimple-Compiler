# Cimple-Compiler
Design and implementation of a compiler for the Cimple programming language.

# Introduction
This project involves the creation of a compiler for a simplified programming language called Cimple. The compiler was developed as part of the "Translators" course at the Department of Computer Engineering and Informatics at the University of Ioannina.

The compiler reads source code written in Cimple, performs lexical, syntactical, and semantic analysis, generates intermediate code, and produces assembly code for a target machine (MIPS).

# How It Works
The Cimple compiler processes the input Cimple code through several stages:

  1. Lexical Analysis: The program's text is broken down into tokens, identifying keywords, identifiers, numbers, and operators.
  2. Syntactic Analysis: Using an LL1 grammar, the compiler checks if the token stream follows the correct syntax of the Cimple language.
  3. Semantic Analysis: The meaning of each part of the code is checked, ensuring that variables are declared before use, function returns are valid, and other semantic rules are followed.
  4. Intermediate Code Generation: The compiler generates quadruples, which are used in the later stages of code generation.
  5. Final Code Generation: The intermediate code is translated into MIPS assembly code. This code is then outputted into .asm files.
 # Features
- Supports basic control structures like if, else, while, and function/procedure calls.
- Generates assembly code for MIPS architecture.
- Can handle variables, constants, arithmetic operations, and logical operations.
# How to Use
  # Running the Compiler
  1. Make sure you have Python installed.
  2. Place your Cimple source code file (with a .ci extension) in the same directory as the compiler.
  3. Run the compiler with the command
     - python met.py yourfile.ci
The compiler will generate two output files:
- A .int file containing the intermediate code.
- An .asm file with the final MIPS assembly code.
