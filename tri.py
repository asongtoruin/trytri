import streamlit as st
from triangulizor import triangulize


@st.cache(show_spinner=False)
def process_image(image, size):
    print(f'Uncached, {size}')
    return triangulize(image, size)


st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Triangulizor')

st.markdown(
    '''
    This web app uses (a fork of) [@mccutchen](https://twitter.com/mccutchen)'s 
    [triangulizor](https://github.com/mccutchen/triangulizor) Python library to 
    convert an image to "triangular" pixels. I think they look pretty cool. 
    It might be a bit slow if your image files are particularly large 
    (e.g. taken on a phone camera), so be patient :turtle: :turtle: :turtle:

    Show [me](https://twitter.com/adam_rusz) what you're making!
    '''
)

uploaded_file = st.file_uploader(
    'Choose a image file', type=['png', 'jpg', 'jpeg', 'tiff']
)

if uploaded_file is not None:
    st.image(uploaded_file, caption='Original Image', use_column_width=True)

    size = st.slider('"Pixel" size', min_value=5, max_value=100, value=20, step=5)

    with st.spinner('Processing...'):
        st.image(
            process_image(uploaded_file, size), 
            caption=f'{size}px Triangles!', 
            use_column_width=True
        )
