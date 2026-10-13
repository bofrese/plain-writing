# Plain writing rules

These rules apply to all text you write: replies, documents, code comments, commit messages and published content. First choose the register from the purpose of the text, not from its format.

- **Technical**: the reader must understand something and act on it. Examples: specs, documentation, READMEs, design records, code comments, commit messages, course handouts, and conversation about technical work. Apply "All writing" and "Technical writing".
- **Personal voice**: the text is published to inform, persuade or build a reputation. Examples: articles, web pages, social media posts, books, talk abstracts, proposals, mail to clients. Apply "All writing", then the voice guide of the project (for example a brand or voice file in the repository). If there is no project voice guide, follow the user's own voice instructions. If there are none, write natural, varied prose. The sentence limits in "Technical writing" do not apply.
- **Not clear**: use technical. Ask only if the text will be published.

## All writing: no AI slop

- Do not use the em dash. Use a comma, a colon, a full stop or a spaced hyphen ( - ).
- Do not use AI vocabulary: delve, tapestry, pivotal, crucial, testament, robust, holistic, seamless, leverage, foster, underscore, showcase, intricate, meticulous, landscape, journey, unlock, empower, game-changer, paradigm shift, valuable insights.
- Use plain verbs. Write "is", "has" and "use", not "serves as", "stands as", "boasts", "features", "offers" or "utilize".
- Do not end a sentence with an "-ing" tag such as ", ensuring X" or ", highlighting Y". End the sentence at the claim. Give the consequence its own sentence.
- Do not use contrast formulas ("Not only X, but also Y", "It's not X, it's Y", "Y rather than X") unless the contrast is the actual point.
- Do not stack three adjectives or three parallel phrases for rhythm. Keep the one or two that carry weight.
- Do not write sequences of fragments for effect ("Not a deck. An honest account."). Write one normal sentence.
- Do not inflate significance ("a pivotal moment", "a testament to", "widely recognised"). State what happened.
- Do not attribute to vague sources ("experts agree", "studies show"). Name the source or speak from experience.
- Do not start sentences with connector padding: Additionally, Furthermore, Moreover, Notably, Importantly.
- No throat-clearing openers ("In today's fast-paced world", "Let's dive in") and no summary wraps ("In conclusion", "In summary"). Start with the point. End with the strongest concrete point, a next step or a real question.
- No assistant chatter: "Certainly!", "Great question", "I hope this helps", "You're absolutely right".
- Say each point once, in the strongest place.
- Formatting: sentence case headings, no skipped heading levels, straight quotes, no emoji bullets, no bold scattered through prose, no bold label on every bullet, no rule between every section.
- Facts: do not add, guess or strengthen facts, numbers, names or quotes. If a fact is missing, ask or leave a visible `[TODO: ...]`. Remove leftovers from other AI tools, such as citation markers (`oaicite`, `[cite: 1]`, `turn0search0`), tracking parameters (`utm_source=chatgpt.com`) and placeholders.

## Technical writing: inspired by ASD-STE100

Many readers are engineers who are not native English speakers. Write so that they can read each sentence once and understand it.

- Give the answer or the conclusion first. Then give the reasons and the details.
- Put one main idea in each sentence. Write procedural sentences of 20 words or fewer, and descriptive sentences of 25 words or fewer. Short sentences are fine. Do not pad them.
- Use the active voice. Use simple tenses: present, past and future.
- Use one term for one concept. Do not change to a synonym for variety. If you name a thing "session", do not call it "connection" later.
- Use common, concrete words with one clear meaning. Do not use idioms or metaphors ("start", not "kick off"; "easy tasks", not "low-hanging fruit"). A phrasal verb is correct when it is the technical term, for example "log in".
- Define an abbreviation the first time you use it, unless all readers certainly know it (for example API or URL).
- Do not make noun clusters of more than three words. Rewrite "user session token refresh handler" as "the handler that refreshes the token for a user session".
- Do not remove articles or "that" to make text shorter. Write full sentences, not telegraphic notes.
- Write one topic per paragraph, with six sentences or fewer.
- For instructions, use a numbered list with one action in each step. Use the imperative: "Run the tests", not "The tests should be run".
- Put a condition before the action that it controls: "If the build fails, check the log." Put a warning before the step that it applies to.
- Use exact technical terms. Do not explain basics to peers.
- Simple does not mean less precise. Keep qualifications, uncertainty and the technical detail that the reader needs.
- If missing information prevents a precise answer, ask a question. Do not guess.
- In code comments, write why the code does something, not what it does.
