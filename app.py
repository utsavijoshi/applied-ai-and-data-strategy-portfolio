
import streamlit as st

st.set_page_config(
    page_title="Applied AI & Data Strategy Portfolio",
    page_icon="📊",
    layout="wide"
)

# Page styling
st.markdown("""
<style>
    .stApp {
        background-color: #F7F9FC;
        color: #243247;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 {
        color: #183153;
    }

    .hero {
        background: #FFFFFF;
        padding: 42px;
        border-radius: 14px;
        border: 1px solid #E3EAF2;
        margin-bottom: 30px;
    }

    .eyebrow {
        color: #3976A8;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero h1 {
        font-size: 38px;
        line-height: 1.2;
        margin-bottom: 15px;
    }

    .hero p {
        color: #52647A;
        font-size: 17px;
        line-height: 1.7;
    }

    .project-card {
        background: #FFFFFF;
        padding: 24px;
        border: 1px solid #E3EAF2;
        border-radius: 12px;
        min-height: 190px;
    }

    .project-card h3 {
        font-size: 19px;
        margin-bottom: 12px;
    }

    .project-card p {
        color: #596B80;
        line-height: 1.6;
        font-size: 14px;
    }

    .status {
        color: #3976A8;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
    }

    .about {
        background: #EDF3F9;
        padding: 25px;
        border-radius: 12px;
        line-height: 1.7;
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
