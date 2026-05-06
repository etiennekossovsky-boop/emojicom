#!/usr/bin/env python3
"""
MCH Agent Example using Emojicom

This example demonstrates how to create a basic MCH agent
that communicates using the Emojicom perceptual language.
"""

class EmojicommunicationAgent:
    """A simple agent that uses Emojicom for perception and communication."""
    
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.perception_state = {}
        self.communication_log = []
    
    def perceive(self, emoji_perception):
        """Process an Emojicom perception."""
        self.perception_state.update(emoji_perception)
        return self.perception_state
    
    def communicate(self, emoji_message):
        """Send an Emojicom communication."""
        self.communication_log.append(emoji_message)
        return emoji_message
    
    def __repr__(self):
        return f"Agent({self.agent_id})"


if __name__ == "__main__":
    # Create an agent
    agent = EmojicommunicationAgent("agent_001")
    
    # Example: perceive joy
    joy_perception = {"emotion": "😊", "intensity": 0.8}
    print(f"Perception: {agent.perceive(joy_perception)}")
    
    # Example: communicate understanding
    message = {"state": "✅", "action": "🎯"}
    print(f"Communication: {agent.communicate(message)}")
