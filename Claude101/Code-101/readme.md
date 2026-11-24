
# Claude Code

Claude Code is an agentic coding tool that understands your codebase, edits your files, runs commands, and integrates with your existing developer tools to help you get things done faster. It's available in your terminal, Visual Studio Code, the Claude Desktop app, on the web, and in JetBrains IDEs.

## whatSeparates Claude Code from Claude?
    If you've used Claude.ai before, you might be wondering what makes Claude Code different. Unlike Claude.ai, Claude Code has direct access to your files, your terminal, and your entire codebase. Instead of copying and pasting code back and forth, it goes in and does the work itself.

    The key differentiator is that Claude Code works as an AI Agent.

## What is an Agent?
    An AI Agent is software that can interact with its environment and perform actions to complete a defined goal. At its core, this works by having a large language model operating in a loop in real time. AI Agents can have access to tools, external services, or even other AI Agents to help reach their goals.


## What Can Claude Code Actually Do?
    Here's what that looks like in practice:

    Read and understand your codebase. You can ask Claude Code to explain a feature or trace a bug throughout your code.
    Edit files across your project. Claude Code can refactor a function and update every file that references it.
    Run terminal commands. It can execute your build script, run your tests, install packages, and use the output to decide what to do next.
    Search the web. If it needs documentation or the latest API references, it can look that up for you.

## Using Claude Code Effectively

    To use Claude Code effectively, keep these three concepts in mind:

    The context window. Think of this as Claude's working memory. It can hold a lot, but not everything at once. This is where the "agentic" aspect comes in — Claude finds strategic ways to locate answers within your codebase without loading the entire thing into context.

    You control its permissions. Claude Code's permission modes let you choose how hands-on to be: it can ask you before running commands or making changes, or run in auto mode, where a background safety check screens most actions instead. You're always in control, whether you prefer a hands-on or hands-off approach.

    It can make mistakes. Just like any tool, Claude Code isn't perfect. It might misunderstand your intent, introduce a bug, or over-engineer a solution. Staying in the loop helps you catch these early.




# To remember Model selection is an architecture decision; effort tuning is a performance lever. Know which you're reaching for before making a recommendation.

## ![The model family](image2.png?raw=true "The model family")



# Seven paths to Claude Code, one right fit for your client
 ## By the end of this lesson, you can map a client's cloud commitments, governance requirements, and feature needs to the right deployment option and explain why you're not recommending the others.

 # The seven paths: Claude.ai Teams, Claude.ai Enterprise, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Azure AI Foundry, Anthropic API, and Anthropic Console.

# Three Categories

 ## ![Three Categories](image3.png?raw=true "The model family")

# Same Claude Code, four different rails

  ## ![Same Claude Code, four different rails](image4.png?raw=true "The model family")


# Course artifact · Lesson 1 contribution

## Deployment Decision Doc
    By the end of this course you'll have a Deployment Decision Doc for a sample client: the path recommendation plus the auth, network, gateway, and compliance posture that defends it. This lesson contributes the client profile and path recommendation.
#### --> 1 Open a new doc. Define a sample client: industry, developer count, primary cloud, and one committed-spend agreement (EDP, CUD, or MACC).

#### --> 2 Answer the four decision drivers for that client in one sentence each: commitments, buying route, compliance posture, admin ownership.

#### --> 3 Write the recommendation: one path, two sentences of rationale, and the single condition that would change your call.

#### --> 4 List the pre-kickoff blockers your path creates, each with an owner and a lead time, so the doc drops straight into the Day -14 checklist of an activation plan.




# A gap flagged at contract time is consulting. The same gap discovered in week three is a defect with your name on it.

## Six gaps that belong in your memo
    These are the differences between the cloud paths and Enterprise direct that clients actually hit. Match them to the path you recommended in 3.1.
    
## ![gap flagged](image5.png?raw=true "The gap flagged")

