import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [',', '\n']
        custom_delimiter_match = re.match(r"//(.+)\n(.*)", numbers)

        if custom_delimiter_match:
            delimiter_part = custom_delimiter_match.group(1)
            numbers = custom_delimiter_match.group(2)

            if delimiter_part.startswith('['):
                # multiple or multi-char delimiters
                delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
            else:
                delimiters = [delimiter_part]

        # Build regex pattern to split numbers
        delimiter_pattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(delimiter_pattern, numbers)

        result = 0
        negatives = []

        for token in tokens:
            if not token:
                continue
            num = int(token)
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                result += num

        if negatives:
            raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
        
        return result


if __name__ == "__main__":
    calc = StringCalculator()
    input_str = input("Enter numbers string (use \\n for newlines): ")
    input_str = input_str.replace("\\n", "\n")
    try:
        result = calc.add(input_str)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
