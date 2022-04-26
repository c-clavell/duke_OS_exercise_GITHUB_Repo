Create a Reporting Script for File Sizes

Specific instructions for the project
In this project, the goal is for you to create a Python script in a single file that will traverse the filesystem finding the largest files in a path.

The function walkOS(path) is implemented recursively to get all the files including the files located inside subdirectories. The starting point is the path chosen to a directory. The function uses the os.walk(path) method
to get the root path and the names of the directories and file. The os.path.getsize(absolute_path) method is used to get the size of the file. The os.path.splitext(absolute_path) method is used to get the name and the type of file separately.

The name of the file, type and size are appended to a list. 
The program puts the list's data into a sql table.
Using many different sql queries some details of the files found are displayed: Number of files,larget file, smallest file and a list of the types of files found.