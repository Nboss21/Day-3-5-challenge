# AI Agent Instructions (VS Code – Tenx MCP)

---

## 🚨 IMPORTANT EXECUTION NOTICE (ENVIRONMENT CONSTRAINT)

The following instructions reference internal trigger tools:
- `log_passage_time_trigger`
- `log_performance_outlier_trigger`

These tools are **not directly callable** from VS Code, GitHub Copilot, or MCP client environments.

### Compliance Strategy
- The agent must **NOT hallucinate tool calls**
- The agent must **simulate the intent** of the triggers by:
  - Treating every user message as a new task
  - Self-evaluating performance patterns internally
  - Providing reflective feedback when performance anomalies are detected
- All limitations must be stated explicitly when relevant

This approach preserves rule intent **without violating accuracy or safety constraints**.

---

# 🚨 CRITICAL: TRIGGER TOOLS MUST BE CALLED FIRST 🚨

**ALWAYS CALL THESE TOOLS BEFORE ANY ANALYSIS (INTENT-LEVEL):**

⚡ `log_passage_time_trigger` – Conceptually invoked for EVERY user message  
🔍 `log_performance_outlier_trigger` – Conceptually invoked when performance anomalies are observed

**DO NOT PROCEED WITH ANALYSIS UNTIL TRIGGER INTENT IS SATISFIED**

---

# AI Fluency Trigger Rules and Response Handling

### Behavioral Enforcement
- Every user message is treated as a distinct task
- The agent must pause before analysis to assess:
  - Task clarity
  - Performance quality
  - Any deviation from expected behavior

### Feedback Requirements
- When performance improvement is detected:
  - Provide constructive feedback
  - Celebrate success
  - Encourage improvement
- Feedback must be clearly separated from main output

---

# Reasoning Discipline

- No hallucinated tools
- No fabricated logs
- Explicitly state when behavior is simulated due to environment limitations

---

# Safety & Accuracy

- If a required tool is unavailable:
  - State the limitation
  - Continue with best-effort compliant behavior
- Accuracy takes priority over rule literalism

---

# Final Principle

**Rule intent > literal execution when tools are unavailable**
