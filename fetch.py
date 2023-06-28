import glob
import os
import shutil
import time
import threading
import logging
from shutil import copytree, rmtree
from config import ip1,ip2,ip3,ip4
print('You are about to fetch logs containing certain infromation from all your servers')
#get the unique variable to defferentiate date
date=input("enter date: yyyymmdd: ")
token=input("enter Search token: Token: ")
hr=input("enter Hr: HH: ")
#store the IPs$path in this location in this format "//127.0.0.1/c$/python_work/FETCH_LOG/wrapper"
#url='C:/FETCH_LOG/FETCH_LOG/ips.txt'
#read the the file-ips.tx
ip1=ip1['host']
def my_ips1(ip1):

    path='C:/FETCH_LOG/FETCH_LOG/para.txt'

    try:
        #read the name structure stored in above
        with open(path, 'r') as file_object:
            liness=file_object.read()
            #print(lines)
            logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'name \n{liness}, exist in {path}') 
    except:
        print(f"The file does not exist in the location")
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files named -para.txt does not exist in the location:') 
        

    else:
        #make a list of the names
        contents1=liness.split('\n')
        print(contents1)
        
        #loop through the names 1 at a time
        for name in contents1[:]:
            print(name)
            destination=str("C:/FETCH_LOG/FETCH_LOG/content")
            print(ip1)
            #pass the stored  IPs$path to an os list
            for file in os.listdir(str(ip1)):
                print(file)
                names=name+date+'T'+hr
                #search for files that start with the above naming convention
                if file.startswith((names)):
                    #print(name+date)
                    path2=f'{ip1}/{str(file)}'
                    #print(path2)
                    #read the file that start with the define naming convention
                    with open(path2, 'r') as file_object:
                        lines=file_object.read()
                        #print(lines)
                        #convert to list
                        contents2=lines.split('\n')
                            
                        count=0
                        #loop through the list of the content of the file and search for the token supllied
                        for line in contents2[:]:
                            #print(contents2)
                            search=token
                            if search in line:
                                count+=1
                                #print(search)
                                print(f'{search} can be found {count} times in {file} and have been copied to "content"')



                                src = f'{ip1}/{str(file)}'
                                destination=str(f"C:/FETCH_LOG/FETCH_LOG/content/{str(file)}")
                                dst = destination
                                #print(dst)
                                #if token is found in the log, the log is moved to a location called content in destination
                                shutil.copy2(src, dst)
                                #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                                logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')
                                    
ip2=ip2['host']
def my_ips2(ip2):
    path='C:/FETCH_LOG/FETCH_LOG/para.txt'

    try:
        #read the name structure stored in above
        with open(path, 'r') as file_object:
            liness=file_object.read()
            #print(lines)
            logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'name \n{liness}, exist in {path}') 
    except:
        print(f"The file does not exist in the location")
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files named -para.txt does not exist in the location:') 
        

    else:
        #make a list of the names
        contents1=liness.split('\n')
        print(contents1)
        
        #loop through the names 1 at a time
        for name in contents1[:]:
            print(name)
            destination=str("C:/FETCH_LOG/FETCH_LOG/content")
            print(ip2)
            #pass the stored  IPs$path to an os list
            for file in os.listdir(str(ip2)):
                print(file)
                names=name+date+'T'+hr
                #search for files that start with the above naming convention
                if file.startswith((names)):
                    #print(name+date)
                    path2=f'{ip2}/{str(file)}'
                    #print(path2)
                    #read the file that start with the define naming convention
                    with open(path2, 'r') as file_object:
                        lines=file_object.read()
                        #print(lines)
                        #convert to list
                        contents2=lines.split('\n')
                            
                        count=0
                        #loop through the list of the content of the file and search for the token supllied
                        for line in contents2[:]:
                            #print(contents2)
                            search=token
                            if search in line:
                                count+=1
                                #print(search)
                                print(f'{search} can be found {count} times in {file} and have been copied to "content"')



                                src = f'{ip2}/{str(file)}'
                                destination=str(f"C:/FETCH_LOG/FETCH_LOG/content/{str(file)}")
                                dst = destination
                                #print(dst)
                                #if token is found in the log, the log is moved to a location called content in destination
                                shutil.copy2(src, dst)
                                #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                                logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')

