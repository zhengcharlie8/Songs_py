
class Song:

    """
    Initial function for Song object.
    parse a given songRecord string to song object.
    For an example songRecord such as "0, Qing Yi Shi,Leon Lai,203.38893,5237536"
    It contains attributes (ID, title, artist, duration, trackID)
    """
    # These create methods checks when there is a ',' character and counts it.
    def createID(self, songRecord):
        ID = ""
        for x in songRecord:
            if x is ',':
                break
            ID += x
        return ID[:len(ID)-1]

    def createTitle(self, songRecord):
        count = 0
        Title = ""
        for x in songRecord:
            if count == 1:
                Title += x
            if x is ',':
                count = count + 1
                if count == 2:
                    break
        return Title[:len(Title)-1]

    def createArtist(self, songRecord):
        count = 0
        Artist = ""
        for x in songRecord:
            if count == 2:
                Artist += x
            if x is ',':
                count = count + 1
                if count == 3:
                    break
        return Artist[:len(Artist)-1]

    def createDuration(self, songRecord):
        count = 0
        Duration = ""
        for x in songRecord:
            if count == 3:
                Duration += x
            if x is ',':
                count = count + 1
                if count == 3:
                    break
        return Duration[:len(Duration)-1]

    def createTrackID(self, songRecord):
        count = 0
        TrackID = ""
        for x in songRecord:
            if count == 4:
                TrackID += x
            if x is ',':
                count = count + 1
        return TrackID[:len(TrackID)-1]

    def __init__(self, songRecord):
        self.size = 0
        self.ID = self.createID(songRecord)
        self.title = self.createTitle(songRecord)
        self.artist = self.createArtist(songRecord)
        self.duration = self.createDuration(songRecord)
        self.trackID = self.createTrackID(songRecord)
        self.key = None

    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist

if __name__ == '__main__':

    sampleSongRecord = "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    sampleSong = Song(sampleSongRecord)
    print(sampleSong.toString())
