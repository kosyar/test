import pathlib
s = pathlib.Path().resolve()
s = str(s).rsplit(sep="\\" , maxsplit=1)
import sys
sys.path.append(s[0]+"\.moduleA")
import dog2
dogAlbert = dog2.dog("Albert2")
dogAlbert.sayName()
dogAlbert.setName("any name")
dogAlbert.sayName()