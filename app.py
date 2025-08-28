import streamlit as st

# --- SCORING FUNCTION ---
def calcscore(ques, choose):
    options = {"a": 0, "b": 1, "c": 2, "d": 3}
    posn = options.get(choose, 0)

    quesone   = [5, 15, 0, 10]
    questwo   = [0, 10, 3, 7]
    questhree = [10, 6, 0, 3]
    quesfour  = [0, 10, 3, 6]
    quesfive  = [15, 20, 0, 10]
    quessix   = [0, 25, 15, 5]
    quesseven = [6, 3, 10, 0]

    score = [quesone, questwo, questhree, quesfour, quesfive, quessix, quesseven]
    return score[ques][posn]

# --- QUESTIONS & OPTIONS ---
questions = [
    ("Do you understand the purpose of life?", [
        "I have a fairly good understanding of the purpose of life",
        "I am not really sure what the purpose of life is",
        "I perfectly understand the purpose of life",
        "I think I have some idea about the purpose of life"
    ]),
    ("Can you dedicate some time regularly to study and acquire new knowledge?", [
        "I am very busy and have no time for study",
        "I am very willing to dedicate time to acquire knowledge",
        "I can find time once in a while for this",
        "I should be able to create some time to study for knowledge"
    ]),
    ("Would you be willing to carry out tested and tried experiments and exercises with your body and mind?", [
        "I am ready to carry out experiments and exercises with my body and mind",
        "I will make my choice on this when I see the experiment or exercise",
        "I am not really interested in experimenting with my body and mind",
        "I am not really ready but I can try some"
    ]),
    ("When you go to a place for the first time, do you find it easy to remember what you saw?", [
        "I find it difficult to recollect what I see",
        "I easily recollect all I have seen after visiting a place",
        "I am able to recollect just a few things",
        "With some effort, I can recollect what I have seen"
    ]),
    ("What makes you accept new ideas you learn as being accurate?", [
        "If a new idea makes sense to me, I will accept it",
        "I only fully accept new ideas after the truth in them is demonstrated",
        "I accept new ideas from people I look up to",
        "I accept new ideas from authorities on the subject"
    ]),
    ("How would you rate yourself in terms of your personal abilities?", [
        "My personal abilities are far below average",
        "My personal abilities are above average",
        "My personal abilities are average",
        "My personal abilities are at a level of excellence"
    ]),
    ("What is your view on taking risks?", [
        "It is sometimes necessary to take risks but not often",
        "I take any kind of risk to get what I want",
        "It is okay to take calculated risks",
        "I do not believe in taking any kind of risk"
    ]),
]

# --- STREAMLIT APP ---
st.title("🧭 AMORC Membership Application Quiz")

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0

q_index = st.session_state.current_q
question, options = questions[q_index]

st.subheader(question)
choice = st.radio("Choose one:", ["a", "b", "c", "d"], format_func=lambda x: options[["a","b","c","d"].index(x)])

if st.button("Next"):
    st.session_state.score += calcscore(q_index, choice)
    st.session_state.current_q += 1

    if st.session_state.current_q == len(questions):
        score = st.session_state.score
        st.success(f"🎯 Your total score is {score}%")

        if score > 79:
            st.write("✅ Your chances of doing well are **EXCELLENT**")
        elif 65 <= score <= 79:
            st.write("👍 Your chances are **VERY GOOD**")
        elif 50 <= score <= 64:
            st.write("🙂 Your chances are **GOOD**")
        elif 32 <= score <= 49:
            st.write("😐 Your chances are **FAIR**")
        else:
            st.write("⚠️ Your chances are **POOR**")

        # Reset option
        if st.button("Restart"):
            st.session_state.current_q = 0
            st.session_state.score = 0
