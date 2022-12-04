#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SHarms, 2022-Nov-30, Added code
# SHarms, 2022-Dec-04, Fixed inv display issue. Added pseudocode.
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __init__(self, id, title, artist): 
        display(self): prints each data row to user.
    """
    def __init__(self, id, title, artist):
        """Schema for how CD data is stored
        Args: None
        Returns: None"""
        
        self.cd_id = id
        self.cd_title = title
        self.cd_artist = artist

    def display(self):
        """Displays CD data
        Args: None
        Returns: prints a string"""
        
        print (str(self.cd_id) + ',' + self.cd_title + ',' + self.cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        load_inventory(file_name): -> (a list of CD objects)
        save_inventory(file_name, lst_Inventory): -> None

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a list of objects.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            None.
        """
        lstOfCDObjects.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            try:
                objCD = CD(int(data[0]), data[1], data[2])
            except ValueError:
                print ("An ID was found to not be an integer. Inventory failed to load past that record.")
            else:
                lstOfCDObjects.append(objCD)
        objFile.close()

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Writes from list to a file.
        Args:
            file_name: file name
            lst_Inventory: list of CD objects
        Returns:
            None"""
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            strCD = str(row.cd_id) + ',' + row.cd_title + ',' + row.cd_artist
        objFile.write(strCD + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Menu and user choices:

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> choice string
        show_inventory(table):-> None
        add_CD():-> None
        """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None."""
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table
        Args:
            table that holds the data during runtime.
        Returns:
            None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            row.display()
        print('======================================')

    @staticmethod
    def add_CD():
        """Asks user for cd data inputs
        Args:
            None.
        Returns:
            None.
            """
        try:
            intID = int(input('Enter ID: ').strip())
        except ValueError:
            print("\nYou did not enter a numeric ID. The entry was cancelled.\n")
        else:
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            objCD = CD(intID, strTitle, strArtist)
            lstOfCDObjects.append(objCD)

# -- Main Body of Script -- #
FileIO.load_inventory(strFileName)

# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break    
    # show user current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.        
    # let user add data to the inventory
    elif strChoice == 'a':
        IO.add_CD()
        continue
    # let user save inventory to file
    elif strChoice == 's':
        FileIO.save_inventory(strFileName, lstOfCDObjects)
        continue
    # let user load inventory from file
    elif strChoice == 'l':
        FileIO.load_inventory(strFileName)
        continue
    