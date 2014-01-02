import sys
from hopcroft import bipartiteMatch

def parseCase():
  firstLine = sys.stdin.readline()

  catCount, dogCount, voteCount = [int(num) for num in firstLine.split()]

  dogLoverVotes = []
  catLoverVotes = []
  conflicts = {}

  for index in range(voteCount):
    line = sys.stdin.readline().split()
    vote = [line[0], line[1], index]
    if (vote[0][0] == 'D'):
      catLoverVotes.append(vote)
    else:
      dogLoverVotes.append(vote)

  for dvote in dogLoverVotes:
    for cvote in catLoverVotes:
      if (dvote[0] == cvote[1] or dvote[1] == cvote[0]):
        if dvote[2] in conflicts.keys():
          conflicts[dvote[2]].append(cvote[2])
        else:
          conflicts[dvote[2]] = [cvote[2]]
  
  max_set, pred, unlayered = bipartiteMatch(conflicts)
  return voteCount - len(max_set)

def main(argv=None):
  results = []
  problemCount = int(sys.stdin.readline())
  for problem in range(problemCount):
    results.append(parseCase())
  for result in results:
    print result  

if __name__ == "__main__":
    sys.exit(main())