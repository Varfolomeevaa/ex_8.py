import json

# [["hi", 2], ["by", 3],["no",2],["yes",1]]


lst_tpl = input()
lst_tpl = json.loads(lst_tpl)
lst_tpl.sort(key=lambda x: x[1], reverse=True)
print(lst_tpl)
