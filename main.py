file = open('Codingal.txt')
content = file.read()
split_content =  content.split('\n')

print("Lines in the above file is:", len(split_content))