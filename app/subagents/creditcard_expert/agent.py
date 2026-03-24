"""Credit Card Expert Agent definition for Cymbal Bank."""

import os
import sys
import yaml
from typing import Optional

from google.adk.agents import Agent
from subagents.card_application.agent import agent as card_application

# Add project root to path to allow absolute imports if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def load_prompt():
    """Load the prompt from the prompt.yaml file."""
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.yaml")
    with open(prompt_path, "r") as file:
        prompt_data = yaml.safe_load(file)
    return prompt_data.get("system_instruction", "")

agent = Agent(
    name="creditcard_expert",
    description="Use this sub-agent to answer any queries related to Indian credit cards, their features, eligibility, fees, or rewards.",
    model=os.getenv(
        "DEMO_AGENT_MODEL",
        "gemini-live-2.5-flash-native-audio" if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").upper() == "TRUE" else "gemini-2.5-flash-native-audio-preview-12-2025"
    ),
    sub_agents=[card_application],
    instruction=load_prompt(),
)
