# Project Status Checker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Introduction

This project is a tool to check the status codes of my project's websites but could also be used to other websites/APIs.

It is designed to be used as a GitHub Action.

The tool is written in Python and generates a JSON file that contains any disturbances to the live service.

## Table of Contents

- [Project Status Checker](#project-status-checker)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [GitHub Action Example](#github-action-example)

## Usage

### GitHub Action Example

The GitHub Action is designed to be used in a workflow.

```yaml
- name: Check Project Statuses
  uses: jackplowman/project-status-checker@latest
```
