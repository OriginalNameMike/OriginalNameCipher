from dMessegeEngine import DMessegeEngine 

# Вызов конструктора класса DMessegeEngine с параметром 10 (key)
engine = DMessegeEngine(10)
engine1 = DMessegeEngine(15)
#cipherd присвоили результат шифрования методом cipher "hello world!" (messege)
ciphered = engine.cipher("hello world!")
#Дописать
deciphered = engine.decipher(ciphered)

engine.report("My naME is life!")
engine1.report("My name is life!")

engine.report("very god!&**")
engine.key = 15
engine.report("i am cool$")

#Классы Кот и Собака, 5 полей и 5 методов.