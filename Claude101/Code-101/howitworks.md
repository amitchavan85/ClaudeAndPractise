# How Claude Code Works
Claude Code is different from typical chat applications. Understanding how it works under the hood will help you use it more effectively.

## The Agentic Loop
    Claude Code is best explained through the agentic loop:

## You enter a prompt into Claude Code.
    Claude gathers the context it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
    It takes action — for example, editing a file or running a command.
    It verifies the results and determines whether they achieve what your prompt set out to do.
    If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.
    Throughout this loop, you can add context, interrupt, or steer the model to help guide it toward your goal.
    ![ AngenticLoop ](https://github.com/amitchavan85/ClaudeAndPractise/tree/main/Claude101/Code-101/image.png)
    Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point

### Context
    Claude has a context window that determines how much of your conversation, file contents, command outputs, and more it can store and reference. Once you reach that limit, Claude Code compacts your conversation — automatically determining what it can remove or summarize to bring the context window back down to a usable size.

### Tools
    Tools are the backbone of how agents work. Most AI assistants simply take text in and return text out. Tools let Claude Code determine when to execute code to get closer to completing a task. This could be a file-reading tool, a web search tool, or any number of other capabilities. Claude Code uses semantic understanding to determine when to call a tool and how to use the output.

### Permissions
Claude Code has several permission modes:

## Manual: Claude asks for explicit permission before editing a file or running a shell command.
    Auto-accept: Files are edited without asking, and common filesystem commands like mkdir, mv, and rm run without asking too. Other commands still require approval.

    Plan mode: Claude reads files and runs shell commands to explore, without editing your source files, and compiles a plan of action before starting any work.

    Auto mode: Claude works without routine permission prompts while a classifier checks most actions in the background, targeted at blocking actions that are irreversible, destructive, or aimed outside your environment. When something is blocked, Claude usually finds a safer approach or asks you for the go-ahead.

    Which mode a new session starts in depends on your Claude Code version and settings.

    Claude Code asking for permission before running a bash command

    All of this can be configured in your settings file. Be cautious when skipping permissions — giving Claude Code free rein to run commands means a mistake could be harder to catch before it happens.