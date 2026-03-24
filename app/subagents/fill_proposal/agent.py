"""Insurance Proposal Agent definition for Cymbal Insurance."""

import os
import sys
import yaml
from typing import Optional

from google.adk.agents import Agent

# Add project root to path to allow absolute imports if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def load_prompt():
    """Load the prompt from the prompt.yaml file."""
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.yaml")
    with open(prompt_path, "r") as file:
        prompt_data = yaml.safe_load(file)
    content = prompt_data.get("insurance_proposal_prompt", "")
    output_format = prompt_data.get("output_format", "")
    return f"{content}\n\n{output_format}".strip()

agent = Agent(
    name="fill_proposal",
    description="Use this sub-agent to capture the details of the user for an insurance proposal form.",
    model=os.getenv(
        "DEMO_AGENT_MODEL",
        "gemini-live-2.5-flash-native-audio" if os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").upper() == "TRUE" else "gemini-2.5-flash-native-audio-preview-12-2025"
    ),
    instruction=load_prompt(),
)
