import sys

class Zipfsong(object):
  def __init__(self, index, playCount, name):
    self.index, self.playCount, self.name = index, playCount, name
  def quality(self):
    return self.index * self.playCount

def main(argv=None):
  firstLine = sys.stdin.readline()
  numberOfSongs, selectionSize = [int(n) for n in firstLine.split()]
  songs = []
  for index in range(1, numberOfSongs+1):
    line = sys.stdin.readline().split()
    playCount = int(line[0])
    name = line[1]
    song = Zipfsong(index, playCount, name)
    songs.append(song)
  songs.sort(key=lambda x: x.quality(), reverse=True)
  for i in range(selectionSize):
    print songs[i].name
  return 0

if __name__ == "__main__":
    sys.exit(main())