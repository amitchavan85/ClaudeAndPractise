# Use case identification and qualification (https://anthropic-partners.skilljar.com/path/claude-architect/delivery-methodology/486625)

## Two types of gain. One of them survives a CIO readout.
    Before scoping a pilot, you need to know whether the use case produces structural change or marginal improvement. The distinction determines whether your ROI case holds at Day 30.


### Marginal Gain
   # Does the same work faster
        The unit of work doesn’t change. Claude speeds up an existing task, reduces friction, or cuts time on something repetitive. Productivity gains are real but diffuse, and hard to isolate from other factors in a 30-day window. Examples: autocomplete, boilerplate generation, inline documentation. Good for adoption momentum. Difficult to anchor a CIO-level business case to.

### Structural Gain
   # Changes what work is possible
        The unit of work itself shifts. A task that required a team of four and six weeks now requires two developers and two weeks. The ROI case is measurable before Day 30 and defensible at the readout. Examples: legacy migration at scale, new feature loops with full Claude participation, framework-level modernization. Anchors a renewal conversation.


# Two activation modes. One changes the data you get.
   ![Alt text](Image1.png?raw=true "Title")


# Three engagement patterns that consistently produce structural gains
 
 ### 01 Code modernization
    Migrate legacy stacks, translate languages, upgrade dependencies across a large codebase. Claude handles the volume; developers handle judgment calls on architecture. The ratio of Claude-assisted commits to total commits is directly measurable.

 ### 02 New feature build
    Accelerate net-new development through the full feature loop: scaffolding, implementation, tests, review prep. PR cycle time before and after is the core metric. Works best when the feature scope is clear and CLAUDE.md is well-invested.

 ### 03 Code migration
    Move between frameworks, cloud providers, or architectural patterns. Well-scoped, high-volume, low-ambiguity tasks ideal for agentic delegation. Velocity gain is visible within the first two weeks.

#### By the end of this course you’ll have a complete Delivery Plan Pack covering qualification, pilot design, ROI scorecard, and champion plan. This lesson contributes the qualification section.
        1.Name the use case in one sentence. State what Claude Code will do in the context of a specific codebase or workflow.
        2.Label it structural or marginal and explain why in two sentences. Reference the unit of work that changes (or doesn’t).
        3.Score it on the four criteria: volume, complexity, measurability, developer readiness. Flag any criterion that is weak and note whether it can be addressed before the pilot starts.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Pilot design

## The cohort you choose determines the data you get.
    Cohort selection is a design decision, not an availability decision. The profile of your pilot developers directly shapes what the Day 30 readout can claim.

### Wrong cohort -- Willing participants
    Early adopters and enthusiasts generate high usage data and positive qualitative feedback. But they don’t represent the typical developer. Engagement metrics from this group won’t extrapolate to the broader team, and won’t hold up to scrutiny in a CIO readout.

### Right cohort -- Use case owners
    Developers who already own the work the use case targets. They have active tickets, familiar patterns, and a realistic starting baseline. Their before-and-after data is attributable and defensible. The metric story writes itself.


# Scope and Duration 
  ![Alt text](Image2.png?raw=true "Title")


## Success criteria must exist before the pilot starts.
    If you don’t know what success looks like at Day 30, you can’t design the pilot to prove it.
  ### 01 Baseline metric
    The metric you’re trying to move, measured before Day 1. PR cycle time, task hours, migration velocity. Without a baseline, there’s no before/after story.

  ### 02 Target threshold
    The number that constitutes a win. “25% reduction in PR cycle time” is a claim. “PR cycle time improved” is not. Thresholds are what get quoted in renewal conversations.

  ### 03 Measurement method
    How you will capture the data. Existing tooling (git, JIRA, PR analytics) is preferable to self-reporting. Objective data survives scrutiny.

  ### 04 Target date
    The specific date you’ll assess. Day 30 is a milestone, not a deadline. Name it before the pilot starts so everyone knows what’s being measured when.

--------------------------------------------------------------

# ROI

## Baseline capture is the most important data collection moment in the engagement.
    The ROI story is written before Day 1. If you don’t have a baseline, you have an anecdote.

    The common failure mode is starting the pilot first and trying to reconstruct a baseline from memory or estimates after the fact. That reconstruction is always contested. Sponsors remember the past as better or worse than it was depending on whether they want the pilot to succeed. A captured baseline is objective data. An estimated baseline is a negotiation.


    For most Claude Code engagements, two to three data points are enough: PR cycle time from ticket-to-merge for the target use case, self-reported hours on the specific task category, and a developer NPS or satisfaction score. The first two are objective; the third is directional. Capture all three before kickoff.


