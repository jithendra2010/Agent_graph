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
Final Output: Summary:  Title: Une am�lioration de l'�ducation num�rique

La pr�sente �tude examine les avantages potentiels d'une utilisation accrue des technologies num�riques pour am�liorer l'�ducation. Elle souligne que la meilleure fa�on de le faire est par une int�gration progressive et adapt�e des technologies dans l'enseignement, ainsi qu'un entra�nement continu pour les enseignants afin de se familiariser avec les nouvelles technologies et leur potentiel p�dagogique.

L'�tude met �galement en lumi�re la n�cessit� d'une planification strat�gique et d'investissements pour am�liorer l'acc�s � des ressources num�riques de qualit� et une infrastructure appropri�e, afin que toutes les �tudiants aient acc�s aux outils n�cessaires pour r�ussir dans leur apprentissage.

In English: This study examines the potential benefits of increased use of digital technologies to improve education. It emphasizes that the best way to do this is through a progressive and adapted integration of technology in teaching, as well as continuous training for teachers to familiarize themselves with new technologies and their educational potential. The study also highlights the need for strategic planning and investments to improve access to quality digital resources and appropriate infrastructure, so that all students have access to the necessary tools to succeed in learning.

In French: Cette �tude examine les avantages potentiels d'une utilisation accrue des technologies num�riques pour am�liorer l'�ducation. Elle met en �vidence qu'il est important de faire une int�gration progressive et adapt�e des technologies dans l'enseignement, ainsi que de former en permanence les enseignants afin qu'ils se familiarisent avec les nouvelles technologies et leur potentiel p�dagogique. L'�tude met �galement en lumi�re la n�cessit� d'une planification strat�gique et d'investissements pour am�liorer l'acc�s aux ressources num�riques de qualit� et une infrastructure appropri�e, afin que tous les �tudiants aient acc�s aux outils n�cessaires pour r�ussir dans leur apprentissage.
```
## This is about the �LangGraph Agent Script�

