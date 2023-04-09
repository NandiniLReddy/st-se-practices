import streamlit as st
st.set_page_config(layout="wide", page_title="Blog Writing",
                   page_icon=":star:")

st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1653163061406-730a0df077eb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1296&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)


st.markdown("<h2 style='text-align: center; color: white;'>Software Engineering Practices for Machine learning implmentation</h2>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: left; color: white;'>Introduction</h2>",
            unsafe_allow_html=True)


container_style = """
    border: 2px solid #f2f2f2;
    border-radius: 10px;
    padding: 20px;
"""

with st.container():
    st.markdown("""<div style='{}; text-align: justify'>Why is machine learning the most popular trending topic in the IT industry? because it is flexible and simple to use and work with. Machine learning is the process of teaching a model to predict or carry out tasks that might be helpful and simplify human work. Although while machine learning is simpler to work with and experiment with, there are several challenges involved in integrating it into a particular system. This complicates the system's ability to integrate machine learning because the machine must be rigorously iterated and fed a lot of data. But it's not completely impossible to lessen these difficulties.
            This article offers insights into how machine learning is viewed at one of the largest IT firms, Microsoft, and what difficulties they are running into when incorporating it into their various products. To work on this, a team at Microsoft conducted interviews and information gathering to learn how machine learning should be applied, what conventional methods they have been using, and what can be done to reduce the difficulties that arise when applying machine learning.
            Since these topics are so diametrically opposed, we need to work specifically with both systems to create a superior system that uses both.
            The entire system will be difficult to operate and produce a better result if one of them fails. Making each technology complement and cooperate with one another is therefore crucial.
            To get better results, machine learning-centric systems need a lot of modeling and remodeling. Like this, additional information is needed to predict any kind of output.
            However, modeling and rebuilding software embedding is quite complex and needs a lot of engineering mechanisms. Similarly, if there is more data, the system becomes more complex in both directions. The system gets even more difficult to integrate machine learning into if there are numerous components and modules that do so. Every model has a distinct flow, and for machine learning the flow needs to be repetitive for better accuracy</div>""".format(container_style), unsafe_allow_html=True)


st.markdown("<h2 style='text-align: left; color: white;'>Challenges</h2>",
            unsafe_allow_html=True)

st.write(""" 
<div style='text-align: justify;'>
Some of the main challenges that can be intrigued while implementing machine learning are data management, model selection, feature engineering, model training, model evaluation, and deployment and monitoring.
The goal is to help organizations build high-quality, reliable, and scalable ML systems by applying effective software engineering practices and leveraging the expertise of data scientists, software engineers, and domain experts; and Solve the best software engineering principles approach to overcome all these challenges while designing a system.</div>
 """, unsafe_allow_html=True)

# mystyle = '''
#     <style>
#         p {
#             text-align: justify;
#             height:250px;

#         }
#         .stMarkdown {
#             margin-top: 0px !important;
#         }
#     </style>
#     '''
# st.markdown(mystyle, unsafe_allow_html=True)


st.write("## what can be done??")


# Generate six equal columns, split into two rows of three
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)


# Place the information in each column
with c1:

    st.markdown("<div style='height: 260px;border: 1px solid grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Version management: Just like with any other area of software development, version management is essential to ML projects. Version control is used to track changes, encourage collaboration, and promote reproducibility for both data and code. This ensures that the results achieved from a given model can be traced back to the code and data used to train it."
                "</div>", unsafe_allow_html=True)

with c2:
    st.markdown(" <div style='height: 260px; border: 1px solid grey; font-family: Arial;'>"
                "Continuous Integration and Delivery: The testing, deployment, and monitoring of ML systems can be automated with the aid of continuous integration and delivery processes. This minimizes the possibility of introducing errors or bugs by ensuring that code updates are constantly merged and tested. By automating the process of distributing new models or upgrading current ones, automated deployment also aids in ensuring quality and dependability."
                "</div>", unsafe_allow_html=True)

