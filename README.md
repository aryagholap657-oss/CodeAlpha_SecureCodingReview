# CodeAlpha Secure Coding Review

## Project Overview

This project demonstrates the difference between insecure and secure coding practices in a Python login system.

## Security Issues Identified

### 1. SQL Injection
The insecure code directly combines user input with the SQL query.

### 2. Plain Text Password Handling
The insecure version uses the password directly without hashing.

### 3. Lack of Secure Input Handling
User input is not safely handled in the insecure version.

## Security Improvements

- Used parameterized SQL queries.
- Added password hashing.
- Improved secure coding practices.

## Technologies Used

- Python
- SQLite
- hashlib

## Internship Task

CodeAlpha Cyber Security Internship  
Task 3: Secure Coding Review