

from Song import Song
import random
import time
import csv



class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not

    """

    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0


    """
    load your Song library from a given file.
    It takes an inputFilename and store the songs in songArray
    """

    # Uploads TenKSong as an .txt file and changes it to a csv file. It then divides every line and adds each line into the songArray
    def loadLibrary(self, inputfilename):
        with open(inputfilename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='=')
            for row in csv_reader:
                self.songArray.append(Song(row[0]))
        self.size = len(self.songArray)

    """
    Linear search function.
    It takes a query string and attibute name (can be 'title' or 'artist')
    and return the number of songs fonud in the library.
    Return -1 if no songs is found.
    Note that, Each song name is unique in the database,
    but each artist can have several songs.
    """

    def linearSearch(self, query, attribute):
        found = 0
        counter1 = 0
        # Checks whether the attribute is title or artist
        # Set a while statement to iterate the entire songArray size and find the title or artist and compares it to the query.
        if attribute == 'title':
            while(counter1<self.size):
                if query == self.songArray[counter1].title:
                    found = 1
                    return found
                counter1 = counter1 + 1
        if attribute == 'artist':
            while(counter1<self.size):
                if query == self.songArray[counter1].artist:
                    found = found + 1
                counter1 = counter1 + 1
        # found is a counter for how many songs are found, if found is 0, then set found at -1.
        if found == 0:
            found = -1
        return found

    """
    Build a BST from your Song library based on the song title.
    Store the BST in songBST variable
    """

    def buildBST(self):
        #Use quicksort to balance it efficiently
        self.quickSort()
        #Binary Search Tree is easily done since the array is sorted
        self.songBST=BinarySearchTree(self.songArray)



    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """

    def searchBST(self, query):

        root=self.songBST.root

        while root is not None:
            if root.title == query:
                return root.toString()
            if query<root.title:
                root=root.leftChild
            else:
                root=root.rightChild
        return None

    """
    Return song libary information
    """

    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)

    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """

    # QuickSort
    def quickSort(self):
        self.qSort(self.songArray, 0, 9708)
        self.isSorted = True

    def qSort(self, arr, start, end):
        if start < end:
            pindex = self.partition(arr, start, end)
            self.qSort(arr, start, pindex - 1)
            self.qSort(arr, pindex + 1, end)

    def partition(self, arr, start, end):
        pivot = end
        pivotValue = arr[pivot].title
        arr[pivot], arr[start] = arr[start], arr[pivot]
        border = start

        for x in range(start, end + 1):
            if arr[x].title < pivotValue:
                border += 1
                arr[x], arr[border] = arr[border], arr[x]
        arr[start], arr[border] = arr[border], arr[start]
        return border

# Create a BST
class BinarySearchTree:
    def __init__(self,arr):
        self.root=None
        self.root = self.balancingBST(arr, 0, 9708)
#This BST works because the list is sorted and continues to
# take the middle breaking list by half
    def balancingBST(self, arr, lower, upper):
        if lower > upper:
            return None
        mid= (lower+upper)//2
        arr[mid].leftChild = self.balancingBST(arr, lower, mid - 1)
        arr[mid].rightChild = self.balancingBST(arr, mid + 1, upper)
        return arr[mid]

if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.txt")
    print(songLib.libraryInfo())
