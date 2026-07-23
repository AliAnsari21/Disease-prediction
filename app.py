import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

dia_model=pickle.load(open("diabetespred.sav",'rb'))
heart_model=pickle.load(open("heartpred.sav",'rb'))
par_model=pickle.load(open("parpred.sav",'rb'))

#siderbar for navigation
with st.sidebar:
    selected =option_menu('E- Doctor Multiple Diease Prediction',

                         ['Diabetes prediction',
                          'Heart Disease prediction',
                          'Parkinsons prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

#diabetes pred page
if(selected == 'Diabetes prediction'):
    st.title('Diabetes prediction using ML')
    #getting input data 
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of pregnencies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Blood pressure level')
    with col1:
        SkinThickness=st.text_input('Skin Thickness level')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI level')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
        Age=st.text_input('Age')

    #code for pred
    diab_diagnosis=''

    #creating button for pred
    if st.button('Diabetes test result'):
        diab_prediction=dia_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0]==1):
            diab_diagnosis=('the person is diabetic')
        else:
            diab_diagnosis=('the person is not diabetic')

    st.success(diab_diagnosis)

#heart pred page
if (selected == 'Heart Disease prediction'):
    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input('Persons Age')
    with col2:
        sex=st.text_input('Persons Gender')
    with col3:
        cp=st.text_input('CP Value')
    with col1:
        trestbps=st.text_input('trestbps value')
    with col2:
        chol=st.text_input('chol value')
    with col3:
        fbs=st.text_input('fbs value')
    with col1:
        restecg=st.text_input('restecg value')
    with col2:
        thalach=st.text_input('thalach value')
    with col3:
        exang=st.text_input('exang value')
    with col1:
        oldpeak=st.text_input('oldpeak value')
    with col2:
        slope=st.text_input('slope value')
    with col3:
        ca=st.text_input('ca value')
    with col1:
        thl=st.text_input('thal value')

    #code for pred
        heart_diagnosis=''
    
        #creating button for pred
        if st.button('Heart test result'):
            heart_prediction=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
            if (heart_prediction[0]==1):
                heart_diagnosis=('the person is heart disease affected')
            else:
                heart_diagnosis=('the person is not heart disease affected')
    
        st.success(heart_diagnosis)

#parkinsons pred page
if(selected == 'Parkinsons prediction'):
    col1,col2,col3=st.columns(3)

    with col1:
        MDVP_Fo_Hz=st.text_input('MDVP:Fo(Hz) value')
    with col2:
        MDVP_Fhi_Hz=st.text_input('MDVP:Fhi(Hz) value')
    with col3:
        MDVP_Flo_Hz=st.text_input('MDVP:Flo(Hz) Value')
    with col1:
        MDVP_Jitter_per=st.text_input ('MDVP:Jitter(%) value')
    with col2:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs) value')
    with col3:
        MDVP_RAP=st.text_input('MDVP:RAP value')
    with col1:
        MDVP_PPQ=st.text_input('MDVP:PPQ value')
    with col2:
        Jitter_DDP=st.text_input('Jitter:DDP value')
    with col3:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer value')
    with col1:
        MDVP_Shimmer_dB=st.text_input('MDVP:Shimmer(dB) value')
    with col2:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3 value')
    with col3:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5 value')
    with col1:
        MDVP_APQ=st.text_input('MDVP:APQ value')
    with col2:
        Shimmer_DDA=st.text_input('Shimmer:DDA value')
    with col3:
        NHR=st.text_input('NHR Value')
    with col1:
        HNR=st.text_input('HNR value')
    with col2:
        RPDE=st.text_input('RPDE value')
    with col3:
        DFA=st.text_input('DFA value')
    with col1:
        spread1=st.text_input('spread1 value')
    with col2:
        spread2=st.text_input('spread2 value')
    with col3:
        D2=st.text_input('D2 value')
    with col1:
        PPE=st.text_input('PPE value')
    

    #code for pred
        par_diagnosis=''
    
        #creating button for pred
        if st.button('Parkinsons test result'):
            par_prediction=par_model.predict([[MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_per,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
    
            if (par_prediction[0]==1):
                par_diagnosis=('the person is Parkinsons disease affected')
            else:
                heart_diagnosis=('the person is not Parkinsons disease affected')
    
        st.success(par_diagnosis)