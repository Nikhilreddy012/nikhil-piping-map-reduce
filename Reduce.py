input = open("sortdata.txt","r")
reduceoutput = open("reducedata.txt", "w")

thisKey = ""
thisValue = 0.0

for line in input:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      reduceoutput.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
reduceoutput.write(thisKey + '\t' + str(thisValue)+'\n')

input.close()
reduceoutput.close()
