
import streamlit as st

st.set_page_config(
    page_title="Applied AI & Data Strategy Portfolio",
    page_icon="📊",
    layout="wide"
)

# Page styling

# Page styling
st.markdown("""
<style>
    .stApp {
        background: #F4F7FB !important;
    }

    [data-testid="stAppViewContainer"] {
        background: #F4F7FB !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    [data-testid="stMain"] {
        color: #34445A !important;
    }

    h1, h2, h3 {
        color: #183153 !important;
    }

    p {
        color: #52647A;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero {
        background: #FFFFFF;
        padding: 42px;
        border-radius: 14px;
        border: 1px solid #DCE5EF;
        margin-bottom: 30px;
    }

    .hero h1 {
        color: #183153 !important;
        font-size: 38px;
    }

    .hero p {
        color: #52647A !important;
        font-size: 17px;
        line-height: 1.7;
    }

    .eyebrow, .status {
        color: #3976A8 !important;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .project-card {
        background: #FFFFFF;
        padding: 24px;
        border: 1px solid #DCE5EF;
        border-radius: 12px;
        min-height: 190px;
    }

    .project-card h3 {
        color: #183153 !important;
        font-size: 19px;
    }

    .project-card p {
        color: #596B80 !important;
        font-size: 14px;
        line-height: 1.6;
    }

    .about {
        background: #EAF1F8;
        padding: 25px;
        border-radius: 12px;
        color: #34445A;
        line-height: 1.8;
    }

    .footer {
        color: #718096;
        font-size: 13px;
        text-align: center;
        padding-top: 35px;
    }
</style>
""", unsafe_allow_html=True)

# Homepage introduction
st.markdown("""
<div class="hero">
    <div class="eyebrow">Applied AI | Data | Business Strategy</div>
    <h1>Turning data and AI into practical business insights</h1>
    <p>
        Welcome to my portfolio. Here I explore how data analytics,
        machine learning and applied AI can help address business
        challenges, identify opportunities and support better decisions.
    </p>
</div>
""", unsafe_allow_html=True)


# Portfolio focus
st.subheader("Areas of focus")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-card">
        <div class="status">Portfolio area</div>
        <h3>Data Analytics</h3>
        <p>
            Working with data, SQL and visualisation to identify
            patterns, understand performance and generate insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <div class="status">Portfolio area</div>
        <h3>Applied AI & Machine Learning</h3>
        <p>
            Exploring AI applications, predictive models and
            practical approaches to solving real-world problems.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="project-card">
        <div class="status">Portfolio area</div>
        <h3>AI & Business Strategy</h3>
        <p>
            Assessing business opportunities, implementation
            considerations and the value AI can create.
        </p>
    </div>
    """, unsafe_allow_html=True)


# Projects section
st.markdown("---")
st.header("Selected projects")

st.write(
    "Practical projects will be added here as they are developed. "
    "Each will include the problem, approach, tools, results and "
    "business implications."
)

p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class="project-card">
        <div class="status">In development</div>
        <h3>Business Data & Insights</h3>
        <p>
            An interactive analysis exploring business performance,
            data trends and decision-making using Python and SQL.
        </p>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="project-card">
        <div class="status">Planned</div>
        <h3>Applied AI Solution</h3>
        <p>
            A practical AI application demonstrating how intelligent
            tools can support research, analysis or business workflows.
        </p>
    </div>
    """, unsafe_allow_html=True)


# About section
st.markdown("---")
st.header("About this portfolio")

st.markdown("""
<div class="about">
    My background spans materials engineering, industrial problem-solving
    and business strategy. This portfolio brings these perspectives
    together through practical work in data analytics, machine learning
    and applied AI.

    <br><br>

    The focus is on demonstrating how technical methods can be applied
    to business and industrial challenges, with clear explanations of
    the approach, findings and limitations.
</div>
""", unsafe_allow_html=True)


# Footer
st.markdown("""
<div class="footer">
    Applied AI & Data Strategy Portfolio
</div>
""", unsafe_allow_html=True)
