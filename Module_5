# Week 5, CI/CD GitHub Actions Reading Assignment

## Chapter 2: How GitHub Actions Work

In this chapter, we explore the components and functionality of GitHub Actions. "GitHub Actions" refers to both the system for executing automated workflows in response to events and the individual units of code that implement these actions. This chapter explains the workflow of GitHub Actions, detailing the triggering events, the role of workflow files, and how jobs and steps are executed on runners.

### Overview of GitHub Actions Flow

1. **Triggering Event**: An event in a GitHub repository triggers a workflow. This event is often associated with a unique SHA1 value and a Git reference (e.g., a branch).
2. **Workflow Identification**: The repository’s `.github/workflows` directory is searched for workflow files that respond to the event type. Workflows can be triggered by various events, such as a push to a specific branch.
3. **Workflow Execution**: Matching workflows are identified and executed. A workflow, written in YAML, contains jobs and steps. Jobs run on runners and can execute steps either as shell commands or predefined actions.

### Components of a Workflow

- **Steps**: Basic units of execution within a job. They can invoke actions or run shell commands.
- **Runners**: Servers (virtual, physical, or containers) where the code is executed.
- **Jobs**: Group steps and define which runner to use. They aggregate smaller tasks to achieve a particular goal.
- **Workflow**: Like a pipeline, it responds to events and executes jobs.

### Triggering Workflows

- Events that trigger workflows include operations in a GitHub repository, external triggers, schedules, and manual initiation.
- The `on` clause in the workflow syntax specifies the events that trigger the workflow.

### Workflow Example

A simple Go build workflow example shows how a workflow file is structured:

```yaml
name: Simple Go Build

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Go version
        uses: actions/setup-go@v2
        with:
          go-version: '1.15.1'
      - run: go run hello-world.go

## Chapter 3. What’s in an action?

The core functionality revolves around workflows—code that responds to events and executes jobs. At the lowest level, a workflow’s jobs execute steps, which can call either an OS command or a GitHub Actions "action."

### Workflows Versus Actions

Actions can be likened to plug-ins or modules in other applications, while workflows function more like pipelines or scripts that utilize these plug-ins or modules.

### Implementation of an Action

An action can range from a simple shell script to a complex set of code, tests, and workflows handling CI/CD tasks. For example, the checkout action is a complex implementation used for tasks like content validation, building, and packaging.

### The Structure of an Action

Actions reside in GitHub repositories and include supporting files like licensing, tests, and source code. They are defined by a metadata file (e.g., action.yml) specifying inputs, outputs, and configuration.

### Interfacing with Actions

To use an action in a workflow, the action repository must include an action.yml file defining inputs, outputs, and how it runs. This YAML file is crucial for understanding how workflows interact with the action.

### Using Actions

Actions are referenced in workflows using the `uses` clause, specifying the repository path and version (e.g., `actions/checkout@v3`). GitHub recommends semantic versioning for specifying action versions.

### Public Actions and the Actions Marketplace

GitHub's Actions Marketplace hosts public actions, providing a central repository for sharing actions. It supports search functionality and categorization to find and use existing actions easily.

## Conclusion

Actions in GitHub are encapsulated units of functionality stored in repositories, defined by metadata files like action.yml. They play a crucial role in workflows by providing reusable automation steps. The GitHub Actions Marketplace facilitates the sharing and discovery of these actions, enhancing workflow development efficiency.


# Chapter 6. Docker Containers

Regardless of the complexity of the actions you implement using GitHub Actions, there must be a system in place to execute those actions—a virtual or physical system with adequate resources to process jobs, configured to interact with the Actions control plane during job dispatch. In GitHub Actions terminology, these systems where workflow jobs are executed are referred to as runners.

## Docker Containers as Runners

GitHub Actions allows you to use Docker containers as runners, providing flexibility and reproducibility in your workflows. Using Docker containers as runners offers several advantages, including:

- **Isolation**: Each job runs in its own clean environment, isolated from the host system and other jobs.
- **Consistency**: Docker containers ensure that the runtime environment remains consistent across different workflows and systems.
- **Reproducibility**: Docker images can be versioned, allowing you to reproduce builds and deployments reliably.

### Using Docker Containers in GitHub Actions

To specify a Docker container as a runner in your workflow, use the `container` keyword in your workflow YAML file:

```yaml
jobs:
  build:
    runs-on: container
    container:
      image: docker://your-docker-image:tag
