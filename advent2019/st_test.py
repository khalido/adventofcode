import streamlit as st
import plotly.express as px


st.title("Plotly")
st.write("Gapminder animation")
gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90],
)
st.plotly_chart(fig)

st.markdown(
    """The problem with plotly is that it doesn't deal with with large data points, and it doesn't yet support cumalative graphs for drawing trendlines. 
    
    That said, it works for examples like the above, where the number of datapoints is small and each frame is independent of the ones before.
    """
)

st.subheader("Gif from Matplotlib")
st.image("test.gif")
