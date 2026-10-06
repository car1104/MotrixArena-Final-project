# Installation Environment

## Installation Requirements

-   **Python Version**: {bdg-danger-line}`3.10.*`

    | Python Version | Support Status |
    | :------------: | :------------: |
    |     ≤ 3.9      |       ❌       |
    |      3.10      |       ✅       |
    |     ≥ 3.11     |       ❌       |

-   **Package Manager**: {bdg-danger-line}`UV`

-   **System and Architecture**:

    -   {bdg-danger-line}`Windows(x86_64)`
    -   {bdg-danger-line}`Linux(x86_64)`

    ```{note}
    Features supported on each platform:

    | Operating System | CPU Simulation | Interactive Viewer | GPU Simulation |
    | :--------------: | :------------: | :----------------: | :------------: |
    |      Linux       |       ✅       |         ✅          |    🛠️ In Development    |
    |     Windows      |       ✅       |         ✅          |    🛠️ In Development    |
    ```

## Installation Method

### Clone Project

```bash
git clone https://github.com/Motphys/MotrixLab.git
cd MotrixLab
```

### Install Dependencies

Use UV to install project dependencies:

```bash
# Install all dependencies
uv sync --all-packages --all-extras
```

If you only need to install one training backend, you can choose to install a specific backend type:

```bash
# Install SKRL JAX (support Linux only)
uv sync --all-packages --extra skrl-jax

# Install SKRL PyTorch
uv sync --all-packages --extra skrl-torch
```
