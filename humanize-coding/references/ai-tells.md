# AI Code Tells

Patterns that instantly flag AI-generated code. Avoid all of these.

---

## Comment Tells

| Tell | Why It's AI |
|------|-------------|
| `# Initialize the variable` | States the obvious |
| `// Step 1: Validate input` | Tutorial numbering |
| `/* This function calculates... */` | Docstring for a 3-line function |
| `# TODO: Add error handling` | Promised but never done |
| Comment on every block | No real dev does this |
| Comment-to-code ratio above 30% | You wrote an essay, not code |

---

## Naming Tells

| Tell | Fix |
|------|-----|
| `userDataObject` | `user` |
| `processedResultData` | `result` |
| `handleClickEvent` | `onClick` or just the action |
| `calculateTotalPriceWithTax` | `priceWithTax` or `totalPrice` |
| `isUserAuthenticated` | `authenticated` or `loggedIn` |
| `errorMessage` | `err` |
| `index` in a for loop | `i` |
| `iterator` | `i`, `j`, `k` |
| `item` in every loop | name the domain thing: `user`, `order`, `line` |
| `data` as a variable name | name what the data IS |
| `value` | same — name the thing |
| `result` when something more specific fits | be specific |
| `flag` | name the condition: `found`, `done`, `ready` |
| `temp` | name what it holds, even briefly |

---

## Structure Tells

| Tell | Fix |
|------|-----|
| Every function exactly the same length | Let functions be the length they need to be |
| Every file has Imports / Constants / Helpers / Main sections | Organic structure |
| Abstract base class with one subclass | Just write the class |
| Factory for one thing | Just instantiate it |
| Interface with one implementation | Skip the interface until you need it |
| Strategy pattern for 2 conditions | Use an if/else or a dict |
| Every method wrapped in try/catch | Handle errors where they matter |
| `main()` calls exactly 4 functions | Don't architect for symmetry |
| Constants file with 40 string constants | Inline the obvious ones |

---

## Language-Specific Tells

### Python
- `for i in range(len(arr)):` instead of `for item in arr:`
- `if x == True:` instead of `if x:`
- String formatting with `%s` or `.format()` when f-strings exist
- Manual class with `__init__` for simple data → use dataclass
- `except Exception as e: pass` — swallowed errors

### JavaScript/TypeScript
- `var` in 2024
- `function` keyword for callbacks that should be arrows
- `if (obj !== null && obj !== undefined)` instead of `obj?.`
- `.then().catch()` chains when `async/await` fits better
- `console.log("error:", error)` as error handling

### Go
- Java-style class hierarchies
- `err != nil` check missing after anything that returns an error
- `interface{}` when the type is known
- Goroutine with no sync mechanism

### Rust
- `.unwrap()` everywhere in non-test code
- `for i in 0..vec.len()` instead of `.iter()`
- Match arms that could be `.map()` or `.filter()`

---

## Tone Tells

Code that reads like it was written for a tutorial:
- Overly clear variable names that sacrifice idiom for readability
- Consistent spacing that's too consistent
- No line ever breaking convention even once
- Zero use of abbreviations that the community has standardized

Real code has texture. It was written over time, by someone who knew the domain.
