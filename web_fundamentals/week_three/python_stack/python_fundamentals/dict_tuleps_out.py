# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def dict_tuleps(dict):
  newList = []
  for key , data in my_dict.iteritems():
    newList.append((key, data))
  return newList
print dict_tuleps(my_dict)