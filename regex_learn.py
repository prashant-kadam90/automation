#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:41:06 2024

@author: prashantkadam
"""

import re


import requests


def test_regex():
    print("Welcome to Regex Tester!")
    print("Enter 'exit' anytime to quit.\n")

    while True:
        # Get regex pattern from user
        pattern = input("Enter your regex pattern: ")
        if pattern.lower() == "exit":
            break
        
        # Get test string from user
        test_string = input("Enter the string to test against: ")
        if test_string.lower() == "exit":
            break
        
        try:
            # Compile the pattern
            regex = re.compile(pattern)
            
            # Find all matches
            matches = regex.findall(test_string)
            if matches:
                print(f"Matches found: {matches}")
            else:
                print("No matches found.")
            
            # Check for a match at the start
            match = regex.match(test_string)
            if match:
                print(f"Matched at the start: {match.group()}")
            
            # Check for a full match
            full_match = regex.fullmatch(test_string)
            if full_match:
                print(f"Fully matched: {full_match.group()}")
            
            # Search for any match
            search = regex.search(test_string)
            if search:
                print(f"First match found: {search.group()} at position {search.start()}-{search.end()}")

        except re.error as e:
            print(f"Invalid regex pattern: {e}")
        
        print("\n---\n")

# Run the tester
if __name__ == "__main__":
    test_regex()