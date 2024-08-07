# # import os
# # import folium
# # import tempfile
# # import subprocess
# # import pandas as pd
# # import streamlit as st
# # from streamlit_folium import st_folium
# # from jinja2 import Template

# # # #Page Setup
# # st.set_page_config(
# #    page_title="MOEST Exam Center Calculator",
# #    page_icon=":school:",
# # #    page_icon="https://avatars.githubusercontent.com/u/167545222?s=200&v=4", # official logo
# #    layout="wide",
# #    initial_sidebar_state="expanded",
# # )

# # #  Custom CSS 
# # custom_css = """
# # <style>
# # .st-ag.st-e4.st-e5 {
# #     flex-direction: row !important;
# # }
# # </style>
# # """
# # legend_template = """
# # {% macro html(this, kwargs) %}
# # <div id='maplegend' class='maplegend' 
# #     style='position: absolute; z-index: 9999; background-color: rgba(255, 255, 255, 0.65);
# #      border-radius: 6px; padding: 10px; font-size: 10.5px; right: 15px; top: 15px; border: 2px solid black;'>     
# # <div class='legend-scale'>
# #   <ul class='legend-labels'>
# #     <li style='font-size:18px;margin-bottom:5px;'><span style='background: #0096FF; opacity: 0.75;'></span>School</li>
# #     <li style='font-size:18px;'><span style='background: #C41E3A; opacity: 1.75;'></span>Center</li>
# #   </ul>
# # </div>
# # </div> 
# # <style type='text/css'>
# #   .maplegend .legend-scale ul {margin: 0; padding: 0; color: #0f0f0f;}
# #   .maplegend .legend-scale ul li {list-style: none; line-height: 18px; margin-bottom: 1.5px;}
# #   .maplegend ul.legend-labels li span {float: left; height: 16px; width: 16px; margin-right: 4.5px;}
# # </style>
# # {% endmacro %}
# # """
# # # Render custom CSS
# # st.markdown(custom_css, unsafe_allow_html=True)

# # # Session setup
# # if 'calculate_clicked' not in st.session_state:
# #     st.session_state.calculate_clicked = False
# # if 'calculation_completed' not in st.session_state:
# #     st.session_state.calculation_completed = False
# # if 'calculated_data' not in st.session_state:
# #     st.session_state.calculated_data = {}
# # if 'filter_type' not in st.session_state:
# #     st.session_state.filter_type = None
# # if 'filter_value' not in st.session_state:
# #     st.session_state.filter_value = None

# # #Maps setup
# # m = folium.Map(location=[27.7007, 85.3001], zoom_start=12, )

# # # Add Legend in map
# # macro = folium.MacroElement()
# # macro._template = Template(legend_template)
# # m.get_root().add_child(macro)

# # fg = folium.FeatureGroup(name="Allocated Centers")

# # #Sidebar
# # with st.sidebar:

# #     add_side_header = st.sidebar.title("Random Center Calculator")

# #     schools_file = st.sidebar.file_uploader("Upload School/College file", type="tsv")
# #     centers_file = st.sidebar.file_uploader("Upload Centers file", type="tsv")
# #     prefs_file = st.sidebar.file_uploader("Upload Preferences file", type="tsv")

# #     calculate = st.sidebar.button("Calculate Centers", type="primary", use_container_width=True)

# # school_df = None
# # # Tabs
# # tab1, tab2, tab3, tab4, tab5 = st.tabs([
# #     "School Center",
# #     "School Center Distance",
# #     "View School Data",
# #     "View Centers Data",
# #     "View Pref Data" 
# #     ])

# # tab1.subheader("School Center")
# # tab2.subheader("School Center Distance")
# # tab3.subheader("School Data")
# # tab4.subheader("Center Data")
# # tab5.subheader("Pref Data")

# # # Show data in Tabs as soon as the files are uploaded
# # if schools_file:
# #     df = pd.read_csv(schools_file, sep="\t")
# #     school_df = df
# #     tab3.dataframe(df)
    
# # else:
# #     tab3.info("Upload data to view it.", icon="ℹ️")

# # if centers_file:
# #     df = pd.read_csv(centers_file, sep="\t")
# #     tab4.dataframe(df)
# # else:
# #     tab4.info("Upload data to view it.", icon="ℹ️")

