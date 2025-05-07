import gradio as gr
from summarizer.summarize import generate_summary

iface = gr.Interface(
    fn=generate_summary,
    inputs=[
        gr.Textbox(label="Enter text manually", lines=8, placeholder="Write or paste text here..."),
        gr.File(label="Or upload a .txt or .pdf file", file_types=[".txt", ".pdf"]),
        gr.Slider(10, 200, value=30, step=10, label="Min Summary Length"),
        gr.Slider(30, 300, value=100, step=10, label="Max Summary Length"),
        gr.Checkbox(label="Use sampling (do_sample)", value=False),
    ],
    outputs=gr.Textbox(label="Generated Summary", elem_id="output-summary"),
    title="📝 Multilingual Text Summarizer with LLMs",
    description="Summarize English or French text using transformers. Supports text, PDF and TXT.",
    theme=gr.themes.Monochrome(), 
        # gr.themes.Default()   
        # gr.themes.Base()
        # gr.themes.Soft()
        # gr.themes.Monochrome()
        # gr.themes.Glass()
    live=True,  # Allow real-time interaction with the summarizer
    examples=[
        [
            """Bonjour, ceci est un exemple d'email professionnel très long. Nous avons plusieurs documents importants à examiner. Le premier document concerne la gestion des ressources humaines, et le second porte sur l'optimisation des processus logistiques pour améliorer l'efficacité des opérations de transport. Les deux documents contiennent des informations clés sur les changements organisationnels que nous avons mis en place récemment. La réunion d'aujourd'hui permettra de discuter de ces points et de prendre des décisions éclairées sur la direction future de notre entreprise. Nous avons besoin d'un résumé clair et précis des principaux changements et recommandations. Merci de prêter attention aux détails les plus importants.""",
        ],
        [
            """This is a long English article that explains how machine learning models are trained using large datasets. Machine learning involves the development of algorithms that can process and analyze data to make predictions or decisions without being explicitly programmed. In this article, we will explore the different stages involved in training a machine learning model, starting with data collection, followed by data preprocessing, feature engineering, model selection, and finally, model training and evaluation. Each of these steps is crucial for building a high-performance machine learning model. We will also discuss some of the challenges faced during the training process, such as overfitting and underfitting, and how to mitigate them using techniques like cross-validation, hyperparameter tuning, and regularization. The goal is to help readers understand the entire process of model training and to provide insights into the best practices used in the industry.""",
        ]
    ],
    css="""
        #text-input, #file-input {
            font-size: 16px;
            border-radius: 8px;
        }
        #min-length-slider, #max-length-slider {
            background-color: #e0e0e0;
        }
        #output-summary {
            font-size: 14px;
            font-family: Arial, sans-serif;
            color: #333;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 12px;
        }
        .footer { 
            display: none;  /* Remove footer */
        }
    """
)


iface.launch()
