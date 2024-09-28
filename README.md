## News-Based Headline Plot Generator with LangChain & Groq LLM (Powered by Llama 3)

This project showcases an innovative tool designed to analyze and visualize news headlines using advanced artificial intelligence technologies. By leveraging the Llama 3.1 70B Versatile model, this tool offers a unique way to process news headlines and generate insightful plots that connect various headlines in a meaningful way.

### Overview
The primary goal of this project is to provide a way to automatically extract, analyze, and visualize news headlines. It uses a combination of LangChain and Groq AI's Llama 3.1 70B Versatile model to perform this task. The tool can scrape news headlines from a designated webpage or accept user-provided custom headlines. Depending on the mode selected by the user, it either extracts the most unusual or politically significant headlines from a news source or generates a plot based on custom input.

### Features
- **Automated News Extraction**: In the default mode, the tool is designed to scrape headlines from a specified news website, such as the Times of India. By utilizing LangChain's WebBaseLoader, the tool fetches the latest headlines from the web. Once the headlines are loaded, the Llama 3.1 70B Versatile model is employed to sift through the headlines and identify three that are particularly politically unusual or surprising. This selection process is guided by a well-defined prompt template that instructs the model to focus on uniqueness and relevance without providing elaboration.
  
- **Custom Headline Input**: For users who prefer to input their own headlines, the tool allows manual entry of three custom headlines. These user-provided headlines are then processed by the Llama 3.1 model to generate a cohesive plot. The plot aims to connect the headlines in a way that reveals intriguing interrelations and potential political implications. The model's ability to understand and integrate diverse headlines into a unified narrative demonstrates its sophisticated capabilities.

### Django REST API Integration
This project includes a Django REST API that allows users to interact with the headline plot generator. Users can submit requests to either scrape headlines from a news website or provide their own custom headlines. The API processes these inputs and generates a plot connecting the headlines, utilizing the same Llama 3.1 70B Versatile model. The API is structured to handle both modes efficiently, providing clear responses with the generated plots. 

### Sample API Requests
- For scraping headlines from the web, users can send a request with the following payload:
  ```json
  {
      "get_what_need": 1
  }
  ```

- For custom headline inputs, the request payload should look like this:
  ```json
  {
      "get_what_need": 2,
      "headline_1": "Custom headline 1",
      "headline_2": "Custom headline 2",
      "headline_3": "Custom headline 3"
  }
  ```

This integration of Django REST API enhances the tool's usability, allowing for seamless interaction with the headline generation process, whether through automated scraping or user-defined input.
