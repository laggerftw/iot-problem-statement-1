import pandas as pd 
import matplotlib.pyplot as plt
while(True):
        print ("Main Menu")
        print ("1. Fetch data")
        print ("2. Display Records")
        print ("3. Working on Records")
        print ("4. Search specific row/column")
        print ("5. Data of medicine stock")
        ch= int (input ("Enter your choice:  "))
        hospital=pd.read_csv("D:\hospital.csv",index_col=0)
        if ch==1:
                print(hospital)
        elif ch==2:
                while (True) :
                    print ("Display Records Menu")
                    print ("1. Specific number of records from the top")
                    print ("2. Specific number of records from the bottom")
                    print ("3. Details of a specific patient")
                    print ("4. Display details of all patients")
                    print ("5. Exit")
                    ch2=int (input ("Enter choice:  "))
                    if ch2==1:
                        n=int (input ("Enter how many records you want to display from the top:  "))
                        print (hospital.head (n))
                    elif ch2==2:
                        n=int (input ("Enter how many records you want to display from the bottom:  ") )
                        print (hospital.tail (n))
                    elif ch2==3:
                        st=input ("Enter the patient name for which you want to see the details:  ")
                        print (hospital.loc[st])
                        s=input("enter patient's diagnosis:  ")
                        if s=="Hyper Tension" or s=="HYPER TENSION" or s=="hyper tension":
                            print("The prescribed medicine is Diuretics")
                        elif s=="Asthma" or s=="asthma" or s=="ASTHMA":
                            print("The prescribed medicines are Fluticasone and Mometasone")
                        elif s=="Heart Attack" or s=="heart attack" or s=="HEART ATTACK":
                            print("The prescribed medicines are Aspirin and Clot Buster")
                        elif s=="Kidney Failure" or s=="kidney failure" or s=="KIDNEY FAILURE":
                            print("The prescribed medicines are Captopril and Finerenone")
                        elif s=="fracture" or s=="Fracture" or s=="FRACTURE":
                            print("The prescribed medicines are Pain Killers")
                        elif s=="Cancer" or s=="cancer" or s=="CANCER":
                            print("The prescribed medicines are Doxorubicin and Idarubincin")
                        elif s=="brain tumor" or s=="Brain Tumor" or s=="BRAIN TUMOR":
                            print("The prescribed medicines are BiCUS and Avastin")
                        elif s=="Liver Transplant" or s=="liver transplant" or s=="LIVER TRANSPLANT":
                            print("The prescribed medicine is Prednisone")
                        elif s=="Tuberculosis" or s=="TUBERCULOSIS" or s=="tuberculosisi":
                            print("The prescribed medicines are Rifampin and Etambutol")
                        elif s=="HIV":
                            print("The prescribed medicines are Abacavir and Tenofovir")
                        elif s=="Measlses" or s=="measlses" or s=="MEASLSES":
                            print("The prescribed medicine is Ibuprofin")
                        elif s=="Slip Disc" or s=="slip disk" or s=="SLIP DISK":
                            print("The prescribed medicines are Aleve and Tylenol")

                            break
                
                    elif ch2==4:
                        print ("Details of all patients:  ")
                        print (hospital)
                    elif ch2==5:
                        break
        elif ch==3:
            while(True):
                        print ("Working on Records Menu")
                        print ("1. Insert the details of a new patient")
                        print ("2. Update a patient details")
                        print ("3. Exit")
                        ch4=int (input ("Enter choice:  "))
                        if ch4==1:
                                a=input("Enter patient name:  ")
                                b=int(input("Enter patient id: "))
                                c=int(input("Enter patient's ward number: "))
                                d=input("Enter patients diagnosis: ")
                                e=input("Enter blood group: ")
                                f=input("Enter blood pressure: ")
                                g=int(input ("Enter heart rate of patient: "))
                                h=int(input ("Enter platelets count: "))
                                i=int(input ("Enter patient age:  "))
                                j=input ("Enter medicine/treatment: ")
                                k=input ("Enter required dosage: ")
                                hospital.loc[a]=[b,c,d,e,f,g,h,i,j,k]
                                print("Data successfully inserted")
                                print(hospital)
                        elif ch4==2:
                            a=input ("Enter patient name for updation:  ")
                            b=int(input ("Enter patient id: "))
                            c=int(input ("Enter patient's ward number: "))
                            d=input("Enter patient's diagnosis: ")
                            e=int(input("Enter patient's blood group: "))
                            f=input("Enter blood pressure: ")
                            g=int(input ("Enter heart rate: "))
                            h=int(input ("Enter platelets count: "))
                            i=input ("Enter patient's age: ")
                            j=input ("Enter required medicine/treatment: ")
                            k=input ("Enter required dosage: ")
                            hospital.loc[a]=[b,c,d,e,f,g,h,i,j,k]
                            print("Data successfully inserted")
                            print(hospital)

                        elif ch4==3:
                            break
        elif ch==4:
                     while(True):
                        print ("Search Menu")
                        print ("1. Search for the details of a patient")
                        print ("2. Search details as per a specific column heading")
                        print ("3. Exit")
                        ch6=int(input("Enter choice "))
                        if ch6==1:
                            st=input ("Enter the name of the patient whose details you want to see")
                            print (hospital.loc [st])
                        elif ch6==2:
                            col=input ("Enter column/heading name whose details you want to see")
                            print(hospital[col])
                        elif ch6==3:
                            break
        elif ch==5:
                   break
meds=pd.read_csv("D:\stock.csv",index_col=0)
print("The following is the table for medicines stock with the hospital")
print(meds)
