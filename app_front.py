import streamlit as st
import requests
import plotly.graph_objects as go
from graphviz import Digraph
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io
import graphviz
from graphviz import dot


def main():



    st.title("Опрос ML системы")
    query_params = st.query_params
    # st.write("Query params:", query_params)
    #st.write("Query params2:",query_params.get('page'))
    #st.write("True or not:",query_params.get('page') == ['ml_system'])
    if query_params.get('page') == "ml_system":

        st.write("Вы на странице ML системы.")
        st.image("schema.png", width=800, caption="Diagram", use_column_width=False)
        st.write("Графики и другая информация:")
        st.line_chart([1, 2, 3, 4, 5])


        fig = go.Figure()


        fig.add_trace(go.Scatter(
            x=[1, 3, 5],
            y=[5, 5, 5],
            mode='markers+text',
            text=["Box A", "Box B", "Box C"],
            textposition="top center",
            marker=dict(size=15, color='LightSkyBlue'),
            hoverinfo='text'
        ))


        fig.add_trace(go.Scatter(
            x=[1, 3],
            y=[5, 5],
            mode='lines+text',
            line=dict(width=2, color='black'),
            textposition="middle right",
            hoverinfo='none'
        ))


        fig.update_layout(
            title="Interactive Diagram with Plotly",
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            showlegend=False
        )

        
        st.plotly_chart(fig)





    else:

        with st.form(key='polling_form'):
            question1 = st.text_input(label='Какие инструменты и платформы вы используете для хранения данных, их обработки и тренировки моделей? Существует ли проблема с разграничением доступа?')
            question2 = st.text_input(label='Есть ли у вас сейчас какие-либо решения для автоматизации CI/CD процессов? Если да, то какие?')
            question3 = st.text_input(label='Используете ли вы контейнеризацию и оркестрацию контейнеров в ваших текущих процессах?')
            question4 = st.text_input(label='Есть ли у вас предпочтения по используемым технологиям и инструментам для MLOps?')
            question5 = st.text_input(label='Есть ли специфические требования к безопасности данных и моделей?')
            question6 = st.text_input(label='Насколько критична для вас интеграция с существующими системами и инструментами?')
            question7 = st.text_input(label='Какие метрики вы используете для измерения эффективности процессов разработки и деплоя моделей? Устраивают ли вас результаты?')
            question8 = st.text_input(label='Есть ли у вас специфические кейсы или примеры, где вы сталкиваетесь с трудностями и хотели бы улучшить процессы?')
            submit_button = st.form_submit_button(label='Отправить')

        if submit_button:
            data = {
                'question1': question1,
                'question2': question2,
                'question3': question3,
                'question4': question4,
                'question5': question5,
                'question6': question6,
                'question7': question7,
                'question8': question8
            }
            try:
                response = requests.post('http://localhost:8000/submit_data_polling', data=data, allow_redirects=False)
                if response.status_code == 303:
                    st.success("Data submitted successfully! Redirecting...")
                    st.markdown('<meta http-equiv="refresh" content="0; url=http://localhost:8501/?page=ml_system" />',
                                unsafe_allow_html=True)
                    st.markdown("""
                                           <script>
                                               window.location.href = "http://localhost:8501/?page=ml_system";
                                           </script>
                                       """, unsafe_allow_html=True)
                else:
                    try:
                        error_message = response.json().get('error', 'Unknown error')
                        st.error(f"Failed to submit survey. Error: {error_message}")
                    except requests.exceptions.JSONDecodeError:
                        st.error("Failed to submit survey. Received an unexpected response.")
            except Exception as e:
                st.error(f"An error occurred: {e}")




if __name__ == '__main__':
    main()