# # if prefs_file:
# #     df = pd.read_csv(prefs_file, sep="\t")
# #     tab5.dataframe(df)
# # else:
# #     tab5.info("Upload data to view it.", icon="ℹ️")


# # # Function to run the center randomizer program
# # def run_center_randomizer(schools_tsv, centers_tsv, prefs_tsv):
# #     cmd = f"python school_center.py {schools_tsv} {centers_tsv} {prefs_tsv}"
# #     subprocess.run(cmd, shell=True)

# # #Function to filter the data
# # def filter_data(df, filter_type, filter_value):
# #     if filter_type in df.columns:
# #         df = df[df[filter_type] == filter_value]
# #         return df
# #     else:
# #         st.error(f"{filter_type} is not a valid column in the DataFrame.")
# #         return pd.DataFrame() 
    
# # # Run logic after the button is clicked
# # if calculate:
# #     st.session_state.calculate_clicked = True
    
# #     def save_file_to_temp(file_obj):
# #         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
# #             file_obj.seek(0)  # Go to the start of the file
# #             temp_file.write(file_obj.read())
# #             return temp_file.name
    
# #     if st.session_state.calculate_clicked:
# #         # Ensure all files are uploaded
# #         if schools_file and centers_file and prefs_file:
# #             schools_path = save_file_to_temp(schools_file)
# #             centers_path = save_file_to_temp(centers_file)
# #             prefs_path = save_file_to_temp(prefs_file)

# #             # Run the program with the temporary file paths
# #             run_center_randomizer(schools_path, centers_path, prefs_path)
# #             st.toast("Calculation successful!", icon="🎉")
# #             st.session_state.calculation_completed = True

# #             # Delete the temporary files after use
# #             os.unlink(schools_path)
# #             os.unlink(centers_path)
# #             os.unlink(prefs_path)

# #             # Set the paths for the output files[UPDATE LATER TO BE FLEXIBLE]
# #             school_center_file = "results/school-center.tsv"
# #             school_center_distance_file = "results/school-center-distance.tsv"

# #             # Store calculated data in session state
# #             if school_center_file and school_center_distance_file:
# #                 st.session_state.calculated_data['school_center'] = school_center_file
# #                 st.session_state.calculated_data['school_center_distance'] = school_center_distance_file
# #             else:
# #                 tab1.error("Calculated data not found", icon="🚨")

# #         else:
# #             st.sidebar.error("Please upload all required files.", icon="🚨")

# # elif not st.session_state.calculate_clicked:
# #     tab1_msg = tab1.info("Results will be shown only after the calculation is completed.", icon="ℹ️")
# #     tab2_msg = tab2.info("Results will be shown only after the calculation is completed.", icon="ℹ️")

# # if st.session_state.calculate_clicked and st.session_state.calculation_completed:
# #     # Display data from session state
# #     if 'school_center' in st.session_state.calculated_data:
# #         df_school_center = pd.read_csv(st.session_state.calculated_data['school_center'], sep="\t")
# #         allowed_filter_types = ['school', 'center']
# #         st.session_state.filter_type = tab1.radio("Choose a filter type:", allowed_filter_types)

# #         # Display an input field based on the selected filter type
# #         if st.session_state.filter_type:
# #          if st.session_state.filter_type == 'school':
# #           # Create filter options with school name and code
# #           filter_options = [f"{code} | {name}" for name, code in zip(df_school_center['school'].unique(), df_school_center['scode'].unique())]

# #          elif st.session_state.filter_type == 'center':
# #           # Create filter options with center name and code
# #           filter_options = [f"{code} | {name}" for name, code in zip(df_school_center['center'].unique(), df_school_center['cscode'].unique())]

# #          # Display a selectbox for selection
# #          st.session_state.filter_value = tab1.selectbox(f"Select a value for {st.session_state.filter_type}:", filter_options)

# #          # Split the selected value to extract name and code
# #          code, name = st.session_state.filter_value.split(' | ')

# #          # Filter the DataFrame based on the selected type and value
# #          filtered_df = filter_data(df_school_center, st.session_state.filter_type, name)

