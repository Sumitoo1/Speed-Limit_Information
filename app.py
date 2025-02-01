import streamlit as st
import datetime


# Function to add background image from URL
def set_background():
    bg_image_url = "https://www.shutterstock.com/image-vector/set-cartoon-paper-cut-weather-260nw-1705020187.jpg"

    st.markdown(f"""
    <style>
    .stApp {{
        background: url("{bg_image_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    .card {{
        border: 2px solid #444;
        border-radius: 12px;
        padding: 15px;
        margin: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.3);
        color: white;
        font-weight: bold;
        font-size: 16px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }}
    .title-text {{
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        color: white;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.9);
    }}
    </style>
    """, unsafe_allow_html=True)


# Function to calculate speed limit based on time of day
def calculate_speed_limit(time_of_day):
    if 6 <= time_of_day.hour < 9:
        return 60, 40, "The weather is foggy during this time, reducing visibility. Speed limits are lowered."
    elif 9 <= time_of_day.hour < 12:
        return 100, 80, "The weather is clear and ideal for traveling at standard speed limits."
    elif 12 <= time_of_day.hour < 15:
        return 80, 60, "Light rain reduces traction and visibility, so speed limits are slightly reduced."
    elif 15 <= time_of_day.hour < 19:
        return 60, 40, "Heavy rainfall makes roads slippery, requiring lower speed limits."
    else:
        return 100, 80, "The weather is clear and ideal for traveling at standard speed limits."


# Main application function
def main():
    set_background()

    st.markdown("<div class='title-text'>🚗💨 Dynamic Speed Limit System</div>", unsafe_allow_html=True)

    highways = [
        "Mumbai-Pune Expressway", "Yamuna Expressway", "Delhi-Meerut Expressway",
        "Eastern Peripheral Expressway", "Western Peripheral Expressway", "Ahmedabad-Vadodara Expressway",
        "Hyderabad Outer Ring Road", "Bangalore-Mysore Expressway", "Purvanchal Expressway",
        "Delhi-Mumbai Expressway", "Lucknow-Agra Expressway", "Chennai Peripheral Ring Road",
        "Dwarka Expressway", "Ganga Expressway", "Mumbai-Nagpur Expressway"
    ]
    selected_highway = st.selectbox("Select the Express Highway:", highways)

    time_labels = ["Morning (6 AM - 9 AM)", "Day (9 AM - 12 PM)", "Afternoon (12 PM - 3 PM)", "Evening (3 PM - 7 PM)",
                   "Night (7 PM Onwards)"]

    time_ranges = [(6, 9), (9, 12), (12, 15), (15, 19), (19, 24)]
    selected_time = st.selectbox("Select Travel Time:", time_labels)

    start_hour, end_hour = time_ranges[time_labels.index(selected_time)]

    # Restrict date selection from today up to December 31, 2025
    min_date = datetime.date.today()
    max_date = datetime.date(2025, 12, 31)

    selected_date = st.date_input("Select Travel Date:", min_date, min_date, max_date)

    selected_datetime = datetime.datetime.combine(selected_date, datetime.time(start_hour, 0))

    with st.expander("📌 Selected Details", expanded=True):
        st.markdown(f"<div class='card'>🏎️ <b>Highway:</b> {selected_highway}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'>⏳ <b>Selected Time:</b> {selected_time}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'>📅 <b>Selected Date:</b> {selected_date}</div>", unsafe_allow_html=True)

    if st.button("🚦 Check Speed Limit"):
        st.markdown(
            f"<div class='card'>🔍 Fetching speed limits for {selected_highway} on {selected_date} at {selected_time}...</div>",
            unsafe_allow_html=True)

        light_vehicle_limit, heavy_vehicle_limit, reason = calculate_speed_limit(selected_datetime)

        st.markdown(
            f"<div class='card'>🚗 <b>Suggested Speed Limit for Light Vehicles:</b> {light_vehicle_limit} km/h</div>",
            unsafe_allow_html=True)
        st.markdown(
            f"<div class='card'>🚛 <b>Suggested Speed Limit for Heavy Vehicles:</b> {heavy_vehicle_limit} km/h</div>",
            unsafe_allow_html=True)
        st.markdown(f"<div class='card'>ℹ️ <b>Reason:</b> {reason}</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
