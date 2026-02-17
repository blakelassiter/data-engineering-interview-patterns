# Data Engineering Interview Patterns

Algorithmic patterns, SQL techniques and system design frameworks
for data engineering interviews. 1,493 tested solutions across
76 algorithmic problems, 26 SQL problems, dbt production patterns, 5 system design walkthroughs and PySpark distributed equivalents.

![Tests](https://github.com/blakelassiter/data-engineering-interview-patterns/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## What this is

A comprehensive interview preparation resource for data engineers. Covers the three types of technical rounds you will face: coding (algorithmic patterns), SQL and system design. Every algorithmic and SQL solution is tested. The system design section provides frameworks for 45-minute interviews, not exhaustive references.

## Quick start

```bash
# Clone and set up
git clone https://github.com/blakelassiter/data-engineering-interview-patterns.git
cd data-engineering-interview-patterns
uv sync

# Run all tests
uv run pytest

# Run tests for a specific section
uv run pytest patterns/      # Algorithmic patterns (1142 tests)
uv run pytest sql/           # SQL patterns (254 tests)
uv run pytest benchmarks/   # Benchmark correctness (27 tests)

# Optional: install PySpark for distributed equivalents
uv sync --extra spark
uv run pytest spark/          # PySpark tests (70 tests)
```

Or click **Open in Codespaces** for a zero-setup environment.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/blakelassiter/data-engineering-interview-patterns)

## Repository structure

```
├── patterns/                  # Algorithmic patterns (12 subsections, 76 problems)
│   ├── 01_hash_map/
│   ├── 02_two_pointers/
│   ├── 03_binary_search/
│   ├── 04_sliding_window/
│   ├── 05_heap_priority_queue/
│   ├── 06_graph_topological_sort/
│   ├── 07_intervals/
│   ├── 08_stack/
│   ├── 09_string_parsing/
│   ├── 10_recursion_trees/
│   ├── 11_probabilistic_structures/
│   └── 12_combined_patterns/
│
├── sql/                       # SQL patterns (6 subsections, 26 problems)
│   ├── 01_window_functions/
│   ├── 02_joins/
│   ├── 03_aggregations/
│   ├── 04_recursive_ctes/
│   ├── 05_optimization_and_production/
│   └── 06_dbt_patterns/
│
├── spark/                     # PySpark equivalents (optional dependency, 70 tests)
│   ├── 01_joins/             # Broadcast, shuffle and skew handling
│   ├── 02_sorting_and_merging/ # Sort-merge join, top-k optimization
│   ├── 03_window_functions/  # Ranking, dedup, running aggregates, sessionization
│   ├── 04_aggregations/      # GroupBy patterns, approximate counting
│   ├── 05_partitioning/      # Partition strategies, explain plans, optimization
│   ├── 06_streaming/         # Structured Streaming with tumbling/sliding windows
│   └── reference/            # Cheatsheet and interview questions
│
├── system_design/             # System design frameworks (17 reference docs)
│   ├── foundations/           # Tradeoffs, estimation, communication
│   ├── patterns/             # Ingestion, modeling, pipelines, scale, quality
│   ├── walkthroughs/         # 5 full interview simulations
│   └── reference/            # Throughput numbers, cost models, tech decisions
│
├── benchmarks/                # 7 performance comparison scripts with tests
│
└── docs/                      # Study aids and cheat sheets
    ├── PATTERN_RECOGNITION.md # "If you see X, think Y"
    ├── INTERVIEW_STRATEGY.md  # Pacing, communication, what to do when stuck
    ├── TIME_COMPLEXITY_CHEATSHEET.md
    ├── GLOSSARY.md
    └── STUDY_PLANS.md         # 3 structured study tracks (1-week to 1-month)
```

## How to use this repo

| Preparing for | Start here | Then work through |
|---|---|---|
| Coding rounds | [`docs/PATTERN_RECOGNITION.md`](docs/PATTERN_RECOGNITION.md) | [`patterns/`](patterns/) |
| SQL rounds | [`sql/README.md`](sql/README.md) | [`sql/01`](sql/01_window_functions/) through [`sql/06`](sql/06_dbt_patterns/) |
| PySpark rounds | [`spark/README.md`](spark/README.md) | [`spark/reference/`](spark/reference/) for cheatsheet and questions |
| System design | [`system_design/foundations/`](system_design/foundations/) | [`system_design/patterns/`](system_design/patterns/), then [`walkthroughs/`](system_design/walkthroughs/) |
| General review | [`docs/INTERVIEW_STRATEGY.md`](docs/INTERVIEW_STRATEGY.md) | Whichever section needs the most work |

## What is inside each problem

- Difficulty and interview frequency tags
- Problem description with worked example
- Multiple approaches (brute force to optimized)
- Complexity analysis (time and space)
- Edge cases explicitly called out
- Interview tips with evaluator framing
- At Scale section (what happens at 10M+ rows)
- DE-specific application
- Full test suite

## About

Built by [Blake Lassiter](https://www.linkedin.com/in/blakelassiter/) - 15+ years building data platforms and production AI/ML systems.

Companion article series: [Data Engineering Interview Patterns on Medium](https://medium.com/@blakelassiter)

## License

[MIT](LICENSE)

## Contributing

Not accepting contributions at this time (personal project).