# A gap memo is one page, not a risk register
    Structure each line the same way:

   ### Name the gap: which capability is absent or reduced on this path
   ### Place the moment: which week, which person, which meeting the client would have hit it
   ### Lead with the mitigation: the plan already in place, stated before the limitation


#### Example "WebSearch is unavailable on Bedrock; your platform docs team would hit this in week one; we'll scope an approved MCP alternative in pre-kickoff" reads as preparation. A bare feature comparison table reads as a reason to stall the deal. Lead with the mitigation, and the memo becomes evidence you've done this before.



# The distinction that matters for enterprise clients
    Enterprise clients with multiple development teams making model calls will eventually ask: who is spending what? A proxy cannot answer that question. A gateway can.

## Five capabilities a proxy cannot replicate
    A proxy has no concept of a team, a budget, or a provider. A gateway has all three. These are the five things enterprise clients with more than one team will eventually ask for.

## ![gap flagged](image6.png?raw=true "The gap flagged")


# How Claude Code labels its own traffic
    Every Claude Code request carries attribution headers the gateway can read without parsing the request body. These three headers are the foundation of per-team chargeback.

   ## Session level
   #### X-Claude-Code-Session-Id
        A unique ID for the current Claude Code session. The gateway aggregates all requests in a session under this ID. This gives you session-level cost and duration reporting without touching request bodies.

   ## Subagent level
   #### X-Claude-Code-Agent-Id
        Present on requests from subagents. When Claude Code fans out into parallel subagents, each carries its own agent ID so the gateway can attribute cost to individual agent threads within the session.

   ## Parent relationship
   #### X-Claude-Code-Parent-Agent-Id
        Links a subagent to its parent. Enables full nested agent attribution: a session that spawns five subagents still rolls up correctly into a single team's cost report at the CoE review.

   ## What this enables
   #### Per-team chargeback
        Map gateway tokens to teams and the three headers give you cost per team per week, sessions per developer, and budget alerts before the next invoice. The CoE metrics review and the CFO conversation, served by the same data pipe.


## Non-technical leads: these headers are what enable per-team cost reporting in the Day 30 readout. You do not configure them. Claude Code sends them automatically. The gateway reads them.



## ![gap flagged](image7.png?raw=true "The gap flagged")


# Encryption at rest

## Where inference data lives, by path

### Anthropic direct

# AES-256, ZDR available
    Infrastructure-level disk encryption, with zero data retention as the no-server-side-persistence option for eligible Enterprise orgs. Topic 3 covers eligibility.


### Amazon Bedrock

# Client's AWS account, KMS optional

    AES-256 with AWS-managed keys, customer-managed keys available through KMS. Retention and key policy are governed by controls the client already audits.


### Google Vertex AI

# Client's GCP project, CMEK optional
    
    Google-managed encryption keys by default, customer-managed (CMEK) available. Same logic as Bedrock: the client's cloud governance applies.


### Microsoft Foundry

# The one that surprises people
    Foundry is an Azure-native deployment — Azure billing, Microsoft Entra ID authentication, and Azure RBAC policies apply. Confirm the data routing path with Anthropic before advising clients with cloud-specific data residency requirements. The "data never leaves our tenancy" question belongs in the path conversation, not the post-mortem.


# Zero data retention is a scope, not a slogan

## Claude Code inference, full stop
    Prompts and model responses from Claude Code sessions are processed in real time and not stored after the response returns, regardless of model, except where law or abuse-handling requires it. Admin capabilities like cost controls, analytics, and audit logs keep working.

## What it doesn't, and what it disables
    The trade the client must choose
    Not covered: claude.ai chat, Cowork, admin metadata like seat assignments, and anything third-party MCP servers process. Disabled outright because they require server-side storage: Claude Code on the web, remote sessions from the desktop app, and /feedback. And flagged sessions can still be retained up to 2 years under the usage policy. A client who wants ZDR and Claude Code on the web is choosing between them
