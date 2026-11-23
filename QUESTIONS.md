# Exercise Questions

This file records the exercise prompts shared for T01 through T13.

## T01: Lists and strings

### T01-E01: Lists: max, min, sum, sorting and stepping

Given `numbers = [14, 3, 9, 27, 8, 21, 5, 18]`, implement
`list_stats(nums)` returning a dictionary with `max`, `min`, `total`,
`average`, `descending` (a new descending-sorted list), and `every_second`
(items at indices 0, 2, 4, ...). Do not mutate the input. Print:

```text
max: 27
min: 3
total: 105
average: 13.12
descending: [27, 21, 18, 14, 9, 8, 5, 3]
every second: [14, 9, 8, 5]
```

### T01-E02: Cleaning names with string methods

Implement `clean_name(raw)` to trim and collapse whitespace and convert to
title case. Implement `initials(name)` to return dotted initials, including
the final dot. For each sample name, print the cleaned name using `repr` and
its initials:

```text
'Anna Maria Smith' -> A.M.S.
"O'Brien John" -> O.J.
'Mary-Jane Watson' -> M.W.
'Li Wei' -> L.W.
```

Sample names: `"  aNNa   maRIA  smith "`, `"o'brien   john"`,
`"MARY-JANE watson"`, and `"li   wei"`.

## T02: Loops and conditions

### T02-E01: FizzBuzz

Read an integer `n` from standard input with no prompt. Implement
`fizzbuzz(n)` returning strings for 1 through `n`: `Fizz` for multiples of 3,
`Buzz` for multiples of 5, `FizzBuzz` for both, and the number otherwise.
Print one result per line. For input `15`, the output ends with:

```text
13
14
FizzBuzz
```

`fizzbuzz(0)` should return an empty list.

### T02-E02: Grade calculator

Read scores separated by spaces. Implement `grade(score)` with A for 90+,
B for 80–89, C for 70–79, D for 60–69, and F below 60. A valid token is a
whole number from 0 to 100. Print `<token>: invalid` for invalid tokens,
exclude them from the average, and print the average of valid scores to one
decimal place, or `No valid scores` when none are valid.

For input `95 82 67 45 100 -5 abc 73`, expected output is:

```text
95: A
82: B
67: D
45: F
100: A
-5: invalid
abc: invalid
73: C
Average of valid scores: 77.0
```

## T03: Text files

### T03-E01: Read a text file and count

Read `data/notes.txt` using a `with` statement and UTF-8 encoding. Print the
first five lines numbered with a right-aligned width of 3. Implement
`file_stats(path)` returning counts of lines, words, characters (excluding
line endings), and blank/whitespace-only lines. For the supplied sample:

```text
Lines: 25
Words: 150
Characters: 872
Blank lines: 1
```

### T03-E02: Write a text file

Implement `write_squares(path, n)` to create parent directories as needed,
write one `<i> squared is <i*i>` line for each `i` from 1 through `n`, and
return `n`. Write 8 lines to `output/squares.txt`, print the number written,
then print the file contents. Running it repeatedly must replace, not append
to, the output file.

```text
Lines written: 8
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
6 squared is 36
7 squared is 49
8 squared is 64
```

## T04: Exceptions and parsing

### T04-E01: Safe division

Read standard input until EOF, skipping blank lines. Implement
`divide_line(line)` for exactly two numbers separated by whitespace. Format
numbers with `:g`; return `Cannot divide by zero` for a zero divisor and
`Invalid input: expected two numbers` for invalid input. Use specific
exception handlers and an `else` clause, not a bare `except`.

For input lines `10 2`, `7 0`, `x 3`, `5`, `7 2`, and `1 2 3`, the output is:

```text
10 / 2 = 5
Cannot divide by zero
Invalid input: expected two numbers
Invalid input: expected two numbers
7 / 2 = 3.5
Invalid input: expected two numbers
```

### T04-E02: Parse sensor readings

Read `data/readings.txt`. Implement `parse_readings(lines)` returning
`(values, bad)`, where `values` contains floats and `bad` contains
`(line_number, stripped_text)` for non-numeric lines. Print total and valid
line counts, invalid line numbers and their text using `repr`, the average
to two decimals, and the minimum and maximum. Expected sample summary:

