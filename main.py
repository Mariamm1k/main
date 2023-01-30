import os
#create class
class Manager:
    def __init__(self, parameters=None):
        self.code_types = [".html", ".css", ".js", ".py", ".exe"]
        self.document_types = [".xlsx", ".txt", ".csv", ".xls", ".docx"]
        self.video_types = [".mp4", ".mov", ".wav"]
        self.parameters = parameters or ["code", "documents", "videos"]

   #check what file shoudn't be organized 
    def organize_files(self, without=0):
        files = os.listdir()
        for file in files:
            if file == "main.py" or file in without:
                continue
    #file types orgznizing 
            for folder in self.parameters:
                if file.endswith(tuple(eval(f"self.{folder}_types"))):
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    os.rename(file, os.path.join(folder, file))
                    break
    #folder creating if it is not in the parameters
    def create_folder(self, folder_name):
        if folder_name not in self.parameters:
            print(f"You need to add parameters for {folder_name}.")
        else:
            os.makedirs(folder_name)
    #remove folder if it already exists
    def remove_folder(self, folder_name):
        if os.path.exists(folder_name):
            os.rmdir(folder_name)
    #remove parameter if it already exists
    def remove_parameter(self, folder_name):
        if folder_name in self.parameters:
            self.parameters.remove(folder_name)
    #if parameter doesn't exist add it 
    def add_parameter(self, parameter):
        if parameter not in self.parameters:
            self.parameters.append(parameter)