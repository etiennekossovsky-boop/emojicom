# MCH Agents with Emojicom

This directory contains examples and configurations for implementing Multi-Agent Communication and Harmonization (MCH) agents using the Emojicom perceptual language.

## 📋 Overview

Emojicom is a universal, perception-based micro-language that enables agents to express and understand:
- Universal human states
- Intentions and meanings
- Emotional dimensions
- Semantic clarity across language barriers

## 📁 Directory Structure

```
examples/mch-agents/
├── agent_example.py          # Python MCH agent implementation
├── config.yaml               # Agent configuration & protocols
├── README.md                 # This file
├── LICENSE.md                # Dual-licensing information
├── mapping.md                # Emojicom symbol mappings
├── sequences.md              # Communication sequences
├── use-cases.md              # Real-world applications
└── interop/                  # Interoperability framework
    ├── emojicom/            # Language integration layer (HCCY 4.0)
    │   ├── mapping.md
    │   ├── sequences.md
    │   └── use-cases.md
    ├── mch/                 # Architecture & alignment (Apache 2.0)
    │   ├── architecture.md
    │   ├── alignment.md
    │   └── diagrams.md
    └── pito/                # Engine & integration (Apache 2.0)
        ├── engine.md
        ├── integration.md
        └── examples/
```

## 📜 Files & Modules

### Core Implementation Files

**`agent_example.py`** (Apache 2.0)
A Python implementation of a basic MCH agent that demonstrates:
- Agent initialization
- Perception processing with Emojicom
- Communication using emoji-based messages
- State management

**`config.yaml`** (Apache 2.0)
Configuration file for MCH agents including:
- Agent definitions and capabilities
- Communication protocol settings
- Perception framework settings
- Example message patterns

### Documentation

**`mapping.md`** (HCCY 4.0)
Comprehensive Emojicom symbol mappings:
- Core emotional states
- Perceptual states
- Intentional actions
- Communication protocols

**`sequences.md`** (HCCY 4.0)
Standardized communication sequences:
- Agent lifecycle patterns
- Multi-agent coordination
- State management
- Learning workflows

**`use-cases.md`** (HCCY 4.0)
Real-world applications:
- Distributed task processing
- Autonomous vehicles
- Healthcare monitoring
- Supply chain logistics
- IoT systems
- Educational AI
- Financial trading
- Crisis management

### Interoperability Framework

**`interop/emojicom/`** (HCCY 4.0)
Language integration layer:
- Symbol mappings
- Communication sequences
- Use cases and applications

**`interop/mch/`** (Apache 2.0)
Architecture and alignment:
- System architecture documentation
- Agent alignment framework
- Architecture diagrams

**`interop/pito/`** (Apache 2.0)
PITO Engine and integration:
- Engine specifications
- Integration patterns
- Implementation examples

## 🚀 Quick Start

```bash
# Run the basic agent example
python agent_example.py
```

## 📊 Example Emojicom Communications

| Intent | Emoji | Meaning |
|--------|-------|----------|
| Greeting | 👋 | Hello/Welcome |
| Affirmation | ✅ | Yes/Confirmed |
| Question | ❓ | Seeking information |
| Error | ❌ | Problem/Issue |
| Success | 🎯 | Goal achieved |
| Joy | 😊 | Positive emotion |
| Caution | ⚠️ | Warning/Attention needed |

## 🔗 Integration

To integrate Emojicom into your MCH system:

1. Import the agent module
2. Initialize an agent with unique ID
3. Feed perceptions through `perceive()`
4. Generate communications via `communicate()`
5. Use the interop module for protocol translation

## 📚 Learning Path

### Beginner
1. Read this README
2. Review `mapping.md` for symbol meanings
3. Run `agent_example.py`

### Intermediate
1. Study `sequences.md` for communication patterns
2. Explore `config.yaml` for customization
3. Review `interop/emojicom/` documentation

### Advanced
1. Deep dive into `interop/mch/architecture.md`
2. Study `interop/pito/engine.md`
3. Implement custom agents using `interop/pito/examples/`

## 📋 Licensing

This project uses **dual-licensing**:

- **Emojicom Language & Semantics**: HCCY 4.0 (Human-Centric Community License v4.0)
  - Language mappings, symbol meanings, semantic framework
  - Community-first, non-exploitative use

- **Technical Implementation & Code**: Apache 2.0
  - All Python code, configuration files, architecture modules
  - Open-source, commercially friendly

See [`LICENSE.md`](./LICENSE.md) for complete licensing details.

## 🤝 Contributing

Contributions are welcome! Please:

1. Follow the dual-licensing model
2. Maintain HCCY 4.0 for language components
3. Maintain Apache 2.0 for technical code
4. Document which license applies to your contribution
5. Submit pull requests with clear descriptions

## 🔗 Resources

- [Emojicom Repository](https://github.com/etiennekossovsky-boop/emojicom)
- [Interop Module](./interop/README.md)
- [Licensing Information](./LICENSE.md)
- [HCCY 4.0 License](https://hccy.org)
- [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

## 👤 Author

**Etienne Kossovsky**  
GitHub: [@etiennekossovsky-boop](https://github.com/etiennekossovsky-boop)

---

**Last Updated:** May 6, 2026  
**Repository:** [etiennekossovsky-boop/emojicom](https://github.com/etiennekossovsky-boop/emojicom)
