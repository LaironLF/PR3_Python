from Classes.AnaliseFile import AnaliseFile
from Classes.CreateFile import CreateFiles

if __name__ == '__main__':
    # file_creator = CreateFiles('./files')
    # file_creator.create_file('test', 10, 10)
    
    file_analise = AnaliseFile('./files/test.txt')
    file_analise.analise()
    file_analise.printResult()
    