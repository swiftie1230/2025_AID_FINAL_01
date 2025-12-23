import streamlit as st
import pandas as pd

exam_title = "2025 AID FINAL RESULTS"
fname = "Final Exam_01.xlsx"
solution_1 = '''Solution
1. (10p - 2p each) \n
(a) F \n
(b) T \n
(c) T \n
(d) F \n
(e) T \n
'''

solution_2 = '''
2. (8p - 2p each) \n
(a) Ensemble Learning \n 
(b) Unsupervised \n
(c) Reinforcement Learning \n
(d) Active Learning \n
'''

solution_3 = '''
3. (10p) \n
(a) - 3p \n
df.loc is label-based (using row/column names), while df.iloc is integer-index based (using 0-based positions). \n
\n
(b) - 4p \n
df_join = pd.concat([df1, df2], axis=0) \n
\n
(c) - 3p \n
data = json.load(file) \n
'''

solution_4 = '''
4. (8p) \n
(a) - 4p \n
def euclidean_distance(row1, row2): \n
    distance = 0.0 \n
    for i in range(len(row1) - 1): \n
        distance += (row1[i] - row2[i])**2 \n
    return math.sqrt(distance) \n
\n
(b)  - 4p \n
Standard scaling ensures all features contribute equally to the distance calculation. Since kNN relies on distance, features with larger scales would otherwise dominate the results. \n
'''

solution_5 = '''
5. (10p) \n
(a) - 6p \n
(1) Missing completely at random: (Y) (2) Missing at random: (X) (3) Missing not at random: (Z) \n
(b) - 4p \n
def min_max_normalize_2d(array): \n
    return (array - array.min(axis=0)) / (array.max(axis=0) - array.min(axis=0)) \n

other solutions: \n
import pandas as pd \n
def min_max_normalize_pandas(df): \n
    df = pd.DataFrame(ax) \n
    return (df - df.min()) / (df.max() - df.min()) \n
'''

solution_6 = '''
6. (14p)
(a) - 4p \n 
375, 25 \n
\n
(b) - 6p \n
0.5, 0.25, 0.8 (%로 적어도 무관) \n
\n
(c) - 4p \n
Accuracy can be misleading because model can achieve a high score by simply predicting the majority class for every instance, failing to detect the minority class entirely. \n
\n
'''

solution_7_a = '''
7. (15p) \n
(a) (11p) \n
'''

code_7_a = '''
df.plot(x='Month', y=['Seoul', 'Daegu'], marker='o') 
plt.title("Monthly Temperature") 
plt.xlabel("Month") 
plt.ylabel("Temp") 
plt.legend() 
plt.grid(True) 
plt.show()
'''

solution_7_b = '''
(b) (4p) \n
'''

code_7_b = '''
plt.plot(x, y, color='red', linestyle='--', marker='o')
(or plt.plot(x, y, 'r--o'))
'''

solution_8 = '''
7. (15p) \n
(a) (3p) \n
The entrypoint file is the main script run to start the app. Additional pages are organized in a sub-folder named "pages". \n
\n
(b) (9p) \n
Answer (1): selectbox Answer (2): slider Answer (3): text_input \n

'''

solution_9 = '''
9. (13p) \n
(a) (3p) \n
It lists all the dependencies and libraries (and their versions) required to run the project. \n 
\n
(b)(4p) \n
conda create -n ai_exam python=3.9 \n
\n
(c) (6p) \n
Reset of add execution (un-staging a file): This removes a file from the staging area but leaves the modifications in your working directory. \n
This is done wiwth git reset <file> (or git reset HEAD <file>). \n 
'''

code_9_c = '''
# Project Plan
## Milestones
* Design
* Develop
* Test

```python
print("Start Project")

'''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df = pd.read_excel(fname)

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Enter your email", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        to_show = data.set_index("e-mail")
        st.write("E-mail: ", to_show.index[0])
        s = to_show.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
        st.dataframe(s, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")
        
st.write(solution_1)  
st.markdown("""---""")
st.write(solution_2)  
st.markdown("""---""")
st.write(solution_3)  
st.markdown("""---""")
st.write(solution_4)  
st.markdown("""---""")
st.write(solution_5)  
st.markdown("""---""")
st.write(solution_6)
st.markdown("""---""")  
st.write(solution_7_a) 
st.code(code_7_a, language='python')
st.write(solution_7_b) 
st.code(code_7_b, language='python')
st.markdown("""---""")
st.write(solution_8) 
st.markdown("""---""")
st.write(solution_9) 
st.code(code_9_c, language='python')
st.markdown("""---""")
