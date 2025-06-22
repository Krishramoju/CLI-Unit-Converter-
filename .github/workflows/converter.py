#!/usr/bin/env python3
import argparse

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Temperature Converter - Convert between Celsius and Fahrenheit",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--celsius', type=float, 
                      help="Convert Celsius to Fahrenheit")
    group.add_argument('-f', '--fahrenheit', type=float,
                      help="Convert Fahrenheit to Celsius")
    
    args = parser.parse_args()
    
    if args.celsius is not None:
        f = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius:.2f}°C is {f:.2f}°F")
    elif args.fahrenheit is not None:
        c = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit:.2f}°F is {c:.2f}°C")

if __name__ == "__main__":
    main()
