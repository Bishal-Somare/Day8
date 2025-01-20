# Day8

## Overview
This project demonstrates how to integrate Python and Java by:

1. Using Python to invoke a Java program via `subprocess`.
2. Passing input data from Python to Java.
3. Performing computations in Java and returning results to Python.

## Features
- Python (Driver): Responsible for orchestrating the integration, compiling, and running the Java program.
- Java (ComplexLogic.java):Computes the sum of GCD and LCM for two numbers received from Python.

## Prerequisites
- Python 3.x
- Java Development Kit (JDK)

4. Observe the output, which includes the computed results from the Java program.
Example
Input

25 30


### Output

Output from Java Program:
GCD + LCM: 180

 Notes
- Ensure that the Java file is in the same directory as the Python script.
- Modify the input data in the Python script as needed.
- Handle errors gracefully by reviewing the error messages from Python or Java.

This integration can be extended to more complex workflows, such as data processing pipelines, leveraging the strengths of both languages.
