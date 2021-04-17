# ----Library-----

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# ----Data-----
data = pd.read_csv("car data.csv")
model = pickle.load(open('carprice.pkl','rb'))

# ----Navigation-----
nav = st.sidebar.radio("Navigation Bar", ['HomePage', 'Graphs'])



                                        # -------------Home_Page------------



if nav == "HomePage":

    def main():

        #-----Heading------
        st.title("Predict The Price Of Yor Car. :car:")

        st.markdown("### Do You Want to predict The Price Of The _**Second Hand Car**_ , You Want To Sell Or Buy...? :mony:",True)
        st.markdown('''<br>
                            ''', True)
        st.markdown(
            "##### **_Enter The certain information And Click On The Predict Button, And You Can Predict The Price Of Your "
            "Car._** :thought_balloon:")
        st.markdown('''<br>
                        ''', True)
        # ---Image---
        st.image("car.jpg", width=650)


        # ---Prediction---

        years = st.number_input('In which year car was purchased ?', 1990, 2020, step=1, key='year')
        Yrs_old	 = 2021 - years

        st.write("")

        Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key='present_price')

        st.write("")

        Kms_Driven = st.slider('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, key='drived')
        st.write(Kms_Driven)

        st.write("")

        Owner = st.radio("The number of owners the car had previously ?", (0, 1, 3), key='owner')

        st.write("")

        Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?', ('Petrol', 'Diesel', 'CNG'), key='fuel')
        if (Fuel_Type_Petrol == 'Petrol'):
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif (Fuel_Type_Petrol == 'Diesel'):
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        st.write("")

        Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer', 'Individual'),
                                              key='dealer')
        if (Seller_Type_Individual == 'Individual'):
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        st.write("")

        Transmission_Manual = st.selectbox('What is the Transmission Type ?', ('Manual', 'Automatic'), key='manual')
        if (Transmission_Manual == 'Mannual'):
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        st.write("")
        st.write("")

        if st.button("Predict"):
            try:
                result = model.predict([[Present_Price,	Kms_Driven,	Owner,	Yrs_old, Fuel_Type_Diesel,	Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
                output = round(result[0], 2)
                if output < 0:
                    st.warning("You will be not able to sell this car !!")
                else:
                    st.success("The Price Of Your Car Is : {} lakhs....👍".format(output))
            except:
                st.warning("Opps!! Something went wrong\nTry again")

    if __name__ == '__main__':
        main()


    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write("©2021 Ruhan Ahire")










                                         # ----------Graph_Page-------------



if nav == "Graphs":
    st.title("See The Graphs Of The Price Depends On a components. :chart_with_upwards_trend:")

    st.write("")
    st.write("")
    st.write("")



    #-----Graphs-----
    st.markdown(" ###  **Select The Component Withe Which You Want To Compare The Car_Price.**")

    st.write("")

    component = st.selectbox("Components", ['Years', 'Fuel_Type', 'Seller-Type' , 'Km_Driven' , 'Gear_Type', 'Number_Of_Owner'],index=0)

    st.write("")



    # ---Year---
    if component == 'Years':
        st.header("Years VS Price Graph")
        st.write("")
        st.write("_This Graphs Sows The **Price** According To The **Years Of The Car**,The Data Is Give since 1900 To 2020._")

        st.info("_Please Wait...Graph will be appear here..._")

        plt.bar(data['Year'],data['Selling_Price'])
        plt.title('Years  |VS|  rice')
        plt.xlabel("Years")
        plt.ylabel("Price_Range")
        st.pyplot()

        st.set_option('deprecation.showPyplotGlobalUse', False)



    # ---Fuel_Type---
    if component == 'Fuel_Type':
        st.header("Fuel_Type VS Price Graph")
        st.write("")
        st.write("_This Graphs Sows The **Price** According To The **Types Of Fuel** Of The Car, There Are 5 Types Of Fuels And This Graph Sows which One Can Gives You The Beat Price._")

        st.info("_Please Wait...Graph will be appear here..._")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        plt.bar(data['Fuel_Type'], data['Selling_Price'])
        plt.title('Fuel_Type  |VS|  rice')
        plt.xlabel("Fuel_Type")
        plt.ylabel("Price_Range")
        st.pyplot()

        #st.set_option('deprecation.showPyplotGlobalUse', False)




    # ---Seller_Type---
    if component == 'Seller-Type' :
        st.header("Seller_Type VS Price Graph")
        st.write("")
        st.write(
            "_This Graphs Sows The **Price** According To The **Types Of Seller** Of The Car, There Are 4 Types Of Seller And This Graph Sows which Type OF Seller  Can Gives You The Beat Deal Over Your Car._")

        st.info("_Please Wait...Graph will be appear here..._")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        plt.bar(data['Seller_Type'], data['Selling_Price'])
        plt.title('Seller_Type  |VS|  rice')
        plt.xlabel("Seller_Type")
        plt.ylabel("Price_Range")
        st.pyplot()

        #st.set_option('deprecation.showPyplotGlobalUse', False)



    # ---Km_Driven---
    if component == 'Km_Driven':
        st.header("Km_Driven VS Price Graph")
        st.write("")
        st.write(
            "_This Graphs Sows You The **Price** According To The **Km_Driven**, How Much Km. Your Car Is Driven ._")

        st.info("_Please Wait...Graph will be appear here..._")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        plt.figure(figsize=(9, 5))
        plt.scatter(data["Kms_Driven"], data["Selling_Price"])
        plt.ylim(0)
        plt.title('Km_Driven  |VS|  rice')
        plt.xlabel("Km_Driven")
        plt.ylabel("Price_Range")
        st.pyplot()

        #st.set_option('deprecation.showPyplotGlobalUse', False)



    # ---Gear_Types---
    if component == 'Gear_Type':
        st.header("Gear_Type VS Price Graph")
        st.write("")
        st.write(
            "_This Graphs Sows You The **Price** According To The **Type Of Gears**, Which One Gives You The High Price ._")

        st.info("_Please Wait...Graph will be appear here..._")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        plt.figure(figsize=(9, 5))
        plt.bar(data["Transmission"], data["Selling_Price"])
        plt.ylim(0)
        plt.title('Gear_Type  |VS|  rice')
        plt.xlabel("Type_Of_Gears")
        plt.ylabel("Price_Range")
        st.pyplot()

        #st.set_option('deprecation.showPyplotGlobalUse', False)



    # ---Number_Of_Owner---
    if component == 'Number_Of_Owner':
        st.header("Number_Of_Owner VS Price Graph")
        st.write("")
        st.write(
            "_This Graphs Sows You The **Price** According To The **Number_Of_Owner**, That How many Owners have Own The Car In The Past ._")

        st.info("_Please Wait...Graph will be appear here..._")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        plt.figure(figsize=(10, 5))
        plt.bar(data["Owner"], data["Selling_Price"])
        plt.ylim(0)
        plt.title('Number_Of_Owner |VS|  rice')
        plt.xlabel("Number_Of_Owner")
        plt.ylabel("Price_Range")
        st.pyplot()

