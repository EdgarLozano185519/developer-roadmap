import json
import sys

def parse_roadmap(data, type):
  nodes = data['mockup']['controls']['control']
  with open("../text/"+type+".txt","w") as file:
    for element in nodes:
      if "properties" in element:
        properties = element['properties']
        if "text" in properties:
          file.write(properties['text']+"\n")
          #print(properties['text'])

print("Roadmap text parser: A small script to extract text from developer roadmaps for plain text usage.\n")
number_arguments = len(sys.argv)

if number_arguments < 2:
  print("Error! Number of arguments is not correct.")
else:
  if sys.argv[1] == "backend" or sys.argv[1] == "frontend" or sys.argv[1] == "devops" or sys.argv[1] == "intro":
    with open("../"+sys.argv[1]+"-map.json") as f:
      data = json.load(f)
      parse_roadmap(data, sys.argv[1])
  else:
    print("Error. Roadmap name not valid.")
    print("Valid roadmaps are backend, frontend, or devops.")
