# MCH Agent Integration Examples

This directory contains practical examples of integrating different IA agent types with the MCH (Multi-agent Cognitive Hub) using Emojicom.

## Structure

```
mch-agents/
├── README.md                        # This file
├── 01-basic-communication/          # Basic agent-to-agent communication
├── 02-multi-agent-collaboration/    # Collaborative problem-solving
├── 03-negotiation-protocol/         # Multi-agent negotiation
├── 04-llm-agent/                    # Large Language Model integration
├── 05-vision-agent/                 # Vision/Image analysis agent
├── 06-symbolic-agent/               # Symbolic reasoning agent
└── 07-hybrid-agent/                 # Multi-modal hybrid agent
```

## Quick Examples

### 1. Basic Communication (Agent to Agent)

**Setup**: Two agents exchange greetings using Emojicom.

```python
# Agent A sends greeting
sequence_greeting = {
    "version": "0.2",
    "intention": "👋",  # Greeting
    "context": ["🌍"],  # Global context
    "actions": ["💬"],  # Communicate
    "metadata": {"agent_id": "agent_a"}
}

mch.dispatch_sequence(sequence_greeting, target_agent="agent_b")
```

**Sequence Flow**:
```
Agent A → 👋🌍💬 → MCH Hub → Validation → Agent B
                  ✅ Valid      Route    Accept
```

### 2. Multi-Agent Negotiation

**Setup**: Three agents negotiate resource allocation.

```python
sequence_negotiate = {
    "version": "0.2",
    "intention": "🤝",      # Negotiate
    "context": ["💰", "🎯"],  # Resources, goals
    "actions": ["💭", "⚖️"],  # Think, balance
    "constraints": ["🔒"],    # Secure
    "metadata": {
        "agent_id": "agent_a",
        "affected_agents": ["agent_b", "agent_c"],
        "topic": "resource_allocation"
    }
}

# MCH initiates 3-way negotiation
mch.protocols.negotiate(sequence_negotiate)
```

**State Progression**:
```
Init → Proposed → Accepted → Terms Negotiating → Agreed → Finalized
                                    ↓
                            (If disagreement)
                                    ↓
                            Disputed → Arbitration
```

### 3. LLM Agent Integration

**File**: `04-llm-agent/llm_with_mch.py`

```python
class LLMAgentMCH:
    def process_emojicom_sequence(self, sequence):
        # Parse Emojicom sequence
        intent = sequence['intention']
        context = sequence['context']
        actions = sequence['actions']
        
        # Convert to natural language
        prompt = self.sequence_to_prompt(intent, context, actions)
        
        # Generate LLM response
        response_text = self.llm_engine.generate(prompt)
        
        # Convert back to Emojicom
        response_sequence = self.text_to_sequence(response_text)
        
        return response_sequence
```

### 4. Vision Agent Integration

**File**: `05-vision-agent/vision_with_mch.py`

```python
class VisionAgentMCH:
    def process_emojicom_sequence(self, sequence):
        # Extract image reference from sequence
        image_ref = sequence['metadata'].get('image_url')
        
        # Analyze image
        visual_data = self.vision_model.analyze(image_ref)
        
        # Generate Emojicom response with findings
        response_sequence = {
            "version": "0.2",
            "intention": "🔍",  # Analyzed/Found
            "context": visual_data['entities'],
            "actions": ["📊"],  # Report
            "metadata": {
                "agent_id": "vision_agent",
                "findings": visual_data,
                "confidence": visual_data['confidence']
            }
        }
        
        return response_sequence
```

### 5. Symbolic Agent

**File**: `06-symbolic-agent/symbolic_with_mch.py`

```python
class SymbolicAgentMCH:
    def process_emojicom_sequence(self, sequence):
        # Convert sequence to logical rules
        rules = self.sequence_to_rules(sequence)
        
        # Apply symbolic reasoning
        conclusions = self.reasoning_engine.infer(rules)
        
        # Convert conclusions back to Emojicom
        response_sequence = self.conclusions_to_sequence(conclusions)
        
        return response_sequence
```

## Usage Patterns

### Pattern 1: Request-Response
```
Agent A → Request (intention + context) → MCH → Agent B
Agent B → Response (findings + recommendations) → MCH → Agent A
```

### Pattern 2: Broadcast
```
Agent A → Broadcast Sequence → MCH → [Agent B, Agent C, Agent D]
```

### Pattern 3: Negotiation
```
Agent A → Proposal → MCH → [Agent B, Agent C]
Agent B → Counter-proposal → MCH → [Agent A, Agent C]
Agent C → Arbitration → MCH → Final Decision
```

### Pattern 4: Workflow
```
Agent A (Coordinator) → Task 1 → Agent B → Result
                    ↓
                    → Task 2 → Agent C → Result
                    ↓
                    → Aggregate → Final Output
```

## Running Examples

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Communication
```bash
python -m examples.mch-agents.01-basic-communication.run
```

### Multi-Agent Negotiation
```bash
python -m examples.mch-agents.03-negotiation-protocol.run
```

### LLM Agent with MCH
```bash
python -m examples.mch-agents.04-llm-agent.run --model gpt-4 --mch-url localhost:8000
```

### Vision Agent with MCH
```bash
python -m examples.mch-agents.05-vision-agent.run --image-url https://example.com/image.jpg
```

## Key Concepts

### 1. Emojicom as Universal Protocol
All agents speak the same symbolic language, eliminating format mismatches.

### 2. MCH as Router
MCH intelligently routes sequences based on agent capabilities and constraints.

### 3. Semantic Preservation
Meaning is preserved across agent boundaries through Emojicom's canonical form.

### 4. Constraint Enforcement
MCH ensures all communication respects Emojicom constraints (neutrality, security, etc.).

### 5. Multi-Modal Reasoning
Different agent types can collaborate on complex problems without adapter layers.

## Advanced Topics

### Custom Protocols
Extend `mch.protocols` with your own communication patterns.

### Agent Plugins
Create custom agent types in `engines/mch/agents/plugins/`.

### Constraint Validation
Add domain-specific constraints in `engines/mch/validator.py`.

## Troubleshooting

### Agent Not Responding
1. Check MCH `/agents/{agent_id}` status endpoint
2. Verify sequence format with `/sequence/validate`
3. Check MCH logs for routing errors

### Sequence Translation Errors
1. Ensure sequence matches `spec/SPEC.md`
2. Validate against JSON schema: `spec/schema/sequence.schema.json`
3. Check agent-specific constraints

### Negotiation Deadlock
1. Review negotiation state machine in `sequences/mch-protocol/negotiation.yaml`
2. Escalate to arbitration via `/protocols/negotiate`
3. Review arbitration decision logs

## References

- **MCH Integration**: `../../MCH_INTEGRATION.md`
- **Emojicom Spec**: `../../spec/SPEC.md`
- **MCH API**: `../../api/mch.yaml`
- **Negotiation Protocol**: `../../sequences/mch-protocol/negotiation.yaml`

## Contributing

Have a useful agent integration example? Submit a PR following the structure above.

---

**Version**: 0.1.0-alpha  
**Status**: Examples in Development  
**Last Updated**: 2026-05-06
