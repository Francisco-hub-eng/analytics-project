import streamlit as st
import pandas as pd
import logging
import nfl_data_py as nfl
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

st.header("SportsWorldCentral Data App")
st.subheader("Team Touchdown Totals")

try:

    flat_team_df_ordered = st.session_state['flat_team_df_ordered']

    unique_leagues = st.session_state['unique_leagues']
    selected_league = st.sidebar.selectbox('Pick league ID', unique_leagues)

    st.sidebar.divider()
    st.sidebar.subheader(":blue[Data sources]")
    st.sidebar.text("SportsWorldCentral")
    st.sidebar.text("NFLDataPy")

    flat_team_df_ordered['league_id'] = flat_team_df_ordered[
        'league_id'
    ].astype(str)
    flat_team_df_ordered = flat_team_df_ordered[
        flat_team_df_ordered['league_id'] == selected_league
    ]