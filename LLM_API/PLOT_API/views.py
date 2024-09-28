# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from django.conf import settings

# Initialize Langchain's LLM
llm = ChatGroq(
    temperature=2, 
    groq_api_key=settings.GROQ_API_KEY,  # Use the key stored in Django settings
    model_name="llama-3.1-70b-versatile"
)

# Define the API view with a decorator
@api_view(['POST'])
def generate_plot(request):
    try:
        # Get the choice (1: scrape headlines, 2: custom headlines)
        get_what_need = request.data.get('get_what_need')

        if get_what_need == 1:
            # Scrape headlines from the web
            url = "https://timesofindia.indiatimes.com/home/headlines"
            loader = WebBaseLoader(url)
            docs = loader.load()

            # Join all page content into a single string
            news_content = "\n".join([doc.page_content for doc in docs])

            # Create the prompt to extract headlines
            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED NEWS HEADLINES FROM WEBSITE:
                {NEWS}
                ### INSTRUCTION:
                SELECT top 3 politically unusual or surprising headlines any three but only three which is unique
                JUST only 3 HEADLINE  as three single line POINTS  
                not more than 10 words for each point (NO PREAMBLE)
                SELECT ONLY  HEADLINES NO ELABORATION NEEDED
                """
            )
            # Generate the headlines using the LLM
            chain_extract = prompt_extract | llm
            res = chain_extract.invoke(input={'NEWS': news_content})
            plot_source = res.content

        elif get_what_need == 2:
            # Get custom headlines from the user
            headline1 = request.data.get('headline_1', "")
            headline2 = request.data.get('headline_2', "")
            headline3 = request.data.get('headline_3', "")
            plot_source = f"{headline1}\n{headline2}\n{headline3}"
        
        else:
            return Response({"error": "Invalid option for 'get_what_need'"}, status=status.HTTP_400_BAD_REQUEST)

        # Now, generate a plot connecting the three points (headlines)
        prompt_extract_2 = PromptTemplate.from_template(
            """
            ### SCRAPED NEWS HEADLINES FROM WEBSITE:
            {points}
            ### INSTRUCTION:
            Create a simple plot which connects all 3 news like each one is interrelated to each other in an interesting way. 
            The plot should be like dark truth happening politically back of the head. Use all the points.
            Generate less than 50 words or tokens.
            GIVE ONLY SINGLE PLOT TO CONNECT ALL THREE POINTS (No PREAMBLE)
            """
        )
        # Generate the plot
        chain_extract_2 = prompt_extract_2 | llm
        plot = chain_extract_2.invoke(input={'points': plot_source})

        # Return the plot as the API response
        return Response({'plot': plot.content}, status=status.HTTP_200_OK)

    except Exception as e:
        # Catch and return any errors
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
