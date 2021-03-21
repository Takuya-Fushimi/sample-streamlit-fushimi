import streamlit as st
import io
import requests
from PIL import Image
from PIL import ImageDraw
import pandas as pd
import numpy as np

st.title('My 1st app')

st.write('dataflame')
st.write(
    pd.DataFrame({
        '1st columns':[1,2,3,4],
        '2st columns':[10,20,30,40]
    })
)

"""
# my 1st app
## magic command
こんな感じ。
"""

if st.checkbox('Show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(50,3),
        columns = ['a','b','c']
    )
    st.line_chart(chart_df)


st.title('face ninchiki')

SUBSCRIPTION_KEY  = '11f8081d917d4dde93616db7343649fa'
assert SUBSCRIPTION_KEY

face_api_url = 'https://20210320fushimi.cognitiveservices.azure.com/face/v1.0/detect'

upload_file = st.file_uploader("Choose an image...", type= 'jpg')

if upload_file is not None:
    img = Image.open(upload_file)
    with io.BytesIO() as output:
        img.save(output, format= "JPEG")
        binary_img= output.getvalue()
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }
    params = {
        'returnFaceId' : 'true',
        'returnFaceAttributes': 'age,gender,smile,facialHair,headPose,glasses'
    }

    res = requests.post(face_api_url, params = params, headers= headers, data= binary_img)
    results = res.json()

    # result = results[0]
    for result in results:
        rect = result['faceRectangle']
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'],rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill= None, outline='green', width= 5)

    st.image(img, caption='Uploaded Image.')

