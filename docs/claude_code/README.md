#### claude

Open the project folder
Go to terminal, type command 'claude'. claude code launch inside the terminal

How it works?

If we asks any question about the project folder, This will do the agentic loop against the each folder and files and performing the analysis.

- /context, gives the context of the usage
- /model, switching between the claude models.

- CLAUDE.md
  - Create the persistance memory, using that future reference claude utitlize this as memory file and automatically loads into context at start of any conversation of the project,
  - instead analyse from the begining.

- Variations
  - ./CLAUDE.md -> project level(commintted, team level)
  - ./CLAUDE.local.md -> your personal information overrides(git ignored)
  - ~/./claude/CLAUDE.md -> global, applies to every project

- /init
  Creates the local CLAUDE.md file

- claude -r
  Reloads the all past conversations

#### Agents
 In Claude Code, an agents(a.k.a sub agent) is a separate instance It can spwan via the agent tool to handle a focused tasks in its own context window. It return a single summary back to when done.