# #         if st.session_state.filter_value:
# #             # Remove thousand separator comma in scode and cscode 
# #             styled_df  = filtered_df.style.format({
# #               "cscode": lambda x: '{:.0f}'.format(x),
# #                "scode": lambda x: '{:.0f}'.format(x)
# #             })
# #             tab1.dataframe(styled_df , hide_index=True)
# #             tab1.subheader('Map')
# #             tab1.divider()
# #             for index, center in filtered_df.iterrows():
# #                 fg.add_child(
# #                     folium.Marker(
# #                         location=[center.center_lat, center.center_long],
# #                         popup=f"{(center.center).title()}\nAllocation: {center.allocation}",
# #                         tooltip=f"{center.center}",
# #                         icon=folium.Icon(color="red")
# #                     )
# #                 )
                
# #             # Initialize an empty dictionary to store school coordinates
# #             filtered_schools = {}  
              
# #             if school_df is not None:
              
# #               for index, row in school_df.iterrows():                       
# #                scode = row['scode']
# #                school_lat = row['lat']
# #                school_long = row['long']
 
# #                if scode in filtered_df['scode'].values:
# #                   filtered_schools.setdefault(scode, []).append((school_lat, school_long))
                 
# #               for index, school in filtered_df.iterrows():
# #                lat_long_list = filtered_schools.get(school['scode'], [])
             
# #                for school_lat, school_long in lat_long_list:
# #                 if school_lat is not None and school_long is not None:
# #                  fg.add_child(
# #                  folium.Marker(
# #                     location=[school_lat, school_long],
# #                     popup=f"{school['school'].title()}\nAllocation: {school['allocation']}",
# #                     tooltip=f"{school['school']}",
# #                     icon=folium.Icon(color="blue")
# #                  )
# #                 )
                 
# #             m.add_child(fg)
# #             with tab1:
# #                 st_folium( m, width=1200, height=400)
        
# #         tab1.divider()
# #         tab1.subheader('All Data')
# #         tab1.dataframe(df_school_center)
# #     else:
# #         tab1.info("No calculated data available.", icon="ℹ️")
    
# #     if 'school_center_distance' in st.session_state.calculated_data:
# #         df = pd.read_csv(st.session_state.calculated_data['school_center_distance'], sep="\t")
# #         tab2.dataframe(df)

# #     else:
# #         tab2.error("School Center Distance file not found.")

# # elif st.session_state.calculate_clicked and not st.session_state.calculated_data:
# #     tab1.error("School Center data not found in session state.")

# # a = 9
# # b = 3
# # c = 17

# # print(a & a)

# # a='zombie'
# # b=a.maketrans('zmi','rls')
# # print (b)

# # lst= [3,5,3,9,1]
# # lst.pop(lst[2])
# # print(lst)


# # j=1
# # while True:
# #     if j%2==0:
# #         break
# # print(j)
# # j+=2


# # A =[[1, 2, 31],[4, 5, 61],[7, 8, 911]]

# # # output 6
# # print(A[1][2])

# # print( 'hello'.capitalize('h'))
# # print('hello {0} {1} {2}'.format(10, 20, 30))


# # a = [3, -7, 5, -2]
# # i = 0  # Corrected:  Use 'i' instead of '1' for the variable name
# # fact = 2
# # while i < 3:
# #     fact = fact * a[i] + 1
# #     i = i + 1 
# # print(fact)


# a = 1 

# def outer():
#     b = 3

#     def inner():
#         nonlocal b  # This is crucial!
#         b = b + 3
#         c = 13
#     print(b)  # Output: 6
#     # return None #implicitly returned
#     print(inner()) # Output: None 6 13 (from inner function)
#     print(b)       # Output: 6 (modified by inner)
#     # return None #implicitly returned

# print(outer()) 




# i = -2
# j = -1
# k = -3

# if i < k:   
#     k = 3
#     if k > 2: 
#         k = 4
#     else: 
#         i = j 
# else:
#     if j >= -3: 
#         i = 3
#     else:
#         j = i 
# print(j, i, k) 

# i = -2
# j = -1
# k = -3

# if j < k:
#     k = 3
#     if k > 2:
#         k = 4
#     else:
#         i = j
# elif i >= -3:  # Assuming you meant to compare 'i' 
#     i = 3
# else:
#     j = i

# print(j, i, k) 



# a = 1

# def outer():
#     b = 3

#     def inner():
#         nonlocal b  
#         b = b + 3
#         c = 13
#         print(b)     # Output: 6
#         sum = 3
#         for i in range(4):
#             sum = sum + 1
#         return sum   

#     return inner()  # Return the result of calling inner()

# print(outer())  

