# Insurance Voice Agents

A multimodal voice assistant designed for **Insurance Services**. This application leverages **Google's Agent Development Kit (ADK)** and the **Gemini 2.5 Flash Native Audio** model to provide real-time, bidirectional voice interactions for insurance customers.

![bidi-demo-screen](assets/bidi-demo-screen.png)

## Capabilities & Domain Delivery

### Domain: Indian Banking & Credit Cards
This agent serves as a customer support representative for Cymbal Bank, specializing in the Indian market. It is capable of:
-   **Multilingual Support**: Seamlessly switches between Hindi and English based on user preference.
-   **General Banking**: Answering queries about account balances and transactions.
-   **Credit Card Expertise**: Providing detailed information about Cymbal Bank's credit card offerings (modeled after Federal Bank products like Visa Celesta, Imperio, Signet).
-   **Application Processing**: Collecting user details to process credit card applications.

### Key Use Cases
1.  **Product Discovery**: "Tell me about the benefits of the Visa Celesta card."
2.  **Eligibility Checks**: "Am I eligible for a credit card with a salary of 5 Lakhs?"
3.  **Fee Inquiries**: "What is the annual fee for the Imperio card?"
4.  **Application**: "I want to apply for this card." (Triggers the specialized application sub-agent).

## Agents Hierarchy

The system uses a hierarchical agent structure to manage conversation flow and expertise.

### 1. Main Agent: `mainbankingdesk`
-   **Role**: Primary customer entry point.
-   **Persona**: Female customer support assistant for Cymbal Bank.
-   **Responsibilities**:
    -   Greeting customers.
    -   Handling general banking queries (balance, transactions).
    -   Routing specific credit card queries to the expert sub-agent.
-   **Tools**: Google Search.

### 2. Sub-Agent: `creditcard_expert`
-   **Role**: Domain specialist for credit cards.
-   **Responsibilities**:
    -   Answering detailed questions about credit card features, rewards, and fees.
    -    explaining eligibility criteria based on Indian banking standards.
    -   Handing off application intents to `card_application`.
-   **Knowledge Base**: Comprehensive details on Indian credit cards (fees, APR, lounge access, etc.).

### 3. Sub-Agent: `card_application`
-   **Role**: Data collection specialist.
-   **Responsibilities**:
    -   Collecting applicant details (Name, Income, PAN, etc.) in a structured format.
    -   Completing the application process.

## Technical Aspects

-   **Framework**: [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
-   **AI Model**: Gemini 2.5 Flash Native Audio (Multimodal Live API).
    -   *Note*: Uses native audio capabilities for low-latency voice interaction.
-   **Backend**: Python 3.11, FastAPI, WebSocket.
-   **Frontend**: Vanilla HTML/JS/CSS (located in `app/static`).
-   **Communication**: Real-time WebSockets with binary audio streaming.
-   **Infrastructure**: Dockerized application deployable on Google Cloud Run.

## Deployment Guide

### Prerequisites
-   Python 3.10+
-   [uv](https://docs.astral.sh/uv/) (recommended) or pip
-   Google API Key (for Gemini Live API) or Google Cloud Project (for Vertex AI)

### 1. Local Setup

**Clone and Install Dependencies:**

```bash
# Using uv (Recommended)
uv sync

# Using pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # or install manually
```

**Configure Environment:**
Create an `app/.env` file:

```bash
GOOGLE_API_KEY=your_api_key_here
# Optional: Set model
DEMO_AGENT_MODEL=gemini-2.5-flash-native-audio-preview-12-2025
```

**Run the Server:**

```bash
cd app
# Using uv
uv run --project .. uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Using pip
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Access the UI at `http://localhost:8000`.

### 2. Docker Deployment

**Build the Image:**
```bash
docker build -t voiceagents .
```

**Run Container:**
```bash
docker run -p 8080:8080 -e GOOGLE_API_KEY=your_key voiceagents
```

### 3. Deploy to Google Cloud Run

1.  **Build and Push Image**:
    ```bash
    gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/voiceagents
    ```

2.  **Deploy Service**:
    ```bash
    gcloud run deploy voiceagents \
      --image gcr.io/YOUR_PROJECT_ID/voiceagents \
      --platform managed \
      --region us-central1 \
      --allow-unauthenticated \
      --set-env-vars GOOGLE_API_KEY=your_key
    ```

## Live Environment

The application is deployed on Google Cloud Run:
- **Frontend URL**: `https://voiceagents-frontend-2ewjgqzoja-uc.a.run.app`
- **Backend API URL**: `https://voiceagents-2ewjgqzoja-uc.a.run.app`