```text
Lines: 30
Valid: 26
Invalid lines: [4, 7, 17, 23]
  line 4: 'N/A'
  line 7: 'abc'
  line 17: 'error'
  line 23: ''
Average: 26.99
Min: 21.5  Max: 120.5
```

## T05: JSON

### T05-E01: JSON basics: dumps and loads

Use `json.dumps` and `json.loads` with the supplied dictionary containing a
name, age, boolean, tuple of scores, `None` nickname, and height. Print compact
JSON; print indented, sorted-key JSON; implement `roundtrip(obj)` and show
the type change from tuple to list, the boolean and `None` values, and whether
the result equals the original. Also show that integer dictionary keys become
strings and catch the `TypeError` from attempting to serialize a set.

The sample should establish that the tuple round trip is not equal and that
the set error is `TypeError: Object of type set is not JSON serializable`.

### T05-E02: Read a config file

Load `data/config.json`. Implement `get_nested(data, path, default=None)` to
follow dotted dictionary paths and return the default if a step is missing
or is not a dictionary. Preserve real false/zero values. Print each requested
path and its `repr` value, then print the administrators and their count.

Expected lookups include `app.name = 'TrainingPortal'`,
`server.port = 8080`, `features.beta_dashboard = False`,
`cache.ttl = 60` (default), and `server.host.name = 'n/a'` (default).
The sample config uses local/reserved test hostnames and finishes with
`admins: asha, ben (2)`.

## T06: Regular expressions

### T06-E01: match, search and fullmatch

Using `re`, implement `starts_with_number(text)` with `re.match`,
`first_number(text)` with `re.search` returning an integer or `None`, and
`is_whole_number(text)` with `re.fullmatch`. Print each sample string using
`repr` left-aligned in width 12, followed by the match, search, and fullmatch
results. Samples: `"42 apples"`, `"apples 42"`, `"42"`, `"forty-two"`, and
`""`. Empty text is not a whole number.

### T06-E02: findall for numbers, tags and pairs

Implement `extract_numbers(text)` for integer and decimal numbers (optional
minus sign), `extract_hashtags(text)` for hashtags containing word
characters, and `extract_pairs(text)` for `key=value` pairs as tuples. Print
the matches, the numeric sum to two decimals, and the pairs as a dictionary.
The supplied sample should produce:

```text
numbers: ['1042', '14', '3', '59.97', '-5.5']
sum: 1113.47
hashtags: ['#sale', '#newArrival', '#eco_friendly']
pairs: [('mode', 'fast'), ('retries', '3'), ('name', 'Zed'), ('level', '7')]
as dict: {'mode': 'fast', 'retries': '3', 'name': 'Zed', 'level': '7'}
```

## T07: Classes

### T07-E01: Book with progress tracking

Create `Book(title, author, pages)` with `current_page` initially zero.
`describe()` returns `'<title>' by <author> (<pages> pages)`. `read(count)`
advances the page without going past the last page, and `progress()` returns
the percentage read rounded to one decimal place.

For `Book("Dune", "Frank Herbert", 412)`, the sample should describe Dune,
start at `0.0`, reach `103` pages and `25.0%`, then stop at `412` pages and
`100.0%` after an oversized read.

### T07-E02: Bank account with validation

Create `InsufficientFundsError` as a `ValueError` subclass and
`BankAccount(owner, balance=0)`. Deposits and withdrawals must be positive;
reject invalid amounts with the specified `ValueError` messages and reject
overdrafts with `InsufficientFundsError`. Successful operations are appended
to `history` as `(kind, amount)` tuples. `statement()` lists the owner,
aligned history entries, and ending balance. Failed operations must not alter
state.

## T08: Functions and closures

### T08-E01: Functions as objects

Implement `add`, `sub`, and `mul`, and an `OPERATIONS` dictionary that maps
their names to the functions. `calculate(op_name, a, b)` dispatches through
that dictionary and raises `ValueError("Unknown operation: <name>")` for
unknown names. Also implement `apply_twice(func, value)` and `compose(f, g)`,
where the composed function returns `f(g(x))`.

The sample checks arithmetic, higher-order functions, function attributes,
the operation keys, and the unknown-operation error.

### T08-E02: Closures: counters and multipliers

