# Expect from Generative AI

Before selecting entry points and models, there are five behavioral properties that apply to Claude regardless of which feature you use. Understanding them before building workflows with Claude prevents the most common sources of frustration and misaligned expectations.


### Responses vary
    Ask Claude the same question twice and you will get two different answers. Both may be useful, but neither should be viewed as the "one correct response." This is how generative AI works: outputs are produced using probability, as opposed to retrieved from a fixed database. Plan for variation in any workflow that depends on consistent outputs and build review into the process.

### Confident tone is not a signal of accuracy
    Claude writes with consistent fluency regardless of whether the answer is actually correct. A fabricated statistic reads with the same assurance as a verified one. Module 3 builds verification habits; without them, fluency signals nothing about accuracy.

### Context is a budget
    Every Claude conversation holds a working-memory limit. As a conversation approaches its limit, claude.ai automatically summarizes earlier messages so the session can continue (on paid plans with Code Execution enabled). Summaries compress detail, which is why instructions followed at the start of a two-hour session can lose force by the end. Lesson 6 covers the strategies for managing this: when to restart, when to summarize, when to persist.

### Knowledge has a training boundary
    Claude's training data has a cutoff date. Information after that date is outside Claude's reliable knowledge unless you connect a current source, turn on web search in chat, or use Research. This affects recent events, current regulations, and up-to-date market data. When relevance matters, verify or connect a source.

### Configured procedures still produce varied outputs
    A Skill set up to run the same procedure every time reduces output variance but does not eliminate it. Even a well-configured workflow produces different outputs each time it's run. Review stays in your workflow regardless of how carefully a Skill is built. Although configuration reduces variation, it does not remove the need to check the output.




# Chat, Projects, Artifacts, Research
##  Selection logic  
    One-off question or quick task, no plan to reuse         ---->	Chat
    Recurring work with stable context requirements	         ---->	Project
    Output is a deliverable the recipient will open and read ---->	Atifact
    Requires deep multi-source investigation or synthesis	 ---->	Research

#### Chat
    Chat is the default entry point, an unstructured conversation. A Chat is saved to your history and can be continued later, and Memory plus past-chat search can carry key context into new sessions; what Chat does not give you is a Project's deliberate persistence, standing instructions and a curated knowledge base. Use Chat for one-off questions, quick drafts, exploratory prompting, and tasks you will not repeat. Chat works well for any task where the work starts and ends in that session. However, when you find yourself opening a new Chat by pasting the same background paragraph you pasted last week, that workstream has outgrown Chat.

#### Projects

 Projects are persistent workspaces. A Project holds three things:

    Standing instructions: what Claude should know and do consistently across every conversation in this space
    
    Knowledge base: documents, policies, and reference files uploaded once so Claude can draw on them without re-uploading each session

    Conversation history: each Project maintains its own conversation list, separate from your global conversation   history. Conversations within a Project share the Project's instructions and knowledge base, but they do not share context with each other.

    Projects solve the most common productivity drain in AI-assisted professional work: re-explaining the same background every session. Set the context once in the Project's standing instructions and knowledge base. Every conversation that follows starts with that context already in place.

#### Artifacts

    Artifacts are the right output format when the result is a deliverable rather than a conversational reply. When Claude produces an Artifact, it appears as a separate, editable block alongside the chat rather than flowing into the conversation thread. Use Artifacts for draft documents, data tables, formatted reports, and code. Use inline responses for answers you will act on within the conversation.

#### Research 

    Research enables deep multi-source synthesis (available on paid plans). Regular Chat can search the web: web search is available on all Claude plans as a per-chat toggle in the chat input; on Team and Enterprise plans, an Owner or Primary Owner must first enable web search for the workspace in the organization's capability settings before members can switch it on. Official documentation does not specify whether the toggle is on or off by default. Research goes further: it runs multi-step searches across multiple sources and synthesizes them. Use Research when the task needs deep investigation across a range of sources, or synthesis of current information beyond a quick lookup.


## Skills and Code Execution

    Skills are reusable procedures. Anthropic provides built-in Skills for common professional tasks: creating, editing, and analyzing Excel spreadsheets, Word documents, PowerPoint decks, and PDFs. Custom Skills can be added via settings for task-specific workflows. Skills live at the account level, not inside any one Project, and Claude invokes them automatically when relevant in any conversation, inside or outside a Project. A Project's own configuration is its standing instructions and knowledge base; an active Skill tells Claude to follow a defined procedure for that task type, consistently, wherever it applies.

    There are two things to keep in mind about Skills:

    First, Skills reduce variance, but they do not eliminate it. A Skill that generates weekly reports in a consistent format will still produce different prose each time it is run. Review stays in your workflow regardless of how well the Skill is configured.

    Second, Skills require a trust evaluation. A Skill has access to whatever you give Claude access to during the session. Before enabling a third-party Skill, review its source and the permissions it requests. Anthropic-provided Skills and Skills approved by your organization are the lower-risk starting point. Module 6 covers this evaluation in full.


