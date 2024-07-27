import streamlit as st
from Home import main as home
from CIDGI_survey import main as cidgi_survey
from Democracy_Reconciliation import main as democracy_reconciliation

PAGES = {
    "Home": home,
    "CIDGI_survey": cidgi_survey,
    "Democracy_Reconciliation": democracy_reconciliation
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

if 'page' in st.experimental_get_query_params():
    selection = st.experimental_get_query_params()['page'][0]

page = PAGES.get(selection, home)
page()

# Set page configuration
st.set_page_config(layout='wide', page_title="Home Page")

# Sidebar with company logo and name
with st.sidebar:
    st.image("CPASI_logo.png", use_column_width=True)
    st.markdown("# Centre for policy Alternatives")
    st.markdown("[Visit CPA Website](https://www.cpalanka.org/)")

# Main section with dashboard buttons

st.markdown("""
    <h1 style="text-align:center; color:#800000; font-size:36px;">
    CPA Data Bank
    </h1>
        <hr style="width:70%; margin:auto; border:1px solid #c2d6d6;">
    <br>

    """, unsafe_allow_html=True)

# Add space between the title and the dashboard section
st.markdown("<br><br>", unsafe_allow_html=True)


st.markdown("### Confidence in Democratic Governance Index – Wave 06")

if st.button("Go to Dashboard - Confidence in Democratic Governance Index – Wave 06"):
    st.experimental_set_query_params(page="CIDGI_survey.py")
    st.experimental_rerun()

st.markdown("### Democracy & Reconciliation in Sri Lanka")
if st.button("Go to Dashboard - Democracy & Reconciliation in Sri Lanka"):
    st.experimental_set_query_params(page="Democracy_Reconciliation.py")
    st.experimental_rerun()
