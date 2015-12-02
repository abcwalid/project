#!/usr/bin/python
import os 
print ('Managment of Rental Cars\n')
x=9;
f1=[];
f2=[];
f3=[];
f4=[];
a='a';
rentf1=[];
rentf2=[];
rentf3=[];
rentf4=[];
import subprocess as sp
########################   Make empty files incase there is no file in the directory
infile = open('car_made.txt', 'a+')       
f1 = infile.read().splitlines()          
infile.close()
infile = open('car_id.txt', 'a+')       
f2 = infile.read().splitlines()         
infile.close()
infile = open('car_price.txt', 'a+')         
f4 = infile.read().splitlines()          
infile.close()
infile = open('car_color.txt', 'a+')  
f3 = infile.read().splitlines()          
infile.close()


infile = open('r_car_made.txt', 'a+')     
rentf1 = infile.read().splitlines()     
infile.close()
infile = open('r_car_id.txt', 'a+')      
rentf2 = infile.read().splitlines()     
infile.close()
infile = open('r_car_price.txt', 'a+')        
rentf3 = infile.read().splitlines()     
infile.close()
infile = open('r_car_color.txt', 'a+')  
rentf4 = infile.read().splitlines()    
infile.close()
####################################################################################
infile = open('car_made.txt', 'r+')       
f1 = infile.read().splitlines()          
infile.close()
infile = open('car_id.txt', 'r+')       
f2 = infile.read().splitlines()         
infile.close()
infile = open('car_price.txt', 'r+')         
f4 = infile.read().splitlines()          
infile.close()
infile = open('car_color.txt', 'r+')  
f3 = infile.read().splitlines()          
infile.close()


infile = open('r_car_made.txt', 'r+')     
rentf1 = infile.read().splitlines()     
infile.close()
infile = open('r_car_id.txt', 'r+')      
rentf2 = infile.read().splitlines()     
infile.close()
infile = open('r_car_price.txt', 'r+')        
rentf3 = infile.read().splitlines()     
infile.close()
infile = open('r_car_color.txt', 'r+')  
rentf4 = infile.read().splitlines()    
infile.close()

xx=0;
def rentcar(xx):
    z=f1[xx];
    rentf1.append(z);
    z=f1.pop(xx);
    z=f2[xx];
    rentf2.append(z);
    z=f2.pop(xx);
    z=f3[xx];
    rentf3.append(z);
    z=f3.pop(xx);
    z=f4[xx];
    rentf4.append(z);
    z=f4.pop(xx);
   
def rentedcar(xx):#function that returns car fro customer tostack to be used for next time
    f1.append(rentf1[xx]);
    z=rentf1.pop(xx);
    
    f2.append(rentf2[xx]);
    z=rentf2.pop(xx);
    
    f3.append(rentf3[xx]);
    z=rentf3.pop(xx);
    
    f4.append(rentf4[xx]);
    z=rentf4.pop(xx);
	
pp=0;
def pclear(): 
	for pp in range(10):
		print ('       \n');
		

pclear();
while (x!=0):
    print ('| 1 | Add Car in the strore ---------\n');
    print ('| 2 | Rent Car ----------------------\n');
    print ('| 3 | Calculate total price ---------\n');
    print ('| 4 | Cars availoble ----------------\n');
    print ('| 5 | See Rented Cars ---------------\n');
    print ('| 6 | Customer Return Car -----------\n');
    print ('| 0 | EXIT --------------------------\n');

    x = int(raw_input(" "))
    if x==1:
	pclear();
        a=raw_input('What is the Make of the Car ----\n');
        f1.append(a);
        a=raw_input('what is the ID of the Car-------\n');
        f2.append(a);
        a=raw_input('What is the Collor of the car---\n');
        f3.append(a);
        a=raw_input('What is the Unit price per day--\n');
        f4.append(a);
    
    elif x==2:
        a=raw_input('What is the ID of the Car ----\n');
        i=0;
        print ('  | Make:        ',rentf1[i]);
        print ('  | Car ID:      ',rentf2[i]);
        print ('  | Color:       ',rentf3[i]);
        print ('  | Unit Price:  ',rentf4[i]);
        print ('-----------------------------------------\n');
        rentcar(i);
    elif x==3:
        print ('iiiii3333333333iii')
    elif x==4:
        i=0;
        print ('Cars in Stack Availoble for Rent are ',len(f1));
        while (i!=len(f1)):
            print ('  | Make:        ',f1[i]);
            print ('  | Car ID:      ',f2[i]);
            print ('  | Color:       ',f3[i]);
            print ('  | Unit Price:  ',f4[i]);
            print ('-----------------------------------------\n');
            i=i+1;
	raw_input('Press Enter to Contunue ');
    elif x==5:
        i=0;
        print ('Rented Cars are ----------------------------- ',len(rentf1));
        while (i!=len(rentf1)):
            print ('  | Make:        ',rentf1[i]);
            print ('  | Car ID:      ',rentf2[i]);
            print ('  | Color:       ',rentf3[i]);
            print ('  | Unit Price:  ',rentf4[i]);
            print ('-----------------------------------------\n');
            i=i+1;
	raw_input('Press Enter to Contunue ');
    elif x==6:
        a=raw_input('What is the ID of the Car ----\n');
        i=0;
        i=rentf2.index(a);
        print ('  | Make:        ',rentf1[i]);
        print ('  | Car ID:      ',rentf2[i]);
        print ('  | Color:       ',rentf3[i]);
        print ('  | Unit Price:  ',rentf4[i]);
        print ('-----------------------------------------\n');
        rentedcar(i);#function is going to move car's information from variable rent to a stack variable to be used next time
    
 

ff1 = open('car_made.txt', 'w+')       
ff2 = open('car_id.txt', 'w+')
ff3 = open('car_color.txt', 'w+')       
ff4 = open('car_price.txt', 'w+')         
############ rentale file
ff5 = open('r_car_made.txt', 'w+')      
ff6 = open('r_car_id.txt', 'w+')
ff7 = open('r_car_color.txt', 'w+')
ff8 = open('r_car_price.txt', 'w+')        
        




while (len(f1)!=0):

    ff1.write(f1.pop());
    ff1.write('\n');
    
    ff2.write(f2.pop())
    ff2.write('\n')
    
    ff3.write(f3.pop());
    ff3.write('\n');
    
    ff4.write(f4.pop());
    ff4.write('\n');
while (len(rentf1)!=0):   
    ff5.write(rentf1.pop());
    ff5.write('\n');

    ff6.write(rentf2.pop());
    ff6.write('\n');
    
    ff7.write(rentf3.pop());
    ff7.write('\n');
    
    ff8.write(rentf4.pop());
    ff8.write('\n');
    
ff1.close();
ff2.close();
ff3.close();
ff4.close();
ff5.close();
ff6.close();
ff7.close();
ff8.close();