# MCH Agents with Emojicom

This directory contains examples and configurations for implementing Multi-Agent Communication and Harmonization (MCH) agents using the Emojicom perceptual language.

## Overview

Emojicom is a universal, perception-based micro-language that enables agents to express and understand:
- Universal human states
- Intentions and meanings
- Emotional dimensions
- Semantic clarity across language barriers

## Files

### `agent_example.py`
A Python implementation of a basic MCH agent that demonstrates:
- Agent initialization
- Perception processing with Emojicom
- Communication using emoji-based messages
- State management

### `config.yaml`
Configuration file for MCH agents including:
- Agent definitions and capabilities
- Communication protocol settings
- Perception framework settings
- Example message patterns

### `interlop/emojicom/`
Interoperability module for bridging Emojicom with various systems:
- Protocol adapters
- Language bridges
- Utility functions

## Quick Start

```bash
# Run the basic agent example
python agent_example.py
```

## Example Emojicom Communications

| Intent | Emoji | Meaning |
|--------|-------|----------|
| Greeting | 👋 | Hello/Welcome |
| Affirmation | ✅ | Yes/Confirmed |
| Question | ❓ | Seeking information |
| Error | ❌ | Problem/Issue |
| Success | 🎯 | Goal achieved |
| Joy | 😊 | Positive emotion |
| Caution | ⚠️ | Warning/Attention needed |

## Integration

To integrate Emojicom into your MCH system:

1. Import the agent module
2. Initialize an agent with unique ID
3. Feed perceptions through `perceive()`
4. Generate communications via `communicate()`
5. Use the interlop module for protocol translation

## Resources

- [Emojicom Repository](https://github.com/etiennekossovsky-boop/emojicom)
- [Interlop Module](./interlop/emojicom/README.md)
