# ==========================================================
# AI Resume Screening System
# Streamlit UI Styling
# Clear Purple Professional Theme
# ==========================================================


def apply_styles():

    return """

    <style>


    /* Main App Background */

    .stApp {

        background:

        linear-gradient(
            135deg,
            #f3e8ff,
            #ede9fe,
            #ddd6fe
        );

        color:#1f1f1f;

    }



    /* Main Title */

    h1 {

        color:#4c1d95 !important;

        text-align:center;

        font-size:45px;

        font-weight:800;

    }



    h2,h3 {

        color:#5b21b6 !important;

    }



    /* Custom Cards */

    .card {


        background:white;


        padding:25px;


        border-radius:20px;


        box-shadow:

        0px 5px 20px

        rgba(
            0,
            0,
            0,
            0.15
        );


        margin:15px;


    }



    /* Sidebar */

    section[data-testid="stSidebar"] {


        background:

        linear-gradient(

            180deg,

            #4c1d95,

            #7e22ce

        );


    }



    section[data-testid="stSidebar"] * {


        color:white !important;


        font-size:17px;


    }



    /* Sidebar Heading */

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {


        color:white !important;

    }



    /* Metrics */

    div[data-testid="metric-container"] {


        background:white;


        padding:20px;


        border-radius:15px;


        box-shadow:

        0px 4px 15px

        rgba(
            0,
            0,
            0,
            0.15
        );


    }



    div[data-testid="metric-container"] label {


        color:#6b21a8 !important;

        font-weight:bold;


    }



    div[data-testid="metric-container"] div {


        color:#111827 !important;


        font-size:28px;


        font-weight:bold;


    }




    /* Upload Box */


    section[data-testid="stFileUploader"] {


        background:white;


        padding:20px;


        border-radius:20px;


        box-shadow:

        0px 4px 15px

        rgba(
            0,
            0,
            0,
            0.15
        );


    }





    /* Buttons */


    .stButton button {


        background:

        linear-gradient(

            90deg,

            #7e22ce,

            #4c1d95

        );


        color:white;


        border:none;


        border-radius:30px;


        padding:

        12px 30px;


        font-weight:bold;


    }



    .stButton button:hover {


        background:#9333ea;


        color:white;


    }




    /* Text Visibility */

    p,li {


        color:#111827 !important;


        font-size:16px;


    }




    /* Success */

    .stSuccess {


        background:#dcfce7;


        color:#166534;


        border-radius:15px;


    }



    /* Warning */

    .stWarning {


        background:#fef3c7;


        color:#92400e;


        border-radius:15px;


    }




    /* Info */


    .stInfo {


        background:#ede9fe;


        color:#4c1d95;


        border-radius:15px;


    }
    [data-testid="stFileUploaderDropzone"] span {
    
        color:#6b7280 !important;
    
    }
    
    
    [data-testid="stFileUploaderDropzone"] svg {
    
        color:#6b7280 !important;
    
        fill:#6b7280 !important;
    
    }



    </style>

    """
