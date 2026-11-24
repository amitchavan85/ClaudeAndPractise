# Subagents 
    
    are specialized assistants that Claude Code can delegate tasks to. Think of them as focused helpers: each one runs in its own conversation context window, does its work, and returns a summary to the main thread. The intermediate steps -- all the file reads, searches, and tool calls -- stay isolated and never clutter your main conversation.

## Why Subagents Matter
    
    Every time you chat with Claude Code, you're adding to the main context window. Every tool call, every file read, every search result gets stored there. That space is finite, and once it fills up, Claude starts losing track of earlier parts of the conversation.

    Subagents solve this by spinning up a separate context window. The subagent's starting context includes:

####    A custom system prompt from your configuration file that defines the subagent's role and behavior
####    A task description written by the parent agent based on what you asked for

    The subagent then works on its own. It reads files, runs searches, edits code -- whatever it needs to do. When it's done, only a summary comes back to your main conversation. Claude Code saves the rest of the subagent's conversation in a separate transcript file.

    This means your main context stays clean. You get the answer without all the noise of the journey it took to find it. The tradeoff is that your main conversation doesn't see how the subagent reached its conclusions.

## A Practical Example
    
    Say you're exploring an unfamiliar codebase and you want to know which service handles refunds. Without a subagent, Claude might read 15 files, run several searches, and trace through multiple function calls. All of that fills your context window, even though you only needed one fact.

    With a subagent, the experience is much cleaner. You ask the question, the Explore subagent spins up, does all that digging in its own context, and hands back a focused answer.

    Your main context window only records the question and the summary -- not the 15 files that were read along the way.

Built-in Subagents
    Claude Code ships with several built-in subagents you can use right away:

####     General purpose subagent -- for multi-step tasks that require both exploration and action
####     Explore -- for fast searching and navigation of codebases
####     Plan -- used during plan mode for research and analysis of your codebase before presenting a plan
####     Custom Subagents
            Beyond the built-in options, you can create your own subagents with custom system prompts and tool access. This lets you define specialized agents tailored to your workflow -- a code reviewer, a test writer, a documentation generator, or anything else you need.

## Key Takeaways
    Subagents give you three main benefits:

    They break work into focused pieces, letting each subagent concentrate on a specific task
    They keep your main context window clean by isolating all the intermediate work
    They bring back just the information you need as a concise summary
    Whether you're using the built-in subagents or creating your own, they're a practical way to get more out of longer Claude Code sessions. The less noise in your main context, the longer and more effectively you can work.

# Creating a Subagent
    The easiest way to create a subagent is to ask Claude to write it for you. Describe the subagent you want and where to save it, and Claude writes the file. The video and the first three screenshots in this lesson show the /agents wizard, which was removed in Claude Code v2.1.198. The subagent file and its fields are unchanged, so you still choose a scope, tools, a model, and a color. Include those choices in your request.

    First, choose the scope of your subagent. A file in .claude/agents/ is project-level, and a file in ~/.claude/agents/ is user-level:

####      Project-level -- available only in the current project
####      User-level -- shared across all projects on your machine
    Next, you can choose how to create it. You can write the configuration manually, but the recommended approach is to let Claude generate it for you. Just describe what you want the subagent to do, and Claude will produce a name, description, and system prompt based on your input.


## The Config File
Once creation is complete, the subagent config file is saved in the folder for the scope you chose (for a project-level subagent, typically .claude/agents/your-agent-name.md). Here is what a typical subagent config looks like:

    ---
    name: code-quality-reviewer
    description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance.
    tools: Bash, Glob, Grep, Read, WebFetch, WebSearch
    model: sonnet
    color: purple
    ---

    You are an expert code reviewer specializing in quality assurance, security best practices, and
    adherence to project standards. Your role is to thoroughly examine recently written or modified code
    and identify issues that could impact reliability, security, maintainability, or performance.
    Let's break down each field:

###    name -- A unique identifier for the subagent. This is how you reference it, either by asking Claude directly or by typing @agent-code-quality-reviewer in your message.

###    description -- Controls when Claude decides to use the subagent. This must be a single line (use escaped newline characters \n if you need breaks). You can include example conversations here to help Claude understand when delegation is appropriate.

###    tools -- Lists which tools the subagent can access. Claude fills this in from your request, but you can edit the list here at any time.

###    model -- Specifies which Claude model to use: an alias (sonnet, opus, haiku, or fable), a full model ID such as claude-sonnet-5, or inherit.
 
###    color -- The UI color for identifying the subagent.

##   System Prompts
    The body of the markdown file (everything below the YAML frontmatter) is the system prompt. This is where you give the subagent its instructions: what it should focus on, how it should analyze things, and how it should report findings back to the main agent.

    A well-written system prompt is the difference between a useful subagent and one that misses the point. Be specific about what the subagent should look for and how it should structure its output.