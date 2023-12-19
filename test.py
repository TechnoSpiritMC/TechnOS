org_string = "aaa best bbb"
spl_word = "best "

print("My Original String: " + str(org_string))

print("Resultant word: " + str(spl_word))

result_string = org_string.split(spl_word)[1]

print("Substring After Character : " + result_string)