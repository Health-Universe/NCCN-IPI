import streamlit as st

def calculate_nccn_ipi(age, ldhl, stage, ecog, extranodal):
    score = 0

    # Age points
    if age <= 40:
        score += 0
    elif 41 <= age <= 60:
        score += 1
    elif 61 <= age <= 75:
        score += 2
    else:
        score += 3

    # LDH points
    if ldhl <= 1:
        score += 0
    elif 1 < ldhl <= 3:
        score += 1
    else:
        score += 2

    # Ann Arbor Stage points
    if stage == 'I':
        score += 0
    elif stage == 'II':
        score += 1
    elif stage == 'III':
        score += 2
    else:
        score += 3

    # ECOG Performance Status points
    if ecog == 0:
        score += 0
    elif ecog == 1:
        score += 1
    elif ecog == 2:
        score += 2
    elif ecog == 3:
        score += 3
    else:
        score += 4

    # Extranodal Sites points
    if extranodal == 0:
        score += 0
    elif extranodal == 1:
        score += 1
    elif extranodal >= 2:
        score += 2

    return score

def main():
    st.title("NCCN-IPI Calculator")
    
    st.write("""
    This app calculates the National Comprehensive Cancer Network International Prognostic Index (NCCN-IPI) for patients with diffuse large B-cell lymphoma (DLBCL). 
    The NCCN-IPI is a tool used by healthcare professionals to predict the prognosis of patients based on specific clinical factors.
    """)

    age = st.number_input("Age", min_value=0, max_value=120, value=50)
    ldhl = st.number_input("Serum LDH level (relative to upper limit of normal)", min_value=0.0, step=0.1, value=1.0)
    stage = st.selectbox("Ann Arbor Stage", options=['I', 'II', 'III', 'IV'])
    ecog = st.selectbox("ECOG Performance Status", options=[0, 1, 2, 3, 4])
    extranodal = st.number_input("Number of extranodal sites", min_value=0, value=0)

    if st.button("Calculate NCCN-IPI"):
        score = calculate_nccn_ipi(age, ldhl, stage, ecog, extranodal)
        st.write(f"The calculated NCCN-IPI score is: {score}")

if __name__ == '__main__':
    main()
