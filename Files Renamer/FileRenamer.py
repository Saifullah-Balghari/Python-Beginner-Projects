import os

class FileRenamer:

    def __init__(self,):
        os.chdir("Cluttered_folder/")
        self.Cluttered_folder = os.listdir()

    def rename_files(self):
        i = 1
        for file in self.Cluttered_folder:

            name, extension = os.path.splitext(file)
            
            new_name = f"File {i}{extension}"

            os.rename(file, new_name)
            i += 1


def main():

    file_renamer_instance = FileRenamer()
    file_renamer_instance.rename_files()


if __name__ == "__main__":
    main()
        