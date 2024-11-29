import streamlit as st
import pickle 
#set the title and an image for the web app
st.title("Welcome")
st.image("image.png")

#load the pre-trained model
with open('titanicpickle.pkl', 'rb') as pickle_file:
    pickle_load_file = pickle.load(pickle_file)


    #function to make predictions
def PredictionFunction(Pclass,Sex, Age,SibSp, Parch, Fare, Embarked):
    prediction = pickle_load_file.predict([[Pclass,Sex, Age,SibSp, Parch, Fare, Embarked]])
    print(prediction) #0/1
    return prediction

def main():
    st.title('Titanic Predictiin App!')
    #the follwoing code created the input fields that will be used by the user
    #for tdata entry for predictin
    Pclass = st.text_input('Passenger Class')
    Sex = st.text_input('Sex')
    Age = st.text_input('Age')
    SibSp = st.text_input('Sibling/Spouse')
    Parch = st.text_input('Parent/Child')
    Fare = st.text_input('Fare')
    Embarked = st.text_input('Embarked')
    result = ''
#This code ensures that when the button 'predict' is clicked, the PredictionFunction
#Which is defined above is called to make the prediction and store in the variable 
#'result'

    if st.button('Predict'):
        #convert the inputs to appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)
        result  = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f'The output is: {result}')

main()
