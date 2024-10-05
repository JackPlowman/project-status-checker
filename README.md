# Project Status Checker

## Table of Contents

- [Project Status Checker](#project-status-checker)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)

## Introduction

This project is a tool to check the statuses of my project's websites but could also be used to other websites/APIs.

It is designed to be used as a GitHub Action.

The tool is written in Python and generates a JSON file that contains any disturbances to the live service.

## Usage

### GitHub Action Example

The GitHub Action is designed to be used in a workflow.

```yaml
- name: Check Project Statuses
  uses: jackplowman/project-status-checker@latest
```
