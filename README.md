# Claude plugin for product managers

A free / open source **Claude plugin for product managers**.

Created by Andy Brudtkuhl ([@abrudtkuhl](https://x.com/abrudtkuhl)).

Start here: https://pmprompt.com/claude-product-management-plugin

It works with:
- **Claude plugins** (directory): https://claude.com/plugins
- **Cowork plugins**: https://claude.com/blog/cowork-plugins
- **Claude Code** (terminal)

Links:
- Landing page: https://pmprompt.com/claude-product-management-plugin
- Skills library: https://pmprompt.com/skills
- Agent skills guide: https://pmprompt.com/blog/ai-agent-skills-guide
- Repo: https://github.com/pmprompt/claude-plugin-product-management

## What this is

Plugins bundle skills/commands so you can install them once and reuse them across projects.

Once installed, these skills show up under the `pmprompt` namespace:

- `/pmprompt:prd-writer`
- `/pmprompt:jobs-to-be-done`
- `/pmprompt:working-backwards`

## Install

### Option 1: Claude Code (local dev / from GitHub)

```bash
git clone https://github.com/pmprompt/claude-plugin-product-management.git
cd claude-plugin-product-management
claude --plugin-dir .
```

Then run any skill:

- `/pmprompt:feature-prioritization-assistant`
- `/pmprompt:positioning-canvas`

## Skills included

| Skill | Description |
|------|-------------|
| [ab-test-designer](skills/ab-test-designer/) | Design robust A/B test experiments. Use when testing a new feature, validating a hypothesis, or optimizing conversion rates. |
| [competitive-analysis-framework](skills/competitive-analysis-framework/) | Create detailed competitive analysis and positioning. Use when launching a new product, planning positioning, or identifying differentiation opportunities. |
| [design-sprint](skills/design-sprint/) | Use when asked to "run a design sprint", "5-day sprint", "prototype in a week", "test ideas before building", or "Jake Knapp sprint". Helps teams go from problem to tested prototype in five days. The Design Sprint framework (created by Jake Knapp at Google Ventures) compresses months of work into one focused week. |
| [feature-prioritization-assistant](skills/feature-prioritization-assistant/) | Calculate RICE scores and prioritize features systematically. Use when building your product roadmap and need to make data-driven prioritization decisions. |
| [growth-loops](skills/growth-loops/) | Use when asked to "growth loops", "build a growth engine", "design a viral loop", "create a content loop", "move beyond paid acquisition", or "why isn't growth compounding". Helps design self-reinforcing growth systems where output becomes input. The Growth Loops framework (from Brian Balfour / Reforge and Elena Verna) shifts thinking from linear funnels to compounding loops. |
| [hierarchy-of-engagement](skills/hierarchy-of-engagement/) | Use when asked to "define our core action", "North Star metric", "accruing benefits", "improve retention mechanics", "hierarchy of engagement", or "Sarah Tavel framework". Helps consumer products identify the actions and benefits that drive long-term retention. The Hierarchy of Engagement framework (created by Sarah Tavel at Benchmark) maps progression from core action to mounting loss. |
| [hierarchy-of-marketplaces](skills/hierarchy-of-marketplaces/) | Use when asked about "marketplace strategy", "chicken and egg problem", "liquidity", "two-sided market", "tipping a marketplace", "GMV growth", or "Sarah Tavel marketplaces". Helps founders and product leaders build defensible marketplace businesses by sequencing supply and demand. The Hierarchy of Marketplaces framework (created by Sarah Tavel / Benchmark) provides a progression from focused launch to market dominance. |
| [hooked-model](skills/hooked-model/) | Use when asked to "build habit-forming products", "Hooked model", "trigger action reward investment", "create sticky behavior loops", or "design habit loops". Helps design products that form unprompted user habits. The Hooked Model (created by Nir Eyal) explains how products create habits through Trigger, Action, Variable Reward, and Investment. |
| [jobs-to-be-done](skills/jobs-to-be-done/) | Use when asked to "jobs to be done", "JTBD", "why customers churn", "prep for customer interviews", "hire and fire products", or "find real competitors". Helps discover unmet needs and the context behind purchasing decisions. The Jobs to be Done framework (created by Clayton Christensen and Bob Moesta) explains why customers hire and fire products. |
| [monetizing-innovation](skills/monetizing-innovation/) | Use when asked about "pricing strategy", "willingness to pay", "value metric", "packaging tiers", "good better best pricing", "subscription vs usage pricing", or "price before product". Helps design products customers will pay for and choose pricing models that capture value. Based on Madhavan Ramanujam's Monetizing Innovation framework from Simon-Kucher. |
| [okrs](skills/okrs/) | Use when asked to "set OKRs", "objectives and key results", "quarterly OKR planning", "align objectives", "measure OKR progress", or "focus priorities with OKRs". Helps teams focus on what matters most and create a cadence of progress. The OKR framework (originated by Andy Grove at Intel, popularized by John Doerr at Google) creates alignment, focus, and learning cycles. Christina Wodtke's Radical Focus approach emphasizes simplicity and avoiding common pitfalls. |
| [opportunity-solution-trees](skills/opportunity-solution-trees/) | Use when asked to "opportunity solution tree", "OST", "Teresa Torres", "map customer opportunities to outcomes", "structure discovery around opportunities", or "compare solutions for a customer need". Helps product teams connect outcomes to customer opportunities and test solutions with Opportunity Solution Trees (created by Teresa Torres). |
| [pmf-survey](skills/pmf-survey/) | Use when asked to "PMF survey", "measure product-market fit", "40% rule", "Sean Ellis test", "Rahul Vohra method", or "how disappointed would you be". Helps quantify product-market fit and systematically improve it. The PMF Survey framework (created by Sean Ellis, popularized by Rahul Vohra at Superhuman) measures how disappointed users would be without your product and turns that data into a roadmap. |
| [positioning-canvas](skills/positioning-canvas/) | Use when asked to "position my product", "positioning canvas", "differentiate from competitors", "figure out our category", "repositioning", or "why customers should pick us". Helps define competitive alternatives, differentiated value, target customers, and market category. April Dunford's positioning framework from "Obviously Awesome" makes your product's value obvious to the right customers. |
| [prd-writer](skills/prd-writer/) | Generate comprehensive product requirements documents. Use when starting a new feature or product initiative and need structured documentation. |
| [product-led-growth](skills/product-led-growth/) | Use when asked about "product-led growth", "PLG strategy", "self-serve growth", "freemium model", "free trial design", "product-led sales", "PQL", or "bottoms-up growth". Helps design and optimize product-led growth motions where the product drives acquisition, activation, and monetization. Based on frameworks from Elena Verna and Hila Qu. |
| [product-led-seo](skills/product-led-seo/) | Use when asked to "product-led SEO", "programmatic SEO", "build programmatic pages", "organic acquisition for product", "decide if SEO is worth it", or "optimize for AI search". Helps evaluate whether SEO fits your business model and how to approach it as a product, not just marketing. The Product-Led SEO framework (created by Eli Schwartz) treats SEO as building products for search users. |
| [radical-candor](skills/radical-candor/) | Use when asked to "radical candor", "give feedback that cares", "have a difficult conversation", "challenge directly", "manage performance issues", or "give praise that lands". Helps deliver direct feedback while showing you care. The Radical Candor framework (created by Kim Scott) teaches how to challenge directly while caring personally. |
| [seven-powers](skills/seven-powers/) | Use when asked to "7 Powers", "build a competitive moat", "analyze defensibility", "find sustainable advantage", "economic moats", or "Hamilton Helmer framework". Helps identify durable competitive advantages. The 7 Powers framework (created by Hamilton Helmer) reveals the economic structures that protect business value from competition. |
| [shape-up](skills/shape-up/) | Use when asked to "shape up", "run a shaping session", "set an appetite", "scope a project without estimates", "betting table", or "ship in fixed cycles". Helps teams escape estimate-driven development and Scrum fatigue. The Shape Up method (created by Ryan Singer at Basecamp/37signals) uses fixed time boxes, variable scope, and collaborative shaping to ship meaningful work predictably. |
| [stakeholder-update-generator](skills/stakeholder-update-generator/) | Create compelling progress updates and release notes. Use when shipping a new feature or need to communicate progress to stakeholders. |
| [strategic-narrative](skills/strategic-narrative/) | Use when asked to "strategic narrative", "Andy Raskin", "tell our company story", "write a pitch deck", "explain why customers should care", or "movement narrative". Helps craft compelling narratives that define movements rather than just selling products. The Strategic Narrative framework (created by Andy Raskin) transforms pitches from feature lists into stories about change. |
| [thinking-in-bets](skills/thinking-in-bets/) | Use when asked to "thinking in bets", "make decisions under uncertainty", "think probabilistically", "avoid resulting", "separate decision quality from outcomes", or "reduce bias in decisions". Helps make explicit bets and evaluate decisions on process, not results. The Thinking in Bets framework (from Annie Duke) applies poker strategy to business and life decisions. |
| [trustworthy-experiments](skills/trustworthy-experiments/) | Use when asked to "run an A/B test", "design an experiment", "check statistical significance", "trust our results", "avoid false positives", or "experiment guardrails". Helps design, run, and interpret controlled experiments correctly. Based on Ronny Kohavi's framework from "Trustworthy Online Controlled Experiments". |
| [user-feedback-synthesizer](skills/user-feedback-synthesizer/) | Analyze collections of user feedback to identify patterns and themes. Use when you have user feedback from multiple sources that needs synthesis. |
| [working-backwards](skills/working-backwards/) | Use when asked to "working backwards", "PR/FAQ", "Amazon PR/FAQ", "write a press release", "define a new product", or "write a customer-focused PRD". Helps define products by starting with the customer problem and desired outcome before building. The Working Backwards process (developed at Amazon) forces clarity on customer value before committing engineering resources. |

## Install (via plugin directory / marketplace)

If/when you find this plugin in the Claude plugin directory, install it from there.

If you want to add the marketplace directly in Claude Code:

```text
/plugin marketplace add pmprompt/claude-plugin-product-management
/plugin install pmprompt
```

(Exact install UI may vary between Claude Code and Cowork.)

## Publishing / versioning

- Plugin manifest: `.claude-plugin/plugin.json`
- Marketplace metadata: `.claude-plugin/marketplace.json`

## Inspiration / credits

This plugin is inspired by the community ecosystem around Claude skills/plugins, including:
- Corey Haines’ Marketing Skills for Claude Code: https://github.com/coreyhaines31/marketingskills
- Firecrawl’s Claude plugin (MCP + plugin pattern): https://github.com/firecrawl/firecrawl-claude-plugin
- rjs/shaping-skills (conceptual inspiration for shaping/breadboarding): https://github.com/rjs/shaping-skills

## Safety / scope

This repo intentionally contains **no internal operating workflows**, private IDs, tokens, or customer data.
