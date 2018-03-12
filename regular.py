import re
pattern = re.compile(r'([\b]+)')
result = pattern.findall('<a href="http://8sot.su/ru/codes7/903/061xxxx">')


print (result)