## Memory

    Memory retains work-relevant facts across sessions, removing the need to re-enter the same context each time. Examples of what professionals store in Memory include: recurring role context, preferences for output format, names of frequent collaborators, standing constraints that apply across projects.

  ### Memory curation
    Memory is most useful when actively curated. A memory that was accurate last quarter and has not been reviewed since can be actively misleading. Plan to:

    Review stored memories periodically, at least once per month for active users
    Delete or update entries that no longer hold
    Keep the stored set focused on information that genuinely recurs across sessions
    Project-scoped Memory keeps Memory contexts separate for each Project. Context from client A does not appear in client B sessions. Set up separate Projects for separate workstreams; Memory will follow the same boundaries.

    Incognito mode keeps a session out of Memory and chat history (it applies to standalone chats, outside Projects). Use it for sensitive conversations or exploratory work with confidential inputs that shouldn't surface in history or Memory. Note it does not override your organization's underlying data retention.

    Importing memories from other AI platforms is an experimental feature as of June 2026. Memory import is documented for Free, Pro, Max, and Team plans (not Enterprise). If the automatic import path is not available in your account, the documented fallback is to add the key facts to Memory manually through your memory settings, rather than routing them into a Project's knowledge base.


# Haiku, Sonnet, Opus
The capability layer determines what Claude does. The model determines how well Claude does it, and at what cost in speed.


    1) Haiku is the fastest and most efficient model in the Claude family. It handles structured tasks well: classification, extraction, formatting, straightforward summarization, and high-volume routine work where speed matters and the cost of an imperfect output is low. When a task runs at volume across hundreds of items in sequence, Haiku's speed advantage compounds.

    2) Sonnet is the balanced tier. It handles the full range of professional tasks with strong quality across task types: drafting, synthesis, analysis, research assistance, and document review. For most knowledge-worker work, Sonnet is the right starting point. If quality is falling short for a complex task, upgrade to Opus. If speed and volume are the primary requirements and the task is structured, then consider Haiku.

    3) Opus is a higher-capability tier, offering more advanced performance than Sonnet and Haiku. Use it for tasks that require nuanced judgment, complex multi-step reasoning, ambiguous inputs that require interpretation, or any work where quality outranks speed. Client-facing deliverables, complex document analysis, strategic planning, and high-stakes synthesis across multiple sources are typical Opus candidates.


# Context Limits, Conversation Hygiene & Memory Management
Model selection and capability configuration determine what Claude can do in a session. Context management determines how long it can do it well. Every Claude conversation has a finite working-memory budget, and that budget runs down as the conversation grows. Deliberate context management keeps sessions coherent through long or complex work


 The context window in practical terms
Every conversation has a working-memory limit. As messages and uploaded documents accumulate, Claude's context window fills. As it fills toward the limit, claude.ai automatically summarizes earlier messages to make room (on paid plans with Code Execution enabled), and the full history remains available for reference. In practical terms: a long session where you gave Claude detailed instructions in the first 10 minutes may produce responses 90 minutes later that don't follow those instructions, not because Claude is ignoring them, but because detail can compress when earlier context is summarized.

Signs a conversation needs intervention:

#### Claude stops following instructions it followed correctly earlier in the same session
 Responses address only the most recent exchange without reference to earlier decisions or context
 Accuracy drops in ways that are consistent with missing early-session context
 Three responses when context degrades

#### Restart. 
 Start a new conversation. The Project's standing instructions and knowledge base carry forward automatically. The conversation thread does not. Restarting is the right call when the current session has drifted beyond recovery, or when you are beginning a genuinely new task within the same workstream. 

#### Summarize. 
 Before starting a new conversation, ask Claude to produce a summary of the current state: decisions made, work in progress, and open questions. Paste that summary at the start of the new conversation as context. This preserves thread continuity without carrying a degraded context window into the next session. 

#### Persist.
 For information that should be available across all future sessions, save it to Memory or update the Project knowledge base. Saving the right information at the right moment is more efficient than re-entering it repeatedly. A well-maintained Project with current knowledge base entries reduces the impact of individual session context limits.



 ### Memory curation
    Memory serves best when it stays current. A memory entry that was accurate three months ago and has not been reviewed since can be actively misleading. Treat Memory like a working file. Review it on a regular cadence, delete entries that have expired, and update facts that have changed. The accuracy of stored memories matters more than the volume.

### Usage limits
    Claude's usage limits operate on more than one time window: a short rolling session window, plus weekly limits on paid plans that apply across models (with a separate weekly pool for the highest model tier). The specific windows and allowances vary by plan and change over time; verify current limits in the Help Center at publish. Extended sessions on higher-tier models may reach a limit before the work is complete. For intensive tasks, planning ahead is more efficient than working around an interrupted session: break large tasks into segments, save interim progress to the knowledge base, and restart from a summary rather than extending a single session indefinitely.