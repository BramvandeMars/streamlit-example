import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("gemeenteScore.csv")
st.title("Risico Cybercrime in de Nederlandse gemeentes")
# st.write(df)

label = "Risico"
df = df.reset_index(drop=True)
with st.form("risico per thema en gemeente"):
    # text_val = st.text_input(label, placeholder="Zoek hier op gemeente...")
    int_val = st.number_input(label , max_value=4, min_value=1)
    submitted = st.form_submit_button("Zoek")
    if submitted:
        st.write("Risico score: ", int_val)
        st.write(df[['gemeente','thema', 'risico_score']].loc[df['risico_score'] == int_val])
        fig, ax = plt.subplots()
        ax.hist(df['risico_score'], bins=20)
        st.pyplot(fig)
        # st.pyplot(sns.lineplot(data=df, x='gemeente', y='risico_score'))
