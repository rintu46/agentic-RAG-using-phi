# Recipe Recommendation System

## Overview

This application is a Recipe Recommendation System that utilizes a Retrieval-Augmented Generation (RAG) approach. It leverages OpenAI's models to recommend recipes based on user input. The system can suggest a three-course meal, including a starter, main course, and dessert.

## Features

- **Traditional RAG**: Provides recipe recommendations based on a knowledge base of PDF documents.
- **Agentic RAG**: Enhances the recommendation process by allowing the agent to search knowledge and show tool calls.
- **User Interface**: (Commented out) A UI component that allows interaction with the agent.

## Dependencies

This application requires the following Python packages:

- `phi`: A library for building AI agents.
- `dotenv`: For loading environment variables from a `.env` file.
- `psycopg`: PostgreSQL adapter for Python.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   gpt=your_openai_api_key
   ```

4. **Database Setup**:
   Ensure you have a PostgreSQL database running and update the `db_url` in `app.py` with your database credentials.

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

## Usage

Once the application is running, you can interact with the agent by providing a request for recipe recommendations. The agent will respond with suggestions based on the input provided.

 



 ## Source

 Please visit this site - 
```
 https://www.youtube.com/watch?v=kkF9gsBF7gg&ab_channel=MervinPraison

```