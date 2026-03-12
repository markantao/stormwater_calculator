import streamlit as st
import plotly.graph_objects as go
import time

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

h1 {
    font-weight: 600;
}

.block-container {
    padding-top: 2rem;
}

/* slider hover animation */
div[data-baseweb="slider"]{
    transition: transform 0.2s ease;
}

div[data-baseweb="slider"]:hover{
    transform: scale(1.05);
}

/* premium card effect */
.metric-card {
    padding: 30px;
    border-radius: 12px;
    background-color: #f7f7f7;
    text-align:center;
    font-size:40px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

st.title("Stormwater Runoff Calculator")

with st.expander("Why Stormwater Calculations Matter"):

    st.write("""
Stormwater runoff calculations help engineers design drainage systems that prevent flooding,
erosion, and infrastructure damage during rainfall events.

By estimating runoff flow rates using the Rational Method (Q = C × I × A), engineers can size
storm sewers, culverts, and retention systems to safely carry water away from developed areas.

These calculations are essential for:

• Preventing urban flooding  
• Protecting roads, buildings, and utilities  
• Designing sustainable stormwater management systems  
• Meeting municipal engineering standards
""")

st.write("Rational Method: Q = C × I × A")

surface = st.selectbox(
    "Surface Type",
    ["Asphalt", "Roof", "Grass", "Gravel"]
)

# Runoff coefficients
coefficients = {
    "Asphalt": 0.9,
    "Roof": 0.95,
    "Grass": 0.3,
    "Gravel": 0.6
}

C = coefficients[surface]

# User inputs
rainfall = st.slider("Rainfall Intensity (mm/hr)", 10, 100, 50)
area = st.slider("Drainage Area (hectares)", 0.1, 5.0, 1.0)

# Runoff calculation
Q = C * rainfall * area

st.divider()

# Runoff Result
st.markdown(
    f"<h1 style='text-align:center;'>Runoff Q = {round(Q,2)}</h1>",
    unsafe_allow_html=True
)

st.write("### Runoff Behavior vs Rainfall Intensity")

# Rainfall Range Visualization
rainfall_values = list(range(10, rainfall + 1))

runoff_values = [C * r * area for r in rainfall_values]

# Create plot
chart_placeholder = st.empty()

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=rainfall_values,
        y=runoff_values,
        mode="lines+markers",
        name="Runoff",
        hovertemplate=
        "Rainfall: %{x} mm/hr<br>" +
        "Runoff: %{y}<extra></extra>"
    )
)

fig.update_layout(
    title="Stormwater Runoff vs Rainfall",
    xaxis_title="Rainfall Intensity (mm/hr)",
    yaxis_title="Runoff (Q)",
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
    hovermode="x unified",
    template="plotly_white"
    
)

for i in range(len(rainfall_values)):
    fig.data[0].x = rainfall_values[:i+1]
    fig.data[0].y = runoff_values[:i+1]
    chart_placeholder.plotly_chart(fig, use_container_width = True)

