from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.document_loaders import WebBaseLoader
from API_KEY import API
llm = ChatGroq(
    temperature=2, 
    groq_api_key=API, # use yours if needed
    model_name="llama-3.1-70b-versatile"
)
get_what_need=int(input('enter 1 if plot based on today news,enter 2 if custom headlines needed to be inserted '))
if get_what_need== 1:


        # Example URL
        url = "https://timesofindia.indiatimes.com/home/headlines"
        # Use WebBaseLoader to load the webpage
        loader = WebBaseLoader(url)

        # Load the webpage's content as a list of documents
        docs = loader.load()

        # Extract text from the documents and print it
        #for doc in docs:

            #print(doc.page_content)
        prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED NEWS HEADLINES FROM WEBSITE:
                {NEWS}
                ### INSTRUCTION:
                SELECT top 3 politically unusual or surprising headlines any three but only three which is unique

            JUST only 3 HEADLINE  as three  single line POINTS  
                
            not more than 10 words for  each point(NO PREAMBLE)
            SELECT ONLY  HEADLINES NO ELABORATION NEEDED

                """
        )

        chain_extract = prompt_extract | llm 
        res = chain_extract.invoke(input={'NEWS':docs})    
        #print(res.content)
        plot_source=res.content
elif get_what_need==2:
        a= input('enter headline 1')
        b= input('enter headline 2')
        c= input('enter headline 3')
        plot_source= a+ ''+b+''+ c
prompt_extract_2 = PromptTemplate.from_template(
        """
        ### SCRAPED NEWS HEADLINES FROM WEBSITE:
        {points}
        ### INSTRUCTION:
        Create a simple plot which connects all 3 news like each one is interrelated to each other in an interestwing way. each point is relevant , which means there is correlation and causation among the given points
         the plot should be like dark truth happening politically back of the head. use all the points
         Generate less than 50 words or tokens
         GIVE ONLY SINGLE PLOT TO CONNECT ALL THREE POINTS  (No PREAMBLE)
        """
)

chain_extract_2 = prompt_extract_2 | llm 
plot = chain_extract_2.invoke(input={'points':plot_source})    
if get_what_need==1:
        print(res.content)
print(plot.content)
