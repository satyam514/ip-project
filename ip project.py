import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main_menu():
    print("***********************")
    print("Read Data From File in Different Way")
    print("1. Read complete csv file")
    print("2. Read complete file without index")
    print("========================")
    print("Data Visualisation")
    print("3. Line Chart")
    print("4. Bar Chart")
    print("5. Pie Chart")
    print("6. Scatter Chart")
    print("========================")
    print("Apply Data Manipulation in the records of csv file")
    print("7. Sorting the data as per your choice")
    print("8. Make the copy of CSV file")
    print("9. Read Top and Bottom from file as per requirement")
    print("10. Read the Specific columns")
    print("*************************")
main_menu()

def Read_csv():
    print("Reading Data from csv file")
    df=pd.read_csv("State.csv")
    print(df)

def no_index():
    print("Reading file from csv without index value")
    df=pd.read_csv("State.csv",index_col=0)
    print(df)

def line_plot():
    df=pd.read_csv("State.csv")
    st=df["State"]
    cnf=df["Patients"]
    rc=df["Saved"]
    dt=df["Dead"]
    ac=df["Active"]
    plt.xlabel("State")
    plt.xticks(rotation="vertical")

    print("Select Specific Line Chart as given below:")
    print("Press 1 to print the data for State vs Patients Cases")
    print("press 2 to print the data for State vs Saved Cases")
    print("press 3 to print the data for State vs Death Cases")
    print("press 4 to print the data for State vs Active Cases")
    print("press 5 to merge all data in one line chart")

    op=int(input("Enter your choice: "))

    if op==1:
        plt.ylabel("Patient Cases")
        plt.title("State wise Patient Cases")
        plt.plot(st,cnf)
        plt.show()
    elif op==2:
        plt.ylabel("Saved Cases")
        plt.title("State wise Saved Cases")
        plt.plot(st,rc)
        plt.show()
    elif op==3:
        plt.ylabel("Death Cases")
        plt.title("State wise Death Cases")
        plt.plot(st,dt)
        plt.show()
    elif op==4:
        plt.ylabel("Active Cases")
        plt.title("State wise Active Cases")
        plt.plot(st,ac)
        plt.show()
    elif op==5:
        plt.ylabel("Number of Cases")
        plt.plot(st,cnf,label="State with Patients Cases")
        plt.plot(st,rc,label="State with Saved Cases")
        plt.plot(st,dt,label="State with Death Cases")
        plt.plot(st,ac,label="State with Active Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")

def bar_plot():
    df=df=pd.read_csv("State.csv")
    st=df["State"]
    cnf=df["Patients"]
    rc=df["Saved"]
    dt=df["Dead"]
    ac=df["Active"]
    plt.xlabel("State")

    print("Select Specific Bar Chart as given below:")
    print("Press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Recovered Cases")
    print("press 3 to print the data for State vs Death Cases")
    print("press 4 to print the data for State vs Active Cases")
    print("press 5 to print all the data in the form of stackbar chart")
    print("Press 6 to print all the data in the form of multi bar system")
    
    op=int(input("Enter your choice: "))

    if op==1:
        plt.ylabel("Confirmed Cases")
        plt.title("State wise Confirmed Cases")
        plt.bar(st,cnf)
        plt.show()
    elif op==2:
        plt.ylabel("Recovered Cases")
        plt.title("State wise Saved Cases")
        plt.bar(st,rc)
        plt.show()
    elif op==3:
        plt.ylabel("Death Cases")
        plt.title("State wise Death Cases")
        plt.bar(st,dt)
        plt.show()
    elif op==4:
        plt.ylabel("Active Cases")
        plt.title("State wise Active Cases")
        plt.bar(st,ac)
        plt.show()
    elif op==5:
        plt.ylabel("Number of Cases")
        plt.bar(st,cnf,width=0.2,label="State with Confirmed Cases")
        plt.bar(st,rc,width=0.2,label="State with Recovered Cases")
        plt.bar(st,dt,width=0.2,label="State with Death Cases")
        plt.bar(st,ac,width=0.2,label="State with Active Cases")
        plt.legend()
        plt.show()
    elif op==6:
        ind=np.arange(len(st))
        width=0.25
        plt.bar(ind,cnf,width,label="State wise Condirmed Cases")
        plt.bar(ind+0.25,rc,width,label="State wise Recovered Cases")
        plt.bar(ind+0.50,dt,width,label="State wise Death")
        plt.bar(ind+0.75,ac,width,label="State wise Active")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        
