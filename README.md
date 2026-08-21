# Agentic Export Control

F108 of the Agentic AI Library.

A multi agent reference system for export control review, evidence organization, item and destination scoping, license question triage, and human controlled compliance workflows.

## Architecture

- [Agents](AGENTS)
- [Tools](TOOLS)
- [Skills](SKILLS)
- [Orchestration](orchestration)
- [Memory](memory)
- [State](state)
- [Schemas](schemas)
- [Prompts](prompts)
- [Config](config)
- [Safety](safety)
- [Observability](observability)
- [Evaluations](evals)
- [Benchmarks](benchmarks)
- [Examples](examples)
- [Tests](tests)
- [Architecture](docs/ARCHITECTURE.md)

## Safety

This repository supports compliance analysis and evidence organization only. It does not make binding legal determinations, authorize exports, classify controlled items, issue licenses, or replace qualified export control counsel or authorized compliance personnel. Consequential actions require human review and approval.

## Run

```bash
python run.py
```

## Test

```bash
python -m pytest -q
```
