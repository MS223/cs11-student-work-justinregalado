class Song(object):

    def __init__(self, artists,title,lyrics):
        self.lyrics = lyrics
        self.title = title
        self.artists = artists


    def sing_me_a_song(self):
        print self.title +  " By "  +self.artists
        for line in self.lyrics:
            print line

happy_bday = Song("walmart" ,"happy birthdaysong", ["Happy birthday to you",
                   "These lyrics are copywrighted",
                   "So I'll stop here"])

hotline_bling = Song("drake","hotline_bling", ["You used to call me on my",
                      "You used to, you used to",
                      "Yeah"])

happy_bday.sing_me_a_song()

hotline_bling.sing_me_a_song()
