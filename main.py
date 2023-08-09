import streamlit as st
import time
import random
from PIL import Image


def calculate_love_percentage(name1, name2):
    combined_names = (name1.lower() + name2.lower()).replace(" ", "")
    random.seed(combined_names)
    if combined_names == "dirgahalimsusilosarasputrimuizza":
        return 100
    return random.randrange(0, 100, 5)


def display_result(love_percentage, name1, name2):
    st.write("Calculation complete!")
    st.write(f"Love Uniqueness between {name1} and {name2}: {love_percentage}%")
    if love_percentage == 100:
        image_path = Image.open('images/perfect.png')
        st.image(image_path, width=120)
        st.write("You are a perfect match!")
    elif love_percentage > 80:
        st.write("Your love is one of a kind!")
    elif love_percentage > 50:
        st.write("There's definitely something unique here!")
    else:
        st.write("Your love might need some more uniqueness.")


def main():
    image_path = Image.open('images/logo.png')
    st.image(image_path, width=100)
    st.title("Love Calculator")
    st.write("Find out the uniqueness of your love!")

    name1 = st.text_input("Enter your name:")
    name2 = st.text_input("Enter your crush's name:")

    calculate_button = st.button("Calculate")

    if calculate_button:
        if name1 and name2:
            st.write("Calculating...")
            progress_bar = st.progress(0)

            for i in range(101):
                time.sleep(0.03)
                progress_bar.progress(i)

            love_percentage = calculate_love_percentage(name1, name2)
            love_percentage = min(love_percentage, 100)

            display_result(love_percentage, name1, name2)

            st.button("Calculate Again")
        else:
            st.warning("Please enter both names to calculate the love uniqueness.")

if __name__ == "__main__":
    main()