with c3:
    st.markdown(" <div style= 'height:260px; border: 1px solid  grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Automated Testing and Monitoring: ML development must include automated testing and monitoring. Automated testing guarantees that models are operating as planned and aids in the early detection of problems during the development process. On the other hand, monitoring raises the flag for problems that call for human intervention and assists in identifying data drift and model deterioration. These methods enable businesses to maintain the accuracy and dependability of their models even as the underlying data changes over time."
                "</div>", unsafe_allow_html=True)

with c4:
    st.markdown(" <div style= 'height: 260px; border: 1px solid grey; font-family: Arial;'>"
                "Agile Development Methodologies: Agile development approaches encourage cooperation and iterative development, making them ideal for ML development. Additionally, they provide rapid prototyping and experimentation, enabling businesses to test and improve their ideas quickly. This procedure can ensure that models are accurate and pertinent to the current business problem while also cutting down on the time and expense associated with ML development."
                "</div>", unsafe_allow_html=True)

with c5:
    st.markdown(" <div style= 'height: 260px; border: 1px solid grey; font-family: Arial; background-color: #f2f2f2; color:black;'>"
                "Collaboration: For ML models to be accurate, pertinent, and scalable, collaboration between data scientists, software developers, and domain specialists is essential. Organizations may make sure that their models are well-designed, efficient, and able to manage complex business problems by bringing together people with various skill sets and perspectives. Additionally, collaboration fosters cross-functional learning and knowledge exchange, which supports the development of an innovative and continuous improvement culture."
                "</div>", unsafe_allow_html=True)

with c6:
    st.markdown("<div style= 'height: 260px; border: 1px solid grey; font-family: Arial;'>"
                "Training and Development: Building ML skills and capabilities inside firms requires spending on training and development. This makes it possible for organizations to fully utilize ML technology and for teams to have the knowledge and resources they need to handle ML initiatives. Organizations can create a long-lasting competitive edge by investing in training and development, which enables them to stay ahead of the curve in a continuously evolving business environment."
                "</div>", unsafe_allow_html=True)


# st.markdown(
#     "<h2>Some other solutions with respect to the model building and data</h2>", unsafe_allow_html=True)

# c7, c8 = st.columns(2)
# c9, c10 = st.columns(2)
# c11, c12 = st.columns(2)
# c13, c14 = st.columns(2)


# with c7:
#     st.info(""" Data Management: Any ML project's success depends on effective data management. This covers operations like data transformation, feature selection, and data cleaning. The authors advise storing datasets in a form that allows for easy access and sharing among team members, as well as using version control for dataset storage. """, height=None)
# with c8:
#     st.info(""" Model Development: An organized workflow and a clear methodology should be used when constructing ML models. The authors advise taking an iterative approach, adding testing and validation into the development process, and establishing regular feedback loops. They also advise choosing the top-performing models using a model selection approach. """)
# with c9:
#     st.info("""" Infrastructure: It's important that the infrastructure used to create and implement ML systems be dependable, scalable, and secure. The authors advocate employing cloud-based infrastructure while considering factors like data security and privacy as well as scalability and performance. """)
# with c10:
#     st.info(""" Deployment: The deployment of ML models should be scalable, dependable, and take into account concerns like model upgrades and version control. The authors advise deploying models on a cloud-based platform and leveraging approaches like containerization. """)
# with c11:
#     st.info(""" Monitoring: To make sure that ML models are functioning as planned and to identify any problems or anomalies, it is crucial to monitor them in production. The authors advise employing methods like logging and visualization to keep an eye on the behaviour and performance of models. """)
# with c12:
#     st.info(""" Bias and Fairness:  The model shouldn't be biased toward the data it was trained on while making predictions. Even if the dataset is smaller, it should still perform well. can accurately foretell eventualities in the real world. """)
# with c13:
#     st.info(""" Security: Any software system, including machine learning systems, should take security seriously. The authors advise employing strategies like access restriction, secure communication, and encryption to guard against illegal access to data and models.  """)
# with c14:
#     st.info(""" Scalability: Scalable infrastructure is needed because machine learning systems frequently deal with enormous volumes of data and models. To manage massive volumes of data and models, the authors advise employing strategies like distributed computing, parallel processing, and cloud-based infrastructure.  """)

