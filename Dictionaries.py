#dictionaries allow you to store info in "key value pairs"
#dictionaries use curly brackets
#left side is the key, right side is the value, all keys must be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "June": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
#can use square bracket to access keys
print(monthConversions["Mar"])
#can also use .get
print(monthConversions.get("Dec"))
#with get function, can specify default value to use if key is not found
print(monthConversions.get("Luv", "Not a valid Key"))
#keys can also be numbers as long as they're unique








