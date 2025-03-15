import streamlit as st

st.title("🌍 Unit Converter 🔄")

st.write("### 🎉 Welcome to the Unit Converter App!") 
st.markdown("🛠️ This app converts units of **Length**, **Weight**, and **Time**. Please select the type of conversion from the dropdown below.👇")

# User selects a category
category = st.selectbox("📌 Select Category", ["📏 Length", "⚖️ Weight", "⏳ Time"])

# Define unit conversion options based on the selected category
if category == "📏 Length":
    unit = st.selectbox("🔁 Select Conversion", ["📐 Kilometers to Miles", "📏 Miles to Kilometers"])
elif category == "⚖️ Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["🏋️ Kilograms to Pounds", "💪 Pounds to Kilograms"])
elif category == "⏳ Time":
    unit = st.selectbox("⏳ Select Conversion", ["⏱️ Seconds to Minutes", "⏲️ Minutes to Seconds", "🕰️ Minutes to Hours", 
                                              "⏳ Hours to Minutes", "📅 Hours to Days", "🌞 Days to Hours"])
else:
    unit = None

# Input field for the value to be converted
value = st.number_input("🔢 Enter the value to convert", min_value=0.0)

# Conversion function
def convert_units(category, value, unit): 
    if category == "📏 Length":
        if unit == "📐 Kilometers to Miles":
            return value * 0.621371
        elif unit == "📏 Miles to Kilometers":
            return value / 0.621371
    elif category == "⚖️ Weight":
        if unit == "🏋️ Kilograms to Pounds":
            return value * 2.20462
        elif unit == "💪 Pounds to Kilograms":
            return value / 2.20462
    elif category == "⏳ Time":
        if unit == "⏱️ Seconds to Minutes":
            return value / 60
        elif unit == "⏲️ Minutes to Seconds": 
            return value * 60
        elif unit == "🕰️ Minutes to Hours":
            return value / 60
        elif unit == "⏳ Hours to Minutes":
            return value * 60
        elif unit == "📅 Hours to Days":
            return value / 24
        elif unit == "🌞 Days to Hours":
            return value * 24
    return None

# Perform conversion when button is clicked
if st.button("🔄 Convert Now"):
    if unit and value >= 0:
        result = convert_units(category, value, unit)
        if result is not None:
            st.success(f"✅ The result is **{result:.2f}**")
        else:
            st.error("❌ Invalid conversion selected.")
    else:
        st.error("⚠️ Please select a valid category and enter a value.")
