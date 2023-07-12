# LLM Workflow Engine (LWE) Test plugin

Test plugin for [LLM Workflow Engine](https://github.com/llm-workflow-engine/llm-workflow-engine)

This is a bare bones example of a shell command plugin that echos back whatever is entered.

## Installation

### From packages

Install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/llm-workflow-engine/lwe-plugin-test
```

### From source (recommended for development)

Install the latest version of this software directly from git:

```bash
git clone https://github.com/llm-workflow-engine/lwe-plugin-test.git
```

Install the development package:

```bash
cd llm-workflow-engine
pip install -e .
```

## Configuration

Add the following to `config.yaml` in your profile:

```yaml
plugins:
  enabled:
    - test
    # Any other plugins you want enabled...
  # These are the default values.
  test:
    response:
      prefix: '[LWE Plugin] Test'
```

## Usage

From a running LWE shell:

```bash
/test Hello World!
```
