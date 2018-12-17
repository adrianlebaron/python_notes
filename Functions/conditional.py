def list_cleany(1st)
  if len(list) > 2:
    lst.pop(0)
    lst.pop()
    return lst
  else:
    return "longer list plzzz"

print(list_cleany(["first thing", "another"]))