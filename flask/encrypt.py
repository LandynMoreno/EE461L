def customEncrypt(inputText, N, D):
    reverse = inputText[::-1]
    shift = N*D
    result = ""
    for letter in reverse:
        num = ord(letter) -34 +shift
        num = num % 93
        num = num+34
        result = result + chr(num)
    return result
