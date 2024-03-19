text = "199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] GET historyapollo HTTP1.0 200 6245"
list = text.split(" ")
print(list)
print(list.index("200"))