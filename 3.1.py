def right_justify(text):
    length=len(text)
    spacetime=70-length
    blank=(' '*spacetime)
    print(blank,text)

right_justify("What am I doing here?")

