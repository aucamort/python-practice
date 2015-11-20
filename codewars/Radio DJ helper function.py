# Radio DJ helper function

# James is a DJ at a local radio station. As it's getting to the top of the hour, he needs to find a 
# song to play that will be short enough to fit in before the news block. He's got a database of songs 
# that he'd like you to help him filter in order to do that.

# Create longestPossible(longest_possible in python and ruby) helper function that takes 1 integer 
# argument which is a maximum length of a song in seconds.

# songs is an array of objects which are formatted as follows:
# {'artist': 'Artist', 'title': 'Title String', 'playback': '04:30'}

# You can expect playback value to be formatted exactly like above.

# Output should be a title of the longest song from the database that matches the criteria of not being 
# longer than specified time. If there's no songs matching criteria in the database, return false.

def longest_possible(playback):
    longestTime = 0
    thisSong = None
    for song in songs:
        time = song['playback']
        min, sec = time.split(':')
        time = float(min)*60 + float(sec)
        if time < playback:
            if longestTime < time:
                longestTime = time
                thisSong = song
    if thisSong is None:
        return False
    return thisSong['title']
    
