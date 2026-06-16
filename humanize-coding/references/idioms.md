# Language Idioms

Patterns real devs reach for. Use these, not the generic equivalent.

---

## Python

```python
# List comprehension, not explicit loop
squares = [x**2 for x in range(10)]
# NOT:
squares = []
for x in range(10):
    squares.append(x**2)

# Enumerate when you need index
for i, item in enumerate(items):
# NOT: for i in range(len(items)):

# Zip for parallel iteration
for a, b in zip(left, right):

# Dict comprehension
counts = {k: len(v) for k, v in groups.items()}

# Walrus operator for read-once values
if m := pattern.match(line):
    process(m.group(1))

# Unpacking
first, *rest = items
a, b = b, a  # swap

# f-strings, always
msg = f"user {user.id} failed"
# NOT: "user %s failed" % user.id
# NOT: "user {} failed".format(user.id)

# Truthiness, not explicit comparison
if items:        # not if len(items) > 0
if not items:    # not if len(items) == 0
if x is None:    # for None checks — never if x == None

# Context managers
with open(f) as fh:
    data = fh.read()

# Defaultdict / Counter instead of manual init
from collections import defaultdict, Counter
counts = Counter(words)

# Dataclass for simple data containers
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

---

## JavaScript / TypeScript

```js
// Destructuring — always
const { id, name } = user
const [head, ...tail] = arr
const { data: { token } } = response  // rename on destructure

// Optional chaining
const city = user?.address?.city
const first = arr?.[0]

// Nullish coalescing
const label = user.name ?? 'Anonymous'
const port = opts.port ?? 3000

// Spread
const merged = { ...defaults, ...overrides }
const copy = [...arr, newItem]

// Array methods over loops
const ids = users.map(u => u.id)
const active = users.filter(u => u.active)
const total = orders.reduce((sum, o) => sum + o.price, 0)
const found = users.find(u => u.id === targetId)

// Arrow functions for callbacks
setTimeout(() => cleanup(), 1000)
arr.forEach((item, i) => process(item, i))

// Template literals
const url = `${base}/api/users/${id}`

// async/await, not .then chains (unless chaining intentionally)
const data = await fetchUser(id)

// Short-circuit for defaults/guards
const name = input || 'default'
user.admin && sendAlert(user)

// Object shorthand
const obj = { id, name, active }  // not { id: id, name: name }

// TypeScript: infer types, don't over-annotate
const ids = users.map(u => u.id)  // type inferred
// Only annotate when inference fails or public API
```

---

## Go

```go
// Short variable declarations always
x := compute()
user, err := db.GetUser(id)

// Multiple return + immediate error check
n, err := w.Write(data)
if err != nil {
    return fmt.Errorf("write failed: %w", err)
}

// Defer for cleanup
f, err := os.Open(path)
if err != nil { return err }
defer f.Close()

// Slices
items := make([]string, 0, 10)  // with capacity hint when known
items = append(items, "a", "b")

// Map literal
scores := map[string]int{
    "alice": 10,
    "bob":   8,
}

// Struct literal with field names
u := User{
    ID:   id,
    Name: "bob",
}

// Interface satisfaction at compile time
var _ http.Handler = (*MyServer)(nil)

// goroutine + channel pattern
ch := make(chan Result, 1)
go func() {
    ch <- compute()
}()
result := <-ch

// Select with timeout
select {
case res := <-ch:
    return res, nil
case <-time.After(5 * time.Second):
    return nil, ErrTimeout
}

// String builder for concatenation in loops
var b strings.Builder
for _, s := range parts {
    b.WriteString(s)
}
return b.String()
```

---

## Rust

```rust
// Iterator chains instead of loops
let total: u32 = orders.iter().map(|o| o.price).sum();
let active: Vec<_> = users.iter().filter(|u| u.active).collect();

// ? operator for error propagation
fn read_config(path: &str) -> Result<Config, io::Error> {
    let contents = fs::read_to_string(path)?;
    let cfg = serde_json::from_str(&contents)?;
    Ok(cfg)
}

// Pattern matching
match status {
    Status::Ok(data) => process(data),
    Status::NotFound => return Err(AppError::Missing),
    Status::Error(e) => return Err(e.into()),
}

// if let for single pattern
if let Some(user) = cache.get(&id) {
    return Ok(user.clone());
}

// while let for consuming iterators
while let Some(item) = queue.pop_front() {
    handle(item);
}

// String handling
let s = format!("{}/{}", base, path);
let trimmed = input.trim().to_lowercase();

// Closures
let doubled: Vec<_> = nums.iter().map(|&x| x * 2).collect();

// Entry API for maps
counts.entry(key).or_insert(0) += 1;

// Struct update syntax
let updated = User { name: new_name, ..user };
```

---

## Bash

```bash
#!/usr/bin/env bash
set -euo pipefail

# [[ ]] not [ ]
if [[ "$1" == "--verbose" ]]; then

# String checks
if [[ -z "$var" ]]; then   # empty
if [[ -n "$var" ]]; then   # non-empty
if [[ -f "$path" ]]; then  # file exists

# Command substitution with $()
dir=$(dirname "$0")
now=$(date +%Y%m%d)

# Arrays
files=("a.txt" "b.txt")
for f in "${files[@]}"; do

# Here-doc
cat <<EOF
line one
line two
EOF

# Default values
port=${PORT:-8080}
env=${APP_ENV:-development}

# Functions
die() { echo "error: $*" >&2; exit 1; }
```

---

## SQL

```sql
-- CTEs for readable multi-step queries
WITH monthly AS (
    SELECT
        date_trunc('month', created_at) AS month,
        sum(amount) AS revenue
    FROM orders
    WHERE created_at >= now() - interval '1 year'
    GROUP BY 1
)
SELECT month, revenue,
       revenue - lag(revenue) OVER (ORDER BY month) AS delta
FROM monthly
ORDER BY month;

-- Window functions over subqueries
SELECT
    id,
    name,
    rank() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank
FROM employees;

-- Explicit JOIN types, no implicit comma joins
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON o.user_id = u.id
LEFT  JOIN payments p ON p.order_id = o.id;

-- RETURNING for insert/update results
INSERT INTO sessions (user_id, token)
VALUES ($1, $2)
RETURNING id, created_at;
```
