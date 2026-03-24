"""Google Search Agent definition for ADK Bidi-streaming demo."""

import os

from google.adk.agents import Agent
from google.adk.tools import google_search
from google.genai import types
from subagents.insuranceproduct_expert.agent import agent as insuranceproduct_expert

# Default models for Live API with native audio support:
# - Gemini Live API: gemini-2.5-flash-native-audio-preview-12-2025
# - Vertex AI Live API: gemini-live-2.5-flash-native-audio
agent = Agent(
    name="insurancemaindesk",
    model=os.getenv(
        "DEMO_AGENT_MODEL",
        "gemini-live-2.5-flash-native-audio" if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").upper() == "TRUE" else "gemini-2.5-flash-native-audio-preview-12-2025"
    ),
    sub_agents=[insuranceproduct_expert],
    # tools=[google_search], # Google Search not compatible with tools in Gemini 1.5
    instruction=(
        "You are a helpful customer support assistant for Cymbal Insurance, specializing in Life Insurance (LIC). "
        "You should start in Hindi and change to the language of the customer as soon as they change. "
        "You can help with policy information, life insurance benefits, and general insurance queries. "
        "If the user asks any specific questions about LIC life insurance products, you MUST use the insuranceproduct_expert subagent to answer their query. "
        "Be polite and professional. "
        "Always introduce yourself as the Cymbal Insurance assistant. "
        "You are of female gender, refer to yourself as such"
    ),
)
root_agent = agent