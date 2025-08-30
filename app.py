import streamlit as st

# -----------------------------
# Scoring Function (same as original)
# -----------------------------
def calcscore(ques, choose):
    if choose == 'a':
        posn = 0
    elif choose == 'b':
        posn = 1
    elif choose == 'c':
        posn = 2
    elif choose == 'd':
        posn = 3
    else:
        return 0  # Invalid choice safety

    quesone = [5,15,0,10]
    questwo = [0,10,3,7]
    questhree = [10,6,0,3]
    quesfour = [0,10,3,6]
    quesfive = [15,20,0,10]
    quessix = [0,25,15,5]
    quesseven = [6,3,10,0]

    score = [quesone, questwo, questhree, quesfour, quesfive, quessix, quesseven]
    return score[ques][posn]

# -----------------------------
# Questions + Options
# -----------------------------
questions = [
    ("Do you understand the purpose of life?", 
     ["I have a fairly good understanding of the purpose of life",
      "I am not really sure what the purpose of life is",
      "I perfectly understand the purpose of life",
      "I think I have some idea about the purpose of life"]),
    
    ("Can you dedicate some time regularly to study and acquire new knowledge?", 
     ["I am very busy and have no time for study",
      "I am very willing to dedicate time to acquire knowledge",
      "I can find time once in a while for this",
      "I should be able to create some time to study for knowledge"]),
    
    ("Would you be willing to carry out tested and tried experiments and exercises with your body and mind?", 
     ["I am ready to carry out experiments and exercises with my body and mind",
      "I will make my choice on this when I see the experiment or exercise",
      "I am not really interested in experimenting with my body and mind",
      "I am not really ready but I can try some"]),
    
    ("When you go to a place for the first time, do you find it easy to remember what you saw?", 
     ["I find it difficult to recollect what I see",
      "I easily recollect all I have seen after visiting a place",
      "I am able to recollect just a few things",
      "With some effort, I can recollect what I have seen"]),
    
    ("What makes you accept new ideas you learn as being accurate?", 
     ["If a new idea makes sense to me, I will accept it",
      "I accept only fully accept new ideas after the truth in them is demonstrated",
      "I accept new ideas from people I look up to",
      "I accept new ideas from authorities on the subject"]),
    
    ("How would you rate yourself in terms of your personal abilities?", 
     ["My personal abilities are far below average",
      "My personal abilities are above average",
      "My personal abilities are average",
      "My personal abilities are at a level of excellence"]),
    
    ("What is your view on taking risks?", 
     ["It is sometimes necessary to take risks but not often",
      "I take any kind of risk to get what I want",
      "It is okay to take calculated risks",
      "I do not believe in taking any kind of risk"])
]

# -----------------------------
# Streamlit App
# -----------------------------
st.title("Rosicrucian Quiz")
st.write("Answer the following questions to see your chances of doing well as a Rosicrucian.")

# Initialize session state
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "totscore" not in st.session_state:
    st.session_state.totscore = 0

# Get current question
if st.session_state.q_index < len(questions):
    question, options = questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index+1}")
    choice = st.radio(question, options, key=f"q{st.session_state.q_index}")

    if st.button("Next"):
        # Map chosen option back to 'a', 'b', 'c', 'd'
        letter_map = {0:'a', 1:'b', 2:'c', 3:'d'}
        answer_letter = letter_map[options.index(choice)]

        # Update score
        st.session_state.totscore += calcscore(st.session_state.q_index, answer_letter)

        # Go to next question
        st.session_state.q_index += 1
        st.rerun()

else:
    # Show final results
    st.success(f"Your final score is {st.session_state.totscore}%")

    if st.session_state.totscore > 79:
        st.write("YOUR CHANCES OF DOING WELL AS A ROSICRUCIAN ARE **EXCELLENT**")
    elif 65 <= st.session_state.totscore <= 79:
        st.write("YOUR CHANCES OF DOING WELL AS A ROSICRUCIAN ARE **VERY GOOD**")
    elif 50 <= st.session_state.totscore <= 64:
        st.write("YOUR CHANCES OF DOING WELL AS A ROSICRUCIAN ARE **GOOD**")
    elif 32 <= st.session_state.totscore <= 49:
        st.write("YOUR CHANCES OF DOING WELL AS A ROSICRUCIAN ARE **JUST FAIR**")
    else:
        st.write("YOUR CHANCES OF DOING WELL AS A ROSICRUCIAN ARE **POOR**")

    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.totscore = 0
        st.rerun()

