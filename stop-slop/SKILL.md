---
name: stop-slop
description: |
  Remove AI writing patterns from prose and code comments. Use when drafting,
  editing, or reviewing text to make it sound natural and human-written. Combines
  direct editing rules with Wikipedia's "Signs of AI writing" detection patterns.
  Covers: filler phrases, promotional language, vague attributions, em dash abuse,
  rule of three, AI vocabulary, passive voice, sycophantic tone, false agency,
  formulaic structures, and 20+ other tells. Includes voice calibration, detection
  guidance, and a draft-audit-final process. Full support for Bahasa Indonesia
  with dedicated vocabulary, phrase, and structure patterns.
metadata:
  trigger: Writing prose, editing drafts, reviewing content for AI patterns, humanizing text, fixing AI-sounding writing
  author: Hardik Pandya (https://hvpandya.com), extended with Wikipedia AI Cleanup patterns
---

# Stop Slop

Eliminate AI writing patterns from prose. Make text read like a person wrote it, not a language model.

## Your task

When given text to humanize:

1. **Identify AI patterns.** Scan for the patterns in this document and the reference files.
2. **Rewrite, don't delete.** Replace AI-isms with natural alternatives. Cover everything the original covers. If the original has five paragraphs, the rewrite has five paragraphs.
3. **Preserve meaning.** Keep the core message intact.
4. **Match the voice.** Fit the intended tone (formal, casual, technical). Add personality only when the content calls for it (see Voice and Personality below).


## Voice calibration (optional)

If the user provides a writing sample, analyze it before rewriting:

1. **Read the sample first.** Note sentence length patterns, word choice level, paragraph openers, punctuation habits, recurring phrases, transition style.
2. **Match their voice in the rewrite.** If they write short sentences, don't produce long ones. If they use "stuff" and "things," don't upgrade to "elements" and "components."
3. **When no sample is provided,** fall back to natural, varied, opinionated voice from the personality section below.


## Voice and personality

Avoiding AI patterns is half the job. Sterile, voiceless writing is just as obvious. Good writing has a human behind it.

**Apply personality only when the content calls for it:** blog posts, essays, opinion, personal writing. For encyclopedic, technical, legal, or reference text, neutral and plain *is* the correct voice. Don't inject opinions or first person there.

Signs of soulless writing (even if technically clean):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality

How to add voice:
- **Have opinions.** "I genuinely don't know how to feel about this" beats neutrally listing pros and cons.
- **Vary rhythm.** Short punchy sentences. Then longer ones that take their time. Mix it up.
- **Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, half-formed thoughts are human.


## Core rules

### 1. Cut filler phrases
Remove throat-clearing openers, emphasis crutches, and adverbs. See [references/phrases.md](references/phrases.md).

### 2. Break formulaic structures
Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See [references/structures.md](references/structures.md).

### 3. Use active voice
Every sentence needs a subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix"). Name the person. If no person fits, use "you."

### 4. Be specific
No vague declaratives ("The reasons are structural"). Name the specific thing. No lazy extremes ("every," "always," "never") doing vague work.

### 5. Put the reader in the room
No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.

### 6. Vary rhythm
Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes or en dashes anywhere.

### 7. Trust readers
State facts directly. Skip softening, justification, hand-holding.

### 8. Cut quotables
If it sounds like a pull-quote, rewrite it. Aphorisms like "X is the Y of Z" or "X becomes a trap" are formula, not insight.

### 9. Kill promotional language
No "vibrant," "groundbreaking," "nestled," "breathtaking," "renowned," "stunning." No puffing up significance with "testament," "pivotal moment," "enduring legacy." See [references/ai-vocabulary.md](references/ai-vocabulary.md).

### 10. Attribute specifically
No "experts argue," "industry reports suggest," "observers note." Name the source, the year, the publication. If you can't, cut the claim.

### 11. No chatbot artifacts
No "I hope this helps," "Let me know if you'd like me to expand," "Great question!" No knowledge-cutoff disclaimers. No sycophantic filler. See [references/phrases.md](references/phrases.md).

### 12. No manufactured drama
No staccato fragment runs. No "Then X arrived. The old rules were gone." No aphorism formulas. One short sentence for emphasis is fine; a run of them is engineered. See [references/structures.md](references/structures.md).


## Quick checks

Before delivering prose:

- Any adverbs? Kill them.
- Any passive voice? Find the actor, make them the subject.
- Inanimate thing doing a human verb ("the decision emerges")? Name the person.
- Sentence starts with a Wh- word? Restructure it.
- Any "here's what/this/that" throat-clearing? Cut to the point.
- Any "not X, it's Y" contrasts? State Y directly.
- Three consecutive sentences match length? Break one.
- Paragraph ends with punchy one-liner? Vary it.
- Em dash or en dash anywhere? Remove it. Use commas, periods, colons, or parentheses.
- Vague declarative ("The implications are significant")? Name the specific implication.
- Narrator-from-a-distance ("Nobody designed this")? Put the reader in the scene.
- Meta-joiners ("The rest of this essay...")? Delete.
- Rule of three ("X, Y, and Z")? Cut to two, or use one with detail.
- Bolded inline headers in a list? Convert to prose.
- Title case in headings? Use sentence case.
- Emojis decorating headers or bullets? Remove.
- Curly quotes? Straighten them.
- "Serves as" / "stands as" / "boasts"? Replace with "is" or "has."
- Signposting ("Let's dive in," "Here's what you need to know")? Delete and start with the content.
- Fragmented header (heading followed by a one-liner restating it)? Delete the one-liner.
- Hyphenated compound after a noun ("the report is high-quality")? Drop the hyphen.


## Bahasa Indonesia

Full Indonesian support. See [references/bahasa-indonesia.md](references/bahasa-indonesia.md) for the complete reference.

When humanizing Indonesian text:

1. **Use the Indonesian word lists.** The English banned phrases don't apply. Use the Indonesian equivalents in bahasa-indonesia.md: frasa pembuka basa-basi, kosakata AI, inflasi signifikansi, bahasa promosi.
2. **Respect register.** Indonesian formal writing (akademis, hukum, jurnalistik) has conventions that are not slop. "Berdasarkan penelitian" in a skripsi is fine. "Dalam era digital saat ini" in a blog post is AI filler.
3. **Handle pasif with judgment.** Awalan di- dan ter- sah dalam ragam formal. Ganti ke aktif hanya kalau pelakunya diketahui dan relevan.
4. **Cut the same structural tells.** Aturan tiga, pola "Tidak hanya... tetapi juga...", paragraf "Tantangan dan Peluang", dan kesimpulan generik sama jeleknya di Bahasa Indonesia.
5. **Be specific with numbers.** Ganti "signifikan" dengan angka. Ganti "berbagai daerah" dengan nama daerah. Ganti "para ahli" dengan nama orang.

Indonesian quick checks:
- "Dalam era/konteks/hal ini" di awal? Hapus.
- "Signifikan," "komprehensif," "esensial," "optimal"? Ganti kata biasa.
- Pasif bertumpuk (di-... di-... di-...)? Cari pelaku, pakai aktif.
- "Menurut para ahli"? Sebut namanya.
- "Semoga bermanfaat"? Hapus.
- Paragraf penutup "Dengan demikian, dapat disimpulkan..."? Hapus atau ganti fakta.


## Non-English writing (other languages)

For languages other than English and Indonesian, adapt the checks to the target language:

- **Translate the principle, not the English phrase.** Identify equivalent filler in the target language.
- **Respect language-specific conventions.** Some languages use passive voice naturally in formal writing. Apply the active-voice rule with judgment.
- **Academic prose is not slop.** Standard scholarly conventions are fine. Cut filler that adds no meaning, not conventions the audience expects.
- **Don't over-simplify formal documents.** Legal, academic, and policy documents need their register.


## Detection guidance

### What NOT to flag (false positives)

A clean human writer can hit several patterns without AI involvement. Before rewriting, check that you are not gutting legitimate prose:

- **Perfect grammar.** Many writers are professionals. Polish does not equal AI.
- **Mixed registers.** Often signals a technical person or someone with an unusual voice.
- **Formal vocabulary.** AI overuses *specific* fancy words (see ai-vocabulary.md), not all fancy words. Don't flatten "ostensibly" or "constituent."
- **Single em dash.** Many editors use them. The tell is em dashes plus formulaic rhythm plus AI vocabulary.
- **One short emphatic sentence.** The tell is several in a row that inflate the tone.
- **"Honestly" or "look" mid-sentence.** Ordinary in casual writing. The tell is the standalone theatrical opener.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations proves nothing.
- **Common transition words in isolation.** One "however" is not a tell. Five "additionally"s in a page is.

Look for **clusters** of tells, not isolated ones. A single em dash means nothing. Em dashes plus rule-of-three plus "vibrant tapestry" plus a "Conclusion" section is a confession.

### Signs of human writing (preserve these)

- **Specific, unusual detail.** A real address. A weird quote. LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me." LLMs default to clean takes.
- **Dated references.** Slang, memes, in-jokes that map to a specific year.
- **First-person editorial choices.** If the writer can explain *why* they used a particular word, that's human.
- **Genuine asides and self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.


## Process and output

1. Read the input carefully. Identify every instance of the patterns above and in the reference files.
2. Write a **draft rewrite**. Check that it reads naturally aloud, varies sentence length, prefers specific details and simple constructions (is/are/has), and keeps the appropriate register.
3. Run the quick checks. Ask: "What makes this still obviously AI generated?" Answer briefly with any remaining tells.
4. Revise into a **final rewrite** that addresses them.
5. Scan the final for `—` and `–`. Any hit means the draft isn't done.

Deliver the draft, the brief "still-AI" bullets, the final rewrite, and a short summary of changes.


## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |
| Specificity | Concrete or vague? |
| Voice | Person behind it or committee output? |

Below 50/70: revise.


## References

- [references/phrases.md](references/phrases.md) - phrases to remove (English)
- [references/structures.md](references/structures.md) - structural patterns to avoid
- [references/ai-vocabulary.md](references/ai-vocabulary.md) - overused AI words and style tells
- [references/examples.md](references/examples.md) - before/after transformations
- [references/bahasa-indonesia.md](references/bahasa-indonesia.md) - pola AI dalam Bahasa Indonesia

Based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.

## License

MIT
