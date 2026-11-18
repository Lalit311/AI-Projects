#!/bin/bash

##########################
# Frontend
##########################

mkdir -p frontend/components

touch frontend/app.py

##########################
# Backend
##########################

mkdir -p backend

touch backend/app.py
touch backend/routes.py
touch backend/config.py

##########################
# LangGraph
##########################

mkdir -p graph

touch graph/__init__.py
touch graph/graph.py
touch graph/state.py
touch graph/planner.py
touch graph/executor.py
touch graph/nodes.py

##########################
# Tools
##########################

mkdir -p tools

touch tools/__init__.py
touch tools/sql_tool.py
touch tools/rag_tool.py
touch tools/analytics_tool.py
touch tools/recommendation_tool.py
touch tools/explanation_tool.py
touch tools/chart_tool.py
touch tools/registry.py

##########################
# Services
##########################

mkdir -p services

touch services/__init__.py
touch services/sqlite_service.py
touch services/llm_service.py
touch services/rag_client.py
touch services/memory_service.py

##########################
# Database
##########################

mkdir -p database

touch database/schema.sql
touch database/finance.db
touch database/seed.py

##########################
# Prompts
##########################

mkdir -p prompts

touch prompts/planner_prompt.py
touch prompts/sql_prompt.py
touch prompts/recommendation_prompt.py
touch prompts/explanation_prompt.py

##########################
# Models
##########################

mkdir -p models

touch models/__init__.py
touch models/state_models.py
touch models/api_models.py
touch models/tool_models.py

##########################
# Monitoring
##########################

mkdir -p monitoring

touch monitoring/__init__.py
touch monitoring/logger.py
touch monitoring/metrics.py
touch monitoring/tracing.py

##########################
# Tests
##########################

mkdir -p tests

touch tests/__init__.py

##########################
# Logs
##########################

mkdir -p logs

touch logs/.gitkeep

##########################
# Docs
##########################

mkdir -p docs

touch docs/HLD.md
touch docs/LLD.md
touch docs/API.md

##########################
# Config
##########################

touch .env
touch .env.example
touch requirements.txt
touch README.md
touch .gitignore

echo "Project structure created successfully!"