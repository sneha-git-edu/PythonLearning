face=input("")
if(face.find(':(')!=-1):
    face=face.replace(':(', '🙁')
if face.find(':)')!=-1:
    face=face.replace(':)', '🙂')
print(face)
    