def pie_plot():
    df=pd.read_csv(r"C:\Users\satya\Downloads\State.csv")
    st=df["State"]
    cnf=df["Patients"]
    rc=df["Saved"]
    dt=df["Dead"]
    ac=df["Active"]
    plt.xticks(rotation="vertical")

    print("Select Specific Pie Chart as given below:")
    print("Press 1 to print the data for State vs Confirmed Cases")
    print("press 2 to print the data for State vs Recovered Cases")
    print("press 3 to print the data for State vs Death Cases")
    print("press 4 to print the data for State vs Active Cases")

    op=int(input("Enter your choice: "))

    if op==1:
        plt.title("State wise Confirmed Cases")
        plt.pie(cnf,labels=st,autopct="%2.1f%%")
        plt.show()
    elif op==2:
        plt.title("State wise Recovered Cases")
        plt.pie(rc,labels=st,autopct="%2.1f%%")
        plt.show()
    elif op==3:
        plt.title("State wise Death Cases")
        plt.pie(dt,labels=st,autopct="%2.1f%%")
        plt.show()
    elif op==4:
        plt.title("State wise Active Cases")
        plt.pie(ac,labels=st,autopct="%2.1f%%")
        plt.show()
    else:
        print("Enter valid input")

def scatter_chart():
    df=pd.read_csv("State.csv")
    st=df["State"]
    cnf=df["Patients"]
    rc=df["Saved"]
    dt=df["Dead"]
    ac=df["Active"]
    
    ax=plt.gca()
    ax.scatter(st,cnf,color="b",label="State with Confirmed Cases")
    ax.scatter(st,rc,color="r",label="State with Recovered Cases")
    ax.scatter(st,dt,color="g",label="State with Death Cases")
    ax.plot(st,ac,color="y",label="State with Active Cases")

    plt.xlabel("State")
    plt.xticks(rotation="vertical")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()

def data_sorting():
    df=pd.read_csv("State.csv")
    print("Press 1 to arange the record as per the State Name")
    print("press 2 to arange the record as per the Confirmed Cases")
    print("press 3 to arange the record as per the Recovered Cases")
    print("press 4 to arange the record as per the Deaths Cases")
    print("press 5 to arange the record as per the Active Cases")

    op=int(input("Enter your choice: "))

    if op==1:
        df.sort_values(["State"],inplace=True)
        #inplace: make the changes in passes DataFrame
        print(df)
    elif op==2:
       df.sort_values(["Patients"],inplace=True)
       print(df)
    elif op==3:
        df.sort_values(["Saved"],inplace=True)
        print(df)
    elif op==4:
        df.sort_values(["Dead"],inplace=True)
        print(a)
    elif op==5:
        a=df.sort_values(["Active"],inplace=True)
        print(df)
    else:
        print("Enter valid input")
        
def top_bottom_selected_records():
    df=pd.read_csv("State.csv")
    top=int(input("How many records to display from top: "))
    print("First",top,"records")
    print(df.head(top))

    bottom=int(input("How many records to display from bottom: "))
    print("Last",bottom,"records")
    print(df.tail(bottom))

def duplicate():
    print("Reading Specific Column from csv file")
    df=pd.read_csv("State.csv")
    df.to_csv("StateNew.csv")
    print("Data from the new file")
    print(df)
def specific_col():
    print("Readin Specific column from csv")
    df=pd.read_csv(r"C:\Users\satya\Downloads\State.csv",usecols=["State","Saved"],index_col=0)
    print(df)

opt=int(input("Enter your choice = "))
if opt==1:
    Read_csv()
elif opt==2:
    no_index()
elif opt==3:
    line_plot()
elif opt==4:
    bar_plot()
elif opt==5:
    pie_plot()
elif opt==6:
    scatter_chart()
elif opt==7:
    data_sorting()
elif opt==8:
    duplicate()
elif opt==9:
    top_bottom_selected_records()
elif opt==10:
    specific_col()
else:
    print("Enter valid input")


    


    


    
    

   
