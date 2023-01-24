import csv

machines = {}

# Process a line of the input file. Splits 
def processLine(job, start, end, machine, index):
  if machine not in machines:
    machines[machine] = []
  machines[machine].append({
    "job": int(job),
    "start": int(start),
    "index": int(index),
    "end": int(end)
  })

with open('input.csv') as csvfile:
  fields = ["","job","start","end","maschinen"]
  reader = csv.DictReader(csvfile, fieldnames=fields)
  line_index = 0
  for row in reader:
    if line_index != 0:
      processLine(job=row["job"], start=row["start"], end=row["end"], machine=row["maschinen"], index=row[""])
    line_index += 1


# Sort the machines by their start time
for machine in machines:
  machines[machine] = sorted(machines[machine], key=lambda k: k['start'])

# Output as a Gantt diagram with Mermaid syntax
output = """
gantt
dateFormat  x
axisFormat %S,%L
title Machinen
"""
for machine in machines:
  output += "\nsection Machine {}\n".format(machine)
  for job in machines[machine]:
    output += "Job {} : {},{},{}\n".format(job["job"], job["index"], job["start"], job["end"])

# Read template file
template_content = ""
with open('template.html', 'r') as f:
  template_content = f.read()

# Write output to file based on template and gantt content
with open('out/output.html', 'w') as f:
  f.write(template_content.replace("{{gantt}}", output))