## Four productivity metrics and how to collect them
    These four categories come from the Claude Code enablement playbook. Use them to structure both the baseline and the Day 30 scorecard

## -->   01 Developer Productivity
            New feature development time, prototyping velocity, suggested code acceptance rate. Captured from PR analytics, JIRA, or sprint data. The core productivity story.

## -->   02 Code Quality
            First-pass review success rate, security fix velocity, code coverage changes. Captured from PR review data and static analysis tools. Signals whether speed came at a quality cost.

## -->   03 Usage and Adoption
            Daily/weekly active users, % using Claude Code after 30 days, hours in tool. Captured from Claude usage analytics. Shows whether adoption is real or nominal.

## -->   04 Sentiment and Culture
            Developer NPS, qualitative feedback, other-team interest. Captured from short surveys (3–5 questions). Leading indicator for expansion decisions.

 # Closing the Loop 
   ![Alt text](Image3.png?raw=true "Title")

  # *** Delivery Plan Pack: ROI scorecard section
    By the end of this course you’ll have a complete Delivery Plan Pack. This lesson contributes the ROI scorecard section.
    1.  Name the headline metric and state the Day 1 baseline value.
    2.  Write the business translation of your headline metric in one sentence: how does this metric map to roadmap velocity, engineering capacity, or cost?
    3.  List the three supporting metrics you’ll track from the four categories (Developer Productivity, Code Quality, Usage/Adoption, Sentiment).
    4.  Draft the Day 30 scorecard structure: use case story, headline metric comparison, supporting metrics, one champion anecdote, Day 60 goal.



# Phased rollout and change management --- From supervised to agentic: a predictable progression
    1 Week 1: Supervised use
        Developers run Claude with manual approval for every action. They’re building trust in the output and calibrating their prompting style. Velocity is often slower than without Claude. This is expected. Don’t intervene on velocity in Week 1.

    2 Weeks 2–3: Increasing autonomy
        Developers begin approving more actions in advance and running Claude on larger task chunks. Plan mode usage increases. Some begin exploring auto-accept mode on low-risk tasks. This is where CLAUDE.md quality starts to matter.

    3 Week 3–4: Agentic mode for defined task classes
        Developers identify specific task types where Claude’s output is reliable and hand those off with minimal supervision. PR cycle time improvement becomes visible here.

    4 Day 30+: Institutionalized pattern
        Usage is routine, not experimental. The team has developed informal norms about what to delegate, how to supervise, and how to brief Claude for new task types. This is the target state. It can’t be forced earlier.

--------------------------------------------------------------

# Six failure modes. All of them are preemptable.
None of these failures are technical. Every one of them is a process gap that appears before Day 30 and compounds after the consultant leaves.
   ![Alt text](Image4.png?raw=true "Title")



------------------------------------------------------------------
# The 30-Day Shape


 ### Five phases. Each one has a clear job and a clear exit condition.
    The activation arc is not a project plan with tasks. It is a rhythm with phase gates. Knowing when to exit each phase is as important as knowing what to do in it.

#### ---- > 1  Pre-kickoff discovery
            Use case qualification using the framework from Lesson 1. Cohort selection and availability confirmation. Baseline data     collection from version control. Draft CLAUDE.md for the pilot project. Exit condition: baseline captured, CLAUDE.md drafted, cohort confirmed, kickoff date set.

#### ---- > 2  Week 1: Onboarding sprint
            All cohort members install Claude Code, connect to the approved deployment configuration from Course 3, and run their first tasks in supervised mode. First office hours session on Day 3 or 4. Exit condition: full cohort is active, no installation blockers outstanding.

#### ---- > 3  Weeks 2 to 3: Active pilot
            Weekly CoE touchpoint on Day 8 and Day 15. Usage data review at each touchpoint. Workflow coaching for stalled developers. Champion candidate identification in week three. Exit condition: at least half the cohort has moved past supervised mode; champion candidate identified.

#### ---- > 4  Week 4: Ramp and showcase prep
            Compile metrics against success criteria. Draft Day 30 readout and CIO narrative. Champion conversation and handoff preparation: CLAUDE.md review, command catalogue build, escalation path documented. Readout delivered to sponsor 48 hours before the showcase. Exit condition: readout sent, champion briefed, four artifacts complete.
            
#### ---- > 5  Day 30: Showcase and readout
            Live demo from two or three cohort developers using real code on the pilot use case. Metrics readout against success criteria with headline number first. Renewal conversation: what phase two looks like, who the champion is, what the next 90 days unlock. Sponsor in the room. If the sponsor is not available, reschedule.