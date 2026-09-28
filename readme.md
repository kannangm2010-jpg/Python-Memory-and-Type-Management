# Python Memory and Type Management

## Overview
This repository explores how Python handles dynamic typing, primitive data structures, and memory allocation at the system level.

## Contents
* **Memory Tracking:** Utilizing the `id()` function to track memory addresses, demonstrating how Python caches small integers and updates pointers during variable reassignment.
* **System Operations:** Importing the `sys` module to calculate the exact byte size (`sys.getsizeof()`) of integers, floats, complex numbers, booleans, and strings.
* **Data Casting:** Explicit conversions between integers, floats, and strings during arithmetic and concatenation operations.