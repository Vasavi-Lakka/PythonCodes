def alternate_case(input_str):
    result = ""
    for i in range(len(input_str)):
        if i % 2 == 0:
            result += input_str[i].upper()
        else:
            result += input_str[i].lower()
    return result

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    output = alternate_case(user_input)
    print("Output:", output)
