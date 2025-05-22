import streamlit as st
import swc_simple_client as swc
import pandas as pd
import logging

logger = logging.getLogger(__name__)

st.header("SportsWorldCentral Data App")
st.subheader("Team Rosters Page")

base_url = st.session_state['base_url']

try:
    team_api_response = swc.call_api_endpoint(base_url, swc.LIST_TEAMS_ENDPOINT)

    if team_api_response.status_code == 200:
        team_data = team_api_response.json()

        teams_df = pd.DataFrame.from_dict(team_data)

        unique_leagues = teams_df['league_id'].unique()
        unique_leagues = sorted(unique_leagues.astype(str))

        if 'unique_leagues' not in st.session_state:
            st.session_state['unique_leagues'] = unique_leagues