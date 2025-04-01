DNA = "TTTCATTCTAGCTGAAAA"
DNA_r = DNA[::-1]

dicionario = {"A":"T",
              "T":"A",
              "G":"C",
              "C":"G"}

DNA_rc = ""
for n in DNA_r:
    DNA_rc = DNA_rc + dicionario[n]

print(DNA_rc)