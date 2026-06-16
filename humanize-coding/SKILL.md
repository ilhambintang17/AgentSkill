---
name: humanize-coding
description: Write code that looks like it was written by a real developer, not an AI. Eliminates AI code tells across all programming languages — no over-commenting, no robotic naming, no textbook structure. Use whenever writing, refactoring, or reviewing code.
metadata:
  trigger: Writing code, refactoring, code review, generating functions/classes/scripts in any language
  author: custom
---

# Humanize Coding

Make code read like a real developer wrote it at 2am, in the zone, knowing what they're doing.

---

## The Problem With AI Code

AI code has a signature. Reviewers, interviewers, and senior devs spot it instantly:

- Every block has a comment explaining what `i++` does
- Variables named `processedDataResult` and `handleUserInputEvent`
- Perfect symmetry: every function exactly 10 lines, every file exactly 3 sections
- Textbook patterns used even when they don't fit
- Comments that just restate the code in English
- Overly defensive checks for things that can't happen
- Zero personality, zero shortcuts, zero "I know what I'm doing" energy

See [references/ai-tells.md](references/ai-tells.md) for full pattern list.

---

## Core Rules

### 1. Comments only when the code can't explain itself

Real devs comment the *why*, never the *what*. If the code is readable, no comment.

Bad:
```python
# increment counter
count += 1

# check if user is authenticated
if user.token:
```

Good:
```python
count += 1

if user.token:
```

Comment only for:
- Non-obvious business logic ("billing resets on the 1st, not midnight")
- Workarounds ("this breaks on Safari 15, hence the timeout")
- Mathematical formulas that need a reference
- TODOs that are actually going to happen

### 2. Name things like a human who's been in this codebase for 6 months

Real devs use short names for short-lived things. They use domain language. They abbreviate when everyone on the team knows what it means.

Bad AI names:
- `userDataObject`, `processedResult`, `handleClickEvent`
- `calculateTotalPriceWithTax`, `getUserAuthenticationStatus`
- `temp1`, `temp2` (pure laziness, also bad)

Good human names:
- `user`, `result`, `onClick`
- `total`, `authStatus`, `invoice`
- `i`, `j`, `k` for loop counters — always
- `err`, `e` for errors — always
- `req`, `res`, `ctx` for web handlers — always
- `cfg`, `opts`, `args` for config/options — common

See [references/naming.md](references/naming.md) for language-specific conventions.

### 3. Break structure when it makes sense to

Real code isn't perfectly uniform. A function that needs 30 lines gets 30 lines. A one-liner stays a one-liner.

Bad:
```js
// Overly decomposed for no reason
function getUserName(user) {
  const name = extractName(user);
  const formattedName = formatName(name);
  return formattedName;
}
```

Good:
```js
function getUserName(u) {
  return u.firstName + ' ' + u.lastName
}
```

Or even:
```js
const getName = u => `${u.firstName} ${u.lastName}`
```

### 4. Use idioms for the language

AI writes generic code that could almost be in any language. Real devs use the native patterns.

Python: use list comprehensions, `enumerate`, `zip`, walrus operator where it fits — not `for i in range(len(arr))`

JS/TS: destructure, optional chaining, nullish coalescing — not `if (obj && obj.prop && obj.prop.val)`

Go: idiomatic error handling, table-driven tests — not try/catch patterns ported from Java

Rust: match arms, iterators, `?` operator — not nested if/else

See [references/idioms.md](references/idioms.md).

### 5. Show awareness without showing off

Real devs don't use design patterns to prove they know them. They use the simplest thing that works. They reach for a pattern when the problem actually needs it.

Skip the factory pattern for a thing that gets created once. Skip the strategy pattern for two code paths. Don't make an abstract base class for one subclass.

But also: don't reinvent what stdlib already has. Real devs know their stdlib.

### 6. Inconsistency is human

Perfect codebases don't exist. Slightly varied spacing, one function in a slightly different style, a variable named differently because it was added later — these are fine. Don't enforce artificial uniformity to "clean up."

Unless the user asked for a refactor with consistent style, leave minor style variations alone.

### 7. Error handling like someone who's been burned before

AI adds `try/catch` everywhere and logs "An error occurred." Real devs handle the errors they've actually seen in production.

Bad:
```python
try:
    result = process(data)
except Exception as e:
    print(f"An error occurred: {e}")
```

Good:
```python
try:
    result = process(data)
except ValueError:
    return None
except requests.Timeout:
    raise RetryableError("upstream timed out")
```

---

## Quick Checks Before Outputting Code

- Any comment that just restates the code? Delete it.
- Any variable over 3 words long? Shorten it.
- Loop counter named `index` or `iterator`? Change to `i`.
- Error variable named `error` or `exception`? Change to `err` or `e`.
- Function named `handleXxxEvent` or `processXxxData`? Strip the redundant wrapper words.
- Every function the same length? Break one intentionally.
- Pattern used for no reason (singleton, factory, observer)? Remove it.
- Comment says `// Step 1:`, `// Step 2:`? This isn't a tutorial. Delete.
- Generic `catch (Exception e)` with a log? Replace with specific handling.
- Five-word function name that could be two? Rewrite it.
- Code could be a one-liner idiom in this language? Use it.

---

## Language Checklist

Run the relevant checklist before outputting. See [references/idioms.md](references/idioms.md) for full details.

**Python** — list comp over explicit loops, `_` for unused, f-strings not `.format()`, no `pass` blocks unless needed  
**JavaScript/TypeScript** — destructure everything, arrow functions for callbacks, `??` and `?.`, no `var`  
**Go** — short var decl `:=`, named returns only when they help, `fmt.Errorf` with `%w`, no OOP shoehorning  
**Rust** — iterators over manual loops, `?` instead of `unwrap`, match over if-chains on enums  
**Java/Kotlin** — Kotlin: data classes, `let`/`apply`/`also`, no null-checks when `?.` works  
**C/C++** — meaningful pointer names, `nullptr` not `NULL` in C++, RAII  
**Shell/Bash** — `[[ ]]` over `[ ]`, quote variables, `set -euo pipefail`  
**SQL** — CTEs for readability, no `SELECT *` in production queries  

---

## Scoring

Rate 1-10 per dimension:

| Dimension | Question |
|-----------|----------|
| Naming | Short, domain-appropriate, idiomatic? |
| Comments | Only where the code can't explain itself? |
| Idioms | Uses native language patterns? |
| Structure | Fits the problem, not a template? |
| Authenticity | Would a senior dev write this without blinking? |

Below 40/50: revise before outputting.

---

## License

MIT
