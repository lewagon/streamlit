
import streamlit as st


def title():
    return 'Local images'


def run():

    st.write('## Using local images for links or background')

    with st.echo():

        import base64

        @st.cache
        def load_image(path):
            with open(path, 'rb') as f:
                data = f.read()
            encoded = base64.b64encode(data).decode()
            return encoded

        def image_tag(path):
            encoded = load_image(path)
            tag = f'<img src="data:image/png;base64,{encoded}">'
            return tag

        def background_image_style(path):
            encoded = load_image(path)
            style = f'''
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
            }}
            </style>
            '''
            return style

        image_path = 'images/python.png'
        image_link = 'https://docs.python.org/3/'

        st.write('*Hey*, click me I\'m a button!')

        st.write(f'<a href="{image_link}">{image_tag(image_path)}</a>', unsafe_allow_html=True)

        if st.checkbox('Show background image', False):
            st.write(background_image_style(image_path), unsafe_allow_html=True)
