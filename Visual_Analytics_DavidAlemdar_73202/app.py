import streamlit as st
from PIL import Image

def show_image(image_path, width=None, height=None, use_column_width=True):
    image = Image.open(image_path)
    if width and height:
        image = image.resize((width, height))
    elif width:
        image = image.resize((width, int(width * image.size[1] / image.size[0])))
    elif height:
        image = image.resize((int(height * image.size[0] / image.size[1]), height))
    st.image(image, use_column_width=use_column_width)




def page():
    image_xcm_confusion_matrix = "XCM_95_ConfusionMatrix.png"
    image_xcm_proba_bubbles = "XCM_95_Proba_Bubbles.png"
    image_xcm_result_table = "XCM_95_Result_Table_50Epoch.png"
    image_xcm_pred_visual = "XCM_95_Pred_Visual.png"
    image_feature_importance = "XCM_95_Featureimportance_Permutation_Class2and3.png"
    image_stepimportance = "XCM_95_Stepimportance_Permutation_Class2and3.png"
    image_dataset = "NATOPS_DATASET.png"
    image_plot_classes = "Plots of classes and its features.png"
    image_channel_explain = "NATOPS_Channel_explain.png"
    image_data_info = "NATOPS_Data_Info.png"
    image_xcm_architecture = "XCM_architecture.png"
    image_xcm_archi_explaination = "XCM_architecture_explaination.png"
    image_xcm_95_grad_beob_data1 = "XCM_95_GRAD_BEOBV_DATA0.png"
    image_xcm_95_grad_beob_data2 = "XCM_95_GRAD_BEOBV_DATA1.png"
    image_xcm_95_grad_beob_data3 = "XCM_95_GRAD_BEOBV_DATA2.png"
    image_xcm_95_grad_beob_data4 = "XCM_95_GRAD_BEOBV_DATA3.png"
    image_xcm_95_grad_beob_data5 = "XCM_95_GRAD_BEOBV_DATA4.png"
    image_xcm_95_grad_beob_data6 = "XCM_95_GRAD_BEOBV_DATA5.png"
    image_xcm_95_grad_beob_data7 = "XCM_95_GRAD_BEOBV_DATA6.png"
    image_xcm_95_grad_beob_data8 = "XCM_95_GRAD_BEOBV_DATA7.png"
    image_xcm_95_grad_beob_data9 = "XCM_95_GRAD_BEOBV_DATA8.png"

    image_xcm_95_grad_time_data1 = "XCM_95_GRAD_TIME_DATA0.png"
    image_xcm_95_grad_time_data2 = "XCM_95_GRAD_TIME_DATA1.png"
    image_xcm_95_grad_time_data3 = "XCM_95_GRAD_TIME_DATA2.png"
    image_xcm_95_grad_time_data4 = "XCM_95_GRAD_TIME_DATA3.png"
    image_xcm_95_grad_time_data5 = "XCM_95_GRAD_TIME_DATA4.png"
    image_xcm_95_grad_time_data6 = "XCM_95_GRAD_TIME_DATA5.png"
    image_xcm_95_grad_time_data7 = "XCM_95_GRAD_TIME_DATA6.png"
    image_xcm_95_grad_time_data8 = "XCM_95_GRAD_TIME_DATA7.png"
    image_xcm_95_grad_time_data9 = "XCM_95_GRAD_TIME_DATA8.png"


    st.title("XAI for classification of multivariate timeseries")

    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)


    tabs = st.tabs(["Approach", "Classification results", "Explanation Classes 2 & 3"])

    with tabs[0]:
      st.header("XCM Model on the multivariate timeseries dataset 'NATOPS'")
      st.write("This dashboard provides results of the classification and also global and local explanation approaches are shown such as permutation (Feature / Step Importance) and GRAD-CAM.")
      st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)
      col1, col2, col3 = st.columns(3, gap = "medium")
      with col1:
          st.header("Dataset 'NATOPS'")
          show_image(image_dataset, use_column_width=True)

      with col2:
          st.header("Dataset Informations")
          show_image(image_data_info)
          expander = st.expander("Channel Explanation", expanded = True)
          with expander:
            show_image(image_channel_explain)

          show_image(image_plot_classes)

      with col3:
          st.header("XCM Architecture")
          expander = st.expander("XCM (Describtion)", expanded = True)
          with expander:  
            show_image(image_xcm_archi_explaination)
          show_image(image_xcm_architecture, width = 500, height = 300, use_column_width=True)
      st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)



    with tabs[1]:
        col1, col2, col3 = st.columns(3, gap = "medium")
        with col1:
          st.header("Metrices & ConfusionMatrix")
          show_image(image_xcm_result_table)
          show_image(image_xcm_confusion_matrix, width=500, height=400, use_column_width=True)
        with col2:
          st.header("Prediction probabilities of classes")
          show_image(image_xcm_proba_bubbles)
        with col3:
          st.header("Sample of predicted classes")
          show_image(image_xcm_pred_visual)

        st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)


    with tabs[2]:
        col1, col2 = st.columns(2, gap = "medium")
 
        with col1:
          expander = st.expander("Feature Importance (Global)", expanded = True)
          with expander:

            st.markdown("<h2 style='text-align: center;'>Feature Importance (Global)</h2>", unsafe_allow_html=True)
            show_image(image_feature_importance)


          expander = st.expander("Step Importance (Global)", expanded = False)
          with expander:

            st.markdown("<h2 style='text-align: center;'>Step Importance (Global)</h2>", unsafe_allow_html=True)        
            show_image(image_stepimportance)


        with col2:

          expander = st.expander("Feature Importance (Lokal)", expanded = True)
          with expander:
            st.markdown("<h2 style='text-align: center;'>Feature Importance (Lokal)</h2>", unsafe_allow_html=True)
            image_options = {
                "1. Datainstance": image_xcm_95_grad_beob_data1,
                "2. Datainstance": image_xcm_95_grad_beob_data2,
                "3. Datainstance": image_xcm_95_grad_beob_data3,
                "4. Datainstance": image_xcm_95_grad_beob_data4,
                "5. Datainstance": image_xcm_95_grad_beob_data5,
                "6. Datainstance": image_xcm_95_grad_beob_data6,
                "7. Datainstance": image_xcm_95_grad_beob_data7,
                "8. Datainstance": image_xcm_95_grad_beob_data8,
                "9. Datainstance": image_xcm_95_grad_beob_data9
            }
            selected_image = st.selectbox("Grad-Cam for features", list(image_options.keys()))
            show_image(image_options[selected_image])

          expander = st.expander("Step Importance (Lokal)", expanded = False)
          with expander:         
            st.markdown("<h2 style='text-align: center;'>Step Importance (Lokal)</h2>", unsafe_allow_html=True)
 
            image_options2 = {
                "1. Datainstance": image_xcm_95_grad_time_data1,
                "2. Datainstance": image_xcm_95_grad_time_data2,
                "3. Datainstance": image_xcm_95_grad_time_data3,
                "4. Datainstance": image_xcm_95_grad_time_data4,
                "5. Datainstance": image_xcm_95_grad_time_data5,
                "6. Datainstance": image_xcm_95_grad_time_data6,
                "7. Datainstance": image_xcm_95_grad_time_data7,
                "8. Datainstance": image_xcm_95_grad_time_data8,
                "9. Datainstance": image_xcm_95_grad_time_data9
            }
            selected_image = st.selectbox("Grad-Cam for time sequences", list(image_options2.keys()))
            show_image(image_options2[selected_image], width = 500, height = 270, use_column_width=True)
        st.markdown("<hr style='border:1px solid black'>", unsafe_allow_html=True)


    css = '''
    <style>
      .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
        display: flex;
        justify-content: center;
        padding: 50px;
        }
      .centered-col {
       display: flex;
       justify-content: center;
       align-items: center;
       }

    </style>
    '''

    centered_image_css = """
      display: flex;
      justify-content: center;
      """

    st.markdown(css, unsafe_allow_html=True)



def main():
    st.set_page_config(page_title="XAI Dashboard", layout="wide")
    page()	

if __name__ == "__main__":
    main()