Implement `make_counter(start=0, step=1)` as an independent stateful closure,
`make_multiplier(n)`, and `build_multipliers(factors)`. The sample counters
produce `0 1 2` and `10 15`; multipliers for `[2, 3, 4]` applied to 10 produce
`[20, 30, 40]`. Explain why lambdas created in a loop that capture the same
loop variable all use its final value.

## T09: Recursion

### T09-E01: Factorial, countdown and list sum

Implement recursive `factorial(n)`, `countdown(n)`, and `sum_list(numbers)`.
Factorial uses `0! = 1! = 1` and raises
`ValueError("n must be non-negative")` for negative input. Countdown returns
`[n, ..., 1]` or an empty list for non-positive input. Sum the list recursively
without using `sum()` or loops.

### T09-E02: Digits, reversing and palindromes

Implement recursive `sum_of_digits(n)` (ignoring the sign),
`reverse_string(text)` (without reverse slicing or `reversed()`), and
`is_palindrome(text)`. Palindrome comparison is recursive and ignores case
and non-alphanumeric characters; the empty string is a palindrome.

## T10: Design patterns

### T10-E01: Singleton application configuration

Write a `singleton(cls)` class decorator that returns the same instance on
every construction, ignoring later constructor arguments. Add a `reset()`
function attribute that clears the stored instance. Decorate `AppConfig`,
whose constructor stores `env` and an empty `values` dictionary; provide
`set(key, value)` and `get(key, default=None)`.

The sample verifies shared identity and state, reset behavior, and the
decorated class name. Note the trade-off that the decorated name is a function,
so `isinstance(value, AppConfig)` does not work.

## T11: Stacks and queues

### T11-E01: Stack and balanced brackets

Implement a list-backed LIFO `Stack` with `push`, `pop`, `peek`, `is_empty`,
and `__len__`. `pop` and `peek` raise `IndexError` when empty. Use the stack
in `is_balanced(text)` to validate matching `()`, `[]`, and `{}` in the right
order while ignoring other characters.

### T11-E02: Queue from two stacks

Implement a FIFO `Queue` using two Python lists as stacks, with `enqueue`,
`dequeue`, `front`, `is_empty`, and `__len__`. Empty `dequeue` and `front`
raise `IndexError`. Implement `process_jobs(jobs)` to return jobs in queue
order. Do not use `list.pop(0)` or `collections.deque`.

## T12: Searching and sorting

### T12-E01: Linear search and binary search

Implement `linear_search(items, target)` and `binary_search(items, target)`.
Each returns `(index, comparisons)`, with `-1` for a missing target. Binary
search may assume sorted input. Implement `first_occurrence(items, target)`
to return the leftmost matching index in a sorted list with duplicates.
The sample checks comparison counts on 100 even numbers, including a missing
target, and a duplicate target.

### T12-E02: Bubble sort and selection sort

Implement `bubble_sort(items)` and `selection_sort(items)`. Each returns
`(sorted_copy, swaps)`, leaves the input unchanged, and counts swaps.
Bubble sort must stop early after a pass with no swaps.

## T13: Command-line applications

### T13-E01: To-do app with a command-line menu

Build a numbered-menu to-do manager with options to add a task, list tasks,
complete by ID, delete by ID, and quit. Tasks have a title, a `high`,
`medium`, or `low` priority (default `medium`), an ID, and a done state.
List open tasks before completed tasks, sorted by priority and then ID.
Persist JSON after every change, load it at startup, and treat end-of-input
like quitting. Invalid choices, IDs, and priorities should display a friendly
message and return to the menu.

Suggested package: `t13_e01_todo`, with separate model, storage, and CLI
modules. The sample session adds three tasks, lists them by priority,
completes one, checks invalid IDs and menu choices, and confirms saved data
can be loaded again.

### T13-E02: Student grade manager

Build a command-line grade manager for CSV rows with `student,subject,score`
columns. Provide `report`, `student NAME`, `top N`, and
`add NAME SUBJECT SCORE` subcommands. The report ranks students by average,
shows subject scores and letter grades, prints per-subject mean/median/range,
and identifies students averaging below 60. Letter-grade thresholds are
A (90+), B (80+), C (70+), D (60+), and F (below 60).

Skip missing or invalid scores with a warning containing the CSV line number.
The `add` command inserts or updates a score, rejects values outside 0–100,
and saves valid changes to CSV. The supplied sample checks malformed rows,
missing subjects, student and top reports, and rejection of score 101.