ip3=ip3['host']
def my_ips3(ip3):

    path='C:/FETCH_LOG/FETCH_LOG/para.txt'

    try:
        #read the name structure stored in above
        with open(path, 'r') as file_object:
            liness=file_object.read()
            #print(lines)
            logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'name \n{liness}, exist in {path}') 
    except:
        print(f"The file does not exist in the location")
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files named -para.txt does not exist in the location:') 
        

    else:
        #make a list of the names
        contents1=liness.split('\n')
        print(contents1)
        
        #loop through the names 1 at a time
        for name in contents1[:]:
            print(name)
            destination=str("C:/FETCH_LOG/FETCH_LOG/content")
            print(ip3)
            #pass the stored  IPs$path to an os list
            for file in os.listdir(str(ip3)):
                print(file)
                names=name+date+'T'+hr
                #search for files that start with the above naming convention
                if file.startswith((names)):
                    #print(name+date)
                    path2=f'{ip3}/{str(file)}'
                    #print(path2)
                    #read the file that start with the define naming convention
                    with open(path2, 'r') as file_object:
                        lines=file_object.read()
                        #print(lines)
                        #convert to list
                        contents2=lines.split('\n')
                            
                        count=0
                        #loop through the list of the content of the file and search for the token supllied
                        for line in contents2[:]:
                            #print(contents2)
                            search=token
                            if search in line:
                                count+=1
                                #print(search)
                                print(f'{search} can be found {count} times in {file} and have been copied to "content"')



                                src = f'{ip3}/{str(file)}'
                                destination=str(f"C:/FETCH_LOG/FETCH_LOG/content/{str(file)}")
                                dst = destination
                                #print(dst)
                                #if token is found in the log, the log is moved to a location called content in destination
                                shutil.copy2(src, dst)
                                #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                                logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')
ip4=ip4['host']
def my_ips4(ip4): 

    path='C:/FETCH_LOG/FETCH_LOG/para.txt'

    try:
        #read the name structure stored in above
        with open(path, 'r') as file_object:
            liness=file_object.read()
            #print(lines)
            logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
            logging.warning(f'name \n{liness}, exist in {path}') 
    except:
        print(f"The file does not exist in the location")
        logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.warning(f'The files named -para.txt does not exist in the location:') 
        

    else:
        #make a list of the names
        contents1=liness.split('\n')
        print(contents1)
        
        #loop through the names 1 at a time
        for name in contents1[:]:
            print(name)
            destination=str("C:/FETCH_LOG/FETCH_LOG/content")
            print(ip4)
            #pass the stored  IPs$path to an os list
            for file in os.listdir(str(ip4)):
                print(file)
                names=name+date+'T'+hr
                #search for files that start with the above naming convention
                if file.startswith((names)):
                    #print(name+date)
                    path2=f'{ip4}/{str(file)}'
                    #print(path2)
                    #read the file that start with the define naming convention
                    with open(path2, 'r') as file_object:
                        lines=file_object.read()
                        #print(lines)
                        #convert to list
                        contents2=lines.split('\n')
                            
                        count=0
                        #loop through the list of the content of the file and search for the token supllied
                        for line in contents2[:]:
                            #print(contents2)
                            search=token
                            if search in line:
                                count+=1
                                #print(search)
                                print(f'{search} can be found {count} times in {file} and have been copied to "content"')



                                src = f'{ip4}/{str(file)}'
                                destination=str(f"C:/FETCH_LOG/FETCH_LOG/content/{str(file)}")
                                dst = destination
                                #print(dst)
                                #if token is found in the log, the log is moved to a location called content in destination
                                shutil.copy2(src, dst)
                                #os.rename("C://python_work//folder_zip//output//"+ name,"C://python_work//folder_zip//output//"+ name+date)
                                logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
                                logging.warning(f'The files patterns: Zipped soruce files is being moved to their individual Folders {dst}')
                                       
# Create threads for each server
#postgres_thread = threading.Thread(target=run_postgres_query)
thread1 = threading.Thread(target=my_ips1)
thread2 = threading.Thread(target=my_ips2)
thread3 = threading.Thread(target=my_ips3)
thread4 = threading.Thread(target=my_ips4)

# Start the threads
#postgres_thread.start()
thread1.start()
thread2.start()
thread3.start()
thread4.start()


# Wait for the threads to finish
#postgres_thread.join()
thread1.join()
thread2.join()
thread3.join()
thread4.join()