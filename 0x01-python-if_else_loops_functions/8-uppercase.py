
#!/usr/bin/python3


def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{:s}".format(result)) #!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
    print("{:s}".format(i), end="")
    print()
