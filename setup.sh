#!/usr/bin/env bash

VENV_DIR=".venv"

# Check if venv exists
if [ -d "$VENV_DIR" ]; then
    echo "✅ Virtual environment already exists in $VENV_DIR"
    echo "👉 Activating it..."
    source "$VENV_DIR/bin/activate"
else
    echo "🚀 Setting up Spark Lab environment..."
    echo "📦 Creating virtual environment in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"

    # activate venv
    source "$VENV_DIR/bin/activate"

    # upgrade pip
    echo "⬆️  Upgrading pip..."
    pip install --upgrade pip

    # install dependencies
    echo "📥 Installing dependencies (PySpark + JupyterLab)..."
    pip install pyspark jupyterlab

    echo "🎉 Setup complete!"
fi

echo ""
echo "👉 To deactivate the environment, run: deactivate"
echo "👉 Current Python: $(which python)"
echo "👉 Current Pip:    $(which pip)"
