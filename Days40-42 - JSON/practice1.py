import json

text_json = '''{
        "demo": "Processing Json in Python",
        "instructor": "Michael",
        "duration": 5.0
        }'''

print(type(text_json), text_json)
#type is string and  double quotes on key and value

data = json.loads(text_json)

print(type(data), data)
#type is dictionary and single quotes on key and value

instructor = data['instructor']

print(instructor)

#better way to write this is to use get because if the value is empty it will not error out also you can
#use a place holder  ==> data.get('instructor', 'SUBSTITUTE')
instructor = data.get('instructor')
print(instructor)

# to make it json
#notice double quotes are back
data_json = json.dumps(data)
print(type(data_json), data_json)