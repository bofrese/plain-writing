# plain-writing

A Claude Code plugin that removes AI slop from the text that Claude writes. It also makes technical text easy to read for engineers who are not native English speakers.

Readers notice generated text quickly: em dashes, "delve", "robust", ", ensuring seamless integration", three adjectives in a row, "In conclusion". When they notice it, they stop trusting the content. This plugin gives Claude one short set of rules that stops these patterns before they get into the text.

## What it does

The plugin selects a register from the purpose of the text, not from its format:

| Register | Used for | Rules |
|---|---|---|
| Technical | Specs, documentation, READMEs, code comments, commit messages, conversation about technical work | No AI slop, plus a plain style inspired by [ASD-STE100](https://www.asd-ste100.org/) (Simplified Technical English) |
| Personal voice | Articles, web pages, posts, books, proposals, mail to clients | No AI slop, plus your own voice guide |

The technical style takes a few writing rules from ASD-STE100: the answer first, short sentences with one idea each, one action per step, conditions before actions, the active voice, one term for one concept, no idioms and no telegraphic notes. Simple does not mean less precise: the rules keep qualifications, uncertainty and necessary detail. It does not use the STE controlled dictionary. That dictionary is for aircraft maintenance manuals, and it makes design discussions difficult to read. The text is inspired by STE. It is not STE-compliant.

All the rules are in one file: [`skills/plain-writing/references/rules.md`](skills/plain-writing/references/rules.md). Read it before you install the plugin. It is under 50 lines.

## Install

```
/plugin marketplace add bofrese/claude-plugins
/plugin install plain-writing@bofrese-plugins
```

## How it works

- A `SessionStart` hook loads the rules into each session. The rules then apply to all text, including chat, code comments and commit messages.
- The `plain-writing` skill contains a procedure to rewrite or review existing text. Ask "check this README for AI slop" or "rewrite this page with plain-writing".
- To apply the rules only when a skill asks for them, set the option `always_on` to `false` in `/config`.

The rules are instructions to the model. They make AI slop much less frequent, but they do not guarantee that it never occurs. To find what is left, ask for a review.

## Add your own voice

The plugin does not contain a personal voice. For published text, it uses one of these, in this sequence:

1. The voice guide of the project, for example a brand or voice file in the repository.
2. Your own voice instructions, for example in `~/.claude/CLAUDE.md` or in a voice skill that you wrote.
3. If neither exists: natural, varied prose that follows the "All writing" rules.

For example, add one line to `~/.claude/CLAUDE.md`:

```
For personal-voice writing with no project voice guide, use my voice guide in ~/writing/voice.md.
```

## Use with other AI tools

`rules.md` is plain markdown with no Claude-specific syntax. Copy it into the instruction file of another tool, for example `AGENTS.md`, or refer to it from that file.

## Use from your own plugin

Add the plugin as a dependency in your `plugin.json`, and tell your writing skills to apply the `plain-writing` rules:

```json
"dependencies": ["plain-writing@bofrese-plugins"]
```

## License

Apache-2.0
