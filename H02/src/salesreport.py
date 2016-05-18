'''
CS 132 Homework #2
salesreport.py
@author: Vivan Chung
'''
#TODO You must add your student ID (eg sgilbert) HERE
def student_id():
    '''Return your student ID (eg. mine is sgilbert)'''
    return 'vchung1'
    pass

def open_files()->'(input_file, output_file)':
    '''Prompt for input and output filenames
    Opens both files if possible and returns them in a tuple
    @return tupe of (input_file, output_file) or
        None in place of files that cannot be opened
    '''
    inputFile = input('Please enter the input file: ')
    outputFile = input('Please enter the output file: ')
    try:
        fin = open(inputFile, 'r') 
    except FileNotFoundError: 
        fin = 'None'          
    try:  
        fout = open(outputFile, 'w')
    except FileNotFoundError:
        fout = 'None'
    return (fin, fout)
        
        

def process_files(files: 'tuple(open_file_for_reading, open_file_for_writing)'):
    '''Produces sales report from input file.
    Closes both files when done
    '''
    if(files[0] != 'None' and files[1] != 'None'):
        fin = files[0]
        fout = files[1]
        fout.write('ICE CREAM SALES REPORT \n')
        fout.write ('Flavor  Store 1   Store 2    Store 3    Total')
        fout.write('-' * 30)
        
        for line in fin: 
            tokens = line.split()
            favor = tokens[0]
            store1 = tokens[1]
            store2 = tokens[2]
            store3 = tokens[3]
            total = tokens[4]
            fout.write('{} {} {} {} {}'.format(favor, store1, store2, store3, total))
        
        fin.close(); 
        fout.close(); 
    else:
        print('The files do not exist')
        return 
    
if __name__ == '__main__':
    files = open_files(); # prompt and open
    if (files[0] != None and files[1] != None):
        process_files(files)
