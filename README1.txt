# LangGraph Agent Script

## Overview
This script implements a LangGraph-based agent using the `langchain-ollama` and `langgraph` libraries.
The agent routes input to one of three nodes:
- Summary node using the Mistral model via Ollama
- Math evaluation node using Python eval
- Fallback node for unsupported commands

## Requirements
- Python 3.10+
- Ollama installed and `mistral` model pulled (`ollama pull mistral`)
- Packages installed:
    pip install langgraph langchain-ollama

## How to Run
1. Make sure your virtual environment is activated.
2. Run the script:

```bash
python agent_graph.py
```

## Screenshots Required for Submission
Please include:
- Output of Summary node
```
   --- Summary Test ---
Final Output: Summary:  LangGraph is a tool that coordinates large language models (LLMs) using a graph structure. Essentially, it manages and organizes the interaction between various LLMs for specific tasks.
```
- Output of Math node
```
   --- Math Test ---
Final Output: Summary:  The result of the expression 15 * 7 - 3 is 94.
```
- Output of Fallback node
```
   --- Fallback Test ---
Final Output: Summary:  Title: Une amélioration de l'éducation numérique

La présente étude examine les avantages potentiels d'une utilisation accrue des technologies numériques pour améliorer l'éducation. Elle souligne que la meilleure façon de le faire est par une intégration progressive et adaptée des technologies dans l'enseignement, ainsi qu'un entraînement continu pour les enseignants afin de se familiariser avec les nouvelles technologies et leur potentiel pédagogique.

L'étude met également en lumière la nécessité d'une planification stratégique et d'investissements pour améliorer l'accès à des ressources numériques de qualité et une infrastructure appropriée, afin que toutes les étudiants aient accès aux outils nécessaires pour réussir dans leur apprentissage.

In English: This study examines the potential benefits of increased use of digital technologies to improve education. It emphasizes that the best way to do this is through a progressive and adapted integration of technology in teaching, as well as continuous training for teachers to familiarize themselves with new technologies and their educational potential. The study also highlights the need for strategic planning and investments to improve access to quality digital resources and appropriate infrastructure, so that all students have access to the necessary tools to succeed in learning.

In French: Cette étude examine les avantages potentiels d'une utilisation accrue des technologies numériques pour améliorer l'éducation. Elle met en évidence qu'il est important de faire une intégration progressive et adaptée des technologies dans l'enseignement, ainsi que de former en permanence les enseignants afin qu'ils se familiarisent avec les nouvelles technologies et leur potentiel pédagogique. L'étude met également en lumière la nécessité d'une planification stratégique et d'investissements pour améliorer l'accès aux ressources numériques de qualité et une infrastructure appropriée, afin que tous les étudiants aient accès aux outils nécessaires pour réussir dans leur apprentissage.
```
## This is about the “LangGraph Agent Script”

