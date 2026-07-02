## 1. How token cost works

You are charged per token used, not per request.
Pricing is like:
$ per 1M tokens (just a unit scale)
Every API call is billed separately.
Formula:
Cost = (Input tokens / 1M) × input_price + (Output tokens / 1M) × output_price
Important insight:

- You do NOT wait until 1M tokens
- You pay incrementally per request

## 2. How chat / LLM works (very important)

LLM is stateless
It does NOT remember previous calls
To maintain context:

You must resend:

system message
user messages
assistant messages (if needed)

- This increases token usage over time

## 3. Roles in LLM system

system
defines behavior
rules / instructions
constant across requests
user
input from user
assistant
model response (used for conversation history)
tool
external function results (API, DB, etc.)

## 4. Your use case (bank transaction classifier)

You correctly identified:

- No need for chat history
- Each request is independent
- Only extract structured data

So best design:

User message → LLM → JSON → Backend DB update

## 5. Token usage in your case

Typical breakdown:

Component Tokens
System prompt ~50–300
User message ~10–20
Output JSON ~50–120

- Total per request: ~120–400 tokens

## 6. Example cost understanding

1 request ≈ fractions of a cent
1,000 requests ≈ a few cents
very low cost overall

## 7. Why tokens increase in chat apps

If history is included:

every previous message is resent
tokens grow linearly with conversation

- This increases cost significantly

## 8. Optimization techniques (MOST IMPORTANT PART)

- A. Avoid LLM calls (biggest saving)
  use regex / rules for simple transactions
  only call LLM for ambiguous input
- B. No chat history
  your use case does NOT need it
  keeps token usage constant
- C. Reduce output tokens
  short JSON keys (from, to, amt)
  no explanations
  no extra fields
- D. Batch requests
  multiple transactions in one call
  saves system prompt overhead

- ~20–40% savings

- E. Hybrid system (best architecture)
  Rule engine → LLM fallback → DB update
  ⚡ F. Prompt caching
  helps only for repeated system prompts
  limited benefit in your case (~5–20%)
  ⚡ G. Structured input (optional)
  force format → reduces LLM reasoning cost

## 9. Bulk vs single request

Mode Efficiency
Single request simple
Bulk request ~20–40% cheaper

## 10. Key takeaways

Most important ideas:

- LLM is stateless
- Tokens = input + output text
- Cost is per request usage
- History increases cost linearly
- System prompt is repeated every request

## Final architecture for your project

Best low-cost design:

User Input
↓
Rule Engine (fast check)
↓
If simple → DB update (NO LLM)
Else → LLM (nano model)
↓
Structured JSON
↓
Database update
💡 One-line summary

Your biggest savings come NOT from reducing prompts, but from reducing how often you call the LLM and keeping outputs compact.
