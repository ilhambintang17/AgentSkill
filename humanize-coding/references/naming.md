# Naming Conventions by Language

Human naming patterns that real devs actually use.

---

## Universal Rules

- Loop counters: `i`, `j`, `k` — always, no exceptions for simple loops
- Error variables: `err` (Go, JS, Python), `e` (Java, C#, Python except handler), `ex` (rare)
- Accumulator: `total`, `sum`, `acc`
- Temporary/swap: name what it holds, even if briefly — `prev`, `tmp` only if nothing better fits
- Boolean: short state word — `done`, `found`, `ok`, `ready`, `valid`, `open`, `active`
- Config/options: `cfg`, `opts`, `conf`, `config`
- Context: `ctx`
- Request/response: `req`/`res` or `r`/`w` (Go)
- Database connection: `db`
- Logger: `log`, `logger`
- Channel (Go): noun + `Ch` — `doneCh`, `errCh`

---

## Python

```python
# Loop vars
for i, item in enumerate(orders):
for k, v in d.items():

# Common abbreviations the community uses
cfg = load_config()
df = pd.DataFrame(...)       # dataframes are always df
arr = np.array(...)
fn = lambda x: x * 2        # for short callbacks
cls = MyClass                # metaclass convention

# Underscore conventions
_ = unused_value             # throwaway
__private = "internal"       # name mangling
_protected = "internal"      # single underscore = "don't touch"

# Don't do this
userDataObjectList = []      # camelCase in Python is wrong
process_user_data_and_return_result = lambda x: x  # too long
```

---

## JavaScript / TypeScript

```js
// Loop vars
for (let i = 0; i < arr.length; i++)
arr.forEach((item, i) => ...)

// Common short names
const el = document.getElementById('app')
const btn = document.querySelector('button')
const cb = () => {}          // callbacks
const fn = x => x * 2

// Event handlers
onClick, onChange, onSubmit  // NOT handleClickEvent
onClose, onOpen

// React specific
const [count, setCount] = useState(0)  // NOT countState
const ref = useRef(null)               // NOT myRef
const ctx = useContext(AppContext)

// Async
const res = await fetch(url)
const data = await res.json()
const { token, user } = data

// TypeScript
type User = { id: string; name: string }  // not UserType or IUser (unless codebase uses I prefix)
```

---

## Go

```go
// Go has strong conventions, follow them exactly

// Receivers: one or two letter abbreviation of the type
func (u *User) Name() string { ... }
func (s *Server) Handle(w http.ResponseWriter, r *http.Request) { ... }

// Error: always err
val, err := doThing()
if err != nil { ... }

// Context: always ctx
func process(ctx context.Context, ...) { ... }

// Writer/Reader interfaces
func Write(w io.Writer, ...) { ... }

// Channels: descriptive + Ch suffix
doneCh := make(chan struct{})
errCh  := make(chan error, 1)

// Common short names Go devs actually use
db    // database connection
cfg   // config
mu    // mutex (sync.Mutex)
wg    // WaitGroup
tx    // database transaction
stmt  // prepared statement
buf   // bytes.Buffer or bufio
sc    // bufio.Scanner
enc   // encoder
dec   // decoder
```

---

## Rust

```rust
// Rust follows snake_case like Python

// Common short names
let n = items.len();
let mut v: Vec<_> = ...;
let mut s = String::new();
let (tx, rx) = channel();   // sender/receiver always tx/rx

// Error handling
fn parse(s: &str) -> Result<u64, ParseError> {
    let n = s.trim().parse::<u64>()?;
    Ok(n)
}

// Closures
items.iter().filter(|x| x.active).map(|x| x.id)
// x is fine for short closures — don't write |item| when |x| reads fine

// Lifetimes
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str  // 'a is standard
```

---

## Java / Kotlin

```kotlin
// Kotlin — modern idioms

// Data
data class User(val id: String, val name: String)

// No getter/setter boilerplate
val name = user.name  // not user.getName()

// Scope functions
val result = db.query(sql).also { log.debug("ran query") }
val user = User(id).apply { name = "Bob" }

// Short names are fine in Kotlin too
val n = list.size
list.forEachIndexed { i, item -> ... }

// Java legacy — acceptable shorts
List<String> names = new ArrayList<>();
Map<String, Integer> counts = new HashMap<>();
Iterator<String> it = names.iterator();
```

---

## Shell / Bash

```bash
# Local vars: lowercase snake_case
local input_file="$1"
local output_dir="$2"

# Environment/exports: UPPERCASE
export APP_ENV="production"
readonly MAX_RETRIES=3

# Loop vars
for f in *.log; do ...
for i in "${arr[@]}"; do ...

# Common shorts
ret=$?          # return code
pid=$!          # background PID
dir=$(dirname "$0")
```

---

## SQL

```sql
-- Table aliases: 2-3 letter meaningful abbreviation
SELECT u.name, o.total
FROM users u
JOIN orders o ON o.user_id = u.id

-- CTE names: readable noun phrases, no underscores needed for short ones
WITH active_users AS (
    SELECT * FROM users WHERE active = true
),
recent_orders AS (
    SELECT * FROM orders WHERE created_at > now() - interval '30 days'
)

-- Column aliases
SELECT count(*) AS total, avg(price) AS avg_price
```