st.markdown("<h2>Some other solutions with respect to the model building and data:</h2>",
            unsafe_allow_html=True)

c7, c8 = st.columns(2)
c9, c10 = st.columns(2)
c11, c12 = st.columns(2)
c13, c14 = st.columns(2)

with c7:
    st.markdown("<div style='height: 120px; border: 1px solid grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Data Management: Any ML project's success depends on effective data management. This covers operations like data transformation, feature selection, and data cleaning. The authors advise storing datasets in a form that allows for easy access and sharing among team members, as well as using version control for dataset storage."
                "</div>", unsafe_allow_html=True)

with c8:
    st.markdown("<div style='height: 120px;  border: 1px solid grey;'>"
                "Model Development: An organized workflow and a clear methodology should be used when constructing ML models. The authors advise taking an iterative approach, adding testing and validation into the development process, and establishing regular feedback loops. They also advise choosing the top-performing models using a model selection approach."
                "</div>", unsafe_allow_html=True)

with c9:
    st.markdown("<div style='height: 120px;  border: 1px solid grey;'>"
                "Infrastructure: It's important that the infrastructure used to create and implement ML systems be dependable, scalable, and secure. The authors advocate employing cloud-based infrastructure while considering factors like data security and privacy as well as scalability and performance."
                "</div>", unsafe_allow_html=True)

with c10:
    st.markdown("<div style='height: 120px;  border: 1px solid grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Deployment: The deployment of ML models should be scalable, dependable, and take into account concerns like model upgrades and version control. The authors advise deploying models on a cloud-based platform and leveraging approaches like containerization."
                "</div>", unsafe_allow_html=True)

with c11:
    st.markdown("<div style='height: 120px; border: 1px solid grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Monitoring: To make sure that ML models are functioning as planned and to identify any problems or anomalies, it is crucial to monitor them in production. The authors advise employing methods like logging and visualization to keep an eye on the behaviour and performance of models."
                "</div>", unsafe_allow_html=True)

with c12:
    st.markdown("<div style='height: 120px; border: 1px solid grey;'>"
                "Bias and Fairness:  The model shouldn't be biased toward the data it was trained on while making predictions. Even if the dataset is smaller, it should still perform well. can accurately foretell eventualities in the real world."
                "</div>", unsafe_allow_html=True)

with c13:
    st.markdown("<div style='height: 120px; border: 1px solid grey;'>"
                "Security: Any software system, including machine learning systems, should take security seriously. The authors advise employing strategies like access restriction, secure communication, and encryption to guard against illegal access to data and models."
                "</div>", unsafe_allow_html=True)

with c14:
    st.markdown("<div style='height: 120px; border: 1px solid grey; background-color: #f2f2f2; font-family: Arial; color:black;'>"
                "Scalability: Scalable infrastructure is needed because machine learning systems frequently deal with enormous volumes of data and models. To manage massive volumes of data and models, the authors advise employing strategies like distributed computing, parallel processing, and cloud-based infrastructure."
                "</div>", unsafe_allow_html=True)


st.write("<h2>Conclusion</h2>", unsafe_allow_html=True)
st.write("<div style=' text-align: justify;'>"
         "Overall, these additional approaches might improve the performance and dependability of ML systems more, but they might also increase complexity and cost more to execute. As a result, it's crucial to carefully weigh the trade-offs and select the options that best suit the requirements of the particular ML project and company."
         "</div>", unsafe_allow_html=True)


# row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
#     (.001, 1.8, .1, 1.3, .1))

# with row0_1:
#     st.info("conclusion")

# with row0_2:
#     st.info("Overall, these additional approaches might improve the performance and dependability of ML systems more, but they might also increase complexity and cost more to execute. As a result, it's crucial to carefully weigh the trade-offs and select the options that best suit the requirements of the particular ML project and company.")

st.write("<div style= 'text-align: center; color:red;'>"
         "<h1>Thank You!!! </h1>"
         "</div>", unsafe_allow_html=True)


st.write("<div style= 'text-align: right; color:red;'>"
         "<h1>By- Nandini Lokesh Reddy </h1>"
         "</div>", unsafe_allow_html=True)
