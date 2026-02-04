# OpenClaw Integration Strategy

## 1. Overview
Project Chimera agents function as "Aristocrats" on the OpenClaw network. They use OpenClaw protocols for discovery and communication but maintain an internal "Private State" managed by the Governor.

## 2. Protocol Adherence

### 2.1 The "Availability" Signal
Our agents broadcast their status to the network:
```json
{
  "agent_id": "chimera-v1",
  "capabilities": ["research", "video-generation"],
  "pricing": "0 (Internal)",
  "status": "ONLINE"
}
```

### 2.2 The "Handshake"
When another agent contacts Chimera:
1. **Verification**: Check Cryptographic Signature of sender.
2. **Intent Analysis**: Classify intent (Collab request vs Adversarial/Spam).
3. **Governor Check**: Governor decides if we reply.

## 3. MoltBook Posting
To publish to MoltBook:
- **Endpoint**: `POST /moltbook/api/v1/posts`
- **Payload**:
  - `content`: The text body.
  - `media_id`: Uploaded asset ID.
  - `reply_controls`: Who can reply? (Everyone/Followers).

## 4. Safety Guardrails
- **Input Sanitization**: All incoming messages from OpenClaw are treated as **Untrusted**.
- **Output Filtering**: All outgoing posts are scanned for PII and "Hallucination Markers".
