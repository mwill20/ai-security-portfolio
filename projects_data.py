projects = {
    "mcp": {
        "title": "MCP Ecosystem",
        "icon": "fas fa-cogs",
        "description": "The Model Context Protocol (MCP) is a scalable framework designed to enable modular AI Agents and tools to communicate and collaborate seamlessly. My ecosystem includes core servers and diverse agents.",
        "projects": [
            {
                "title": "MCP Intelligence System",
                "description": "Claude-powered operational intelligence platform that connects to live engineering data over MCP and answers engineering-operations questions in natural language, producing a daily morning brief and live incident views.",
                "tech": ["Python", "MCP", "Claude"],
                "icon": "fas fa-chart-line",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AV_MCP_Intel_System", "class": "btn-primary"}
                ]
            },
            {
                "title": "MCP Model Server",
                "description": "Python backend server implementing the Model Context Protocol to host AI models and expose them to MCP-compliant agents and applications through a standardized interface.",
                "tech": ["Python", "MCP"],
                "icon": "fas fa-network-wired",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/MCP_Project", "class": "btn-primary"},
                    {"label": "Live Demo", "url": "https://huggingface.co/spaces/mwill-AImission/MCP_Project", "class": "btn-success"}
                ]
            },
            {
                "title": "MCP Tools Demo",
                "description": "Multi-tool Gradio application with MCP integration, bundling several tools behind a single interactive front end.",
                "tech": ["Gradio", "MCP"],
                "icon": "fas fa-toolbox",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/mcp-tools-demo", "class": "btn-primary"},
                    {"label": "Live Demo", "url": "https://huggingface.co/spaces/mwill-AImission/mcp-tools-demo", "class": "btn-success"}
                ]
            }
        ]
    },
    "security": {
        "title": "Security",
        "icon": "fas fa-shield-alt",
        "projects": [
            {
                "title": "Rapid Exposure Response (RER) Kit",
                "description": "Generic, reusable playbook kit for reacting to emerging critical vulnerabilities: contain fast with compensating controls, remediate, verify, and hunt. An eight-stage playbook with entry and exit gates, compensating-control and verification libraries, SIEM-agnostic retro-hunt hypotheses, Copilot agent instructions and prompt packs, and drills with answer keys. Built to be pulled one way into a work environment and run with Microsoft 365 Copilot.",
                "tech": ["Python", "PowerShell", "M365 Copilot", "Vulnerability Management"],
                "icon": "fas fa-bolt",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/rapid-exposure-response", "class": "btn-primary"}]
            },
            {
                "title": "SecureCLI-Tuner",
                "description": "Security-first LLM fine-tuned for Agentic DevOps that translates natural language into safe, valid Bash commands. Implements a Defense-in-Depth architecture with sanitized QLoRA fine-tuning and three-layer runtime guardrail system.",
                "icon": "fas fa-terminal",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/SecureCLI-Tuner", "class": "btn-primary"}]
            },
            {
                "title": "AI Guardrails",
                "description": "Layered security framework for LLMs and agents that combines deterministic rules, semantic classifiers, and policy enforcement to detect prompt injection, malicious intent, and unsafe reasoning before outputs reach users or systems.",
                "icon": "fas fa-user-shield",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/AI-Guardrails", "class": "btn-primary"}]
            },
            {
                "title": "SageVault - Secure RAG",
                "description": "Security-focused RAG application with built-in guardrails for safe document and codebase analysis with AI.",
                "icon": "fas fa-lock",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/SageVault", "class": "btn-primary"},
                    {"label": "Watch Demo", "url": "../static/videos/sagevault-demo.mp4", "class": "btn-secondary"}
                ]
            },
            {
                "title": "ML Malware Detection System",
                "description": "Enterprise-Grade Security: Advanced ensemble ML system with 9 trained models, grey-zone decision gating, and SHAP explainability. Features Streamlit web interface, CLI tools, and production-ready deployment achieving 95%+ recall for SOC environments.",
                "tech": ["Ensemble Learning", "SHAP", "Streamlit", "CI/CD"],
                "icon": "fas fa-shield-virus",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/ml-malware-detection-system", "class": "btn-primary"},
                    {"label": "Live Demo", "url": "https://ml-malware-detection-system-jokkbsjues7uiddb7sduh4.streamlit.app/", "class": "btn-success"},
                    {"label": "Technical Overview", "url": "https://github.com/mwill20/ml-malware-detection-system/blob/main/README.md", "class": "btn-secondary"}
                ]
            },
            {
                "title": "Malware Analysis LightGBM",
                "description": "AI-powered malware detection using LightGBM and static PE file analysis for enterprise endpoint security. Achieves 98%+ F1-score with millisecond prediction times.",
                "icon": "fas fa-bug",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/Malware_analysis_LightGBM", "class": "btn-primary"}]
            },
            {
                "title": "PE File Metadata Analysis",
                "description": "Comprehensive malware detection using PE file metadata with advanced feature engineering, visualization, and model validation. Multi-method feature selection with PCA, t-SNE, and ensemble methods.",
                "icon": "fas fa-file-code",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/Malware_Detection_using_PE_File_Metadata", "class": "btn-primary"}]
            },
            {
                "title": "High-Recall Malware Detector",
                "description": "Integration Capstone: Combines supervised and unsupervised ML approaches with recall-first optimization for SOC environments. Synthesizes insights from LightGBM and PE metadata projects into a unified detection framework achieving 99.95% recall.",
                "icon": "fas fa-crosshairs",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/High-Recall_Malware_Detector_Supervised_Unsupervised", "class": "btn-primary"}
                ]
            },
            {
                "title": "Unsupervised Anomaly Detection",
                "description": "Proactive Malware Defense: Signature-free malware detection using unsupervised learning for Aegis AI Security's Sentinel Endpoint Agent. Achieves 93% AUC with Isolation Forest for real-time pre-execution threat analysis.",
                "icon": "fas fa-search",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Unsupervised_Anomaly_Detection_Proactive_Malware_Defense", "class": "btn-primary"}
                ]
            },
            {
                "title": "Structural Anomaly Detection",
                "description": "Malware Triage: Advanced ensemble-based PE file analysis combining Isolation Forest, K-Means, and One-Class SVM. Features interpretable anomaly scoring and confidence-based triage for SOC environments with rich visualization suite.",
                "icon": "fas fa-microscope",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Unsupervised_Structural_Anomaly_Detection_PE_Files_Malware_Triage", "class": "btn-primary"}
                ]
            },
            {
                "title": "Smart Security Camera",
                "description": "An intelligent security system with face detection and motion tracking, built with Python and OpenCV.",
                "icon": "fas fa-video",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/smart-security-camera", "class": "btn-primary"}]
            }
,
            {
                "title": "ClawGuard",
                "description": "Guardrail-first agent security monitoring framework built around OpenClaw job-search telemetry, detecting unsafe agent behavior and preserving evidence for investigation.",
                "tech": ["Python", "Agent Security", "Telemetry"],
                "icon": "fas fa-shield-halved",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/ClawGuard", "class": "btn-primary"}
                ]
            },
            {
                "title": "MalVec",
                "description": "Explainable malware classification using structural similarity. Classifies PE files as malware or benign by comparing them against known samples, surfacing the reasoning rather than returning an opaque risk score.",
                "tech": ["Python", "PE Analysis", "Explainability"],
                "icon": "fas fa-fingerprint",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/MalVec", "class": "btn-primary"}
                ]
            },
            {
                "title": "LLM Red Teaming Audit",
                "description": "Security assessment of a financial-services chatbot and an e-commerce agent. Manual probing, automated scanning with Giskard, and adversarial simulation identified 16 distinct vulnerabilities across the OWASP Top 10 for LLMs.",
                "tech": ["LLM Red Teaming", "Giskard", "OWASP LLM Top 10"],
                "icon": "fas fa-user-secret",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/LLM-Red-Teaming-Audit-Demo", "class": "btn-primary"}
                ]
            },
            {
                "title": "ThreatPrism V2",
                "description": "Demo-safe SOC migration accelerator for organizations moving from outsourced SOC operations toward an internal model. A case-centric backend ingests SOAR-style payloads, normalizes evidence, applies deterministic guardrails, and produces structured triage and GRC output behind role-safe API views.",
                "tech": ["Python", "SOC", "Guardrails", "GRC"],
                "icon": "fas fa-sitemap",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/ThreatPrism_V2", "class": "btn-primary"}
                ]
            },
            {
                "title": "CLI-Tuner",
                "description": "Data and training pipeline behind SecureCLI-Tuner: a security-aware ML workflow for translating natural language into Bash, built on Qwen2.5-Coder-7B-Instruct with zero-tolerance validation.",
                "tech": ["Python", "Qwen2.5-Coder", "Dataset Engineering"],
                "icon": "fas fa-code",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/CLI-Tuner", "class": "btn-primary"}
                ]
            },
            {
                "title": "Governed AI Pipeline",
                "description": "Portable governance pipeline for Claude Code - custom slash commands, validation hooks, and audit logging - built to demonstrate that an AI-augmented development workflow can be rolled out safely across a small team.",
                "tech": ["Claude Code", "Governance", "Audit Logging"],
                "icon": "fas fa-clipboard-check",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Governed_AI_Pipeline", "class": "btn-primary"}
                ]
            },
            {
                "title": "AI Sec Practice Ground",
                "description": "Offline-first rehearsal range for AI security workflows. Provides deterministic simulators and synthetic fixtures so a full loop - read the challenge, run the workflow, capture evidence, write the report - can be practiced without standing up lab infrastructure.",
                "tech": ["PowerShell", "Simulation", "Blue Team"],
                "icon": "fas fa-flask",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AI-SEC-practice-ground", "class": "btn-primary"}
                ]
            },
            {
                "title": "GAN Security Learning",
                "description": "Step-by-step learning project on Generative Adversarial Networks and AI security - building image-generating models, then attacking and defending them to observe the failure modes directly.",
                "tech": ["Python", "GANs", "Adversarial ML"],
                "icon": "fas fa-vials",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/GAN-Security-Learning", "class": "btn-primary"}
                ]
            }
        ]
    },
    "agents": {
        "title": "AI Agents",
        "icon": "fas fa-robot",
        "projects": [
             {
                "title": "TrustBench SecureEval Ops v3.0 Production",
                "description": "Production-Grade Multi-Agent Security Evaluation Framework: Advanced evolution of Trust Bench featuring SecureEval guardrails, intelligent agent routing, consensus building, and operational excellence. Features specialized security, quality, and documentation agents with cross-agent collaboration, weighted scoring, confidence metrics, and comprehensive export capabilities. Includes structured logging, health probes, CI/CD pipeline, and 79% test coverage.",
                "tech": ["Python", "LangGraph", "Multi-Agent Systems", "FastAPI", "Security Analysis", "CI/CD"],
                "icon": "fas fa-shield-alt",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Trust-Bench-SecureEval-Ops", "class": "btn-primary"}
                ]
            },
            {
                "title": "Aegis MultiAgent SOC Competition Finalist (v1)",
                "description": "Secure multi-agent SOC triage with A2A guardrails and structured observability, designed as a v1 competition finalist with v2 upgrades planned for expanded SOC automation.",
                "tech": ["Python 3.13", "Google ADK", "a2a-sdk", "Gemini 2.5 Flash-Lite", "Uvicorn", "Pytest"],
                "icon": "fas fa-trophy",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/MultiAgent_SOC", "class": "btn-primary"}
                ]
            },
            {
                "title": "Trust Bench Demo",
                "description": "A LangGraph-based multi-agent workflow that inspects software repositories for security leaks, code quality gaps, and documentation health. Features a collaborative system of specialized agents working together to provide comprehensive repository analysis.",
                "tech": ["Python", "LangGraph", "Multi-Agent Systems", "Security Analysis"],
                "icon": "fas fa-laptop-code",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Trust_Bench", "class": "btn-primary"},
                    {"label": "Watch Demo", "url": "https://1drv.ms/v/c/2c8c41c39e8a63cb/EQil7I1iewdEuzPdQGBqVOYBHaRg9tBcyogZvmKUXKFLyw?e=8Dl8P5", "class": "btn-secondary"}
                ]
            },
            {
                "title": "AgentLedger",
                "description": "Proof-of-concept six-layer trust infrastructure for agent-native services, covering discovery, identity, trust signals, context disclosure, workflow validation, and liability evidence. Registers and verifies services rather than executing workflows itself.",
                "tech": ["Python", "Agent Identity", "Trust Infrastructure"],
                "icon": "fas fa-certificate",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AgentLedger", "class": "btn-primary"}
                ]
            },
            {
                "title": "AI Factory",
                "description": "Portable nine-agent software factory with security engineering built into the pipeline at both design time and implementation time. Tool-agnostic - installs into any project and produces auditable, security-reviewed code.",
                "tech": ["Multi-Agent Systems", "Secure SDLC", "Shell"],
                "icon": "fas fa-industry",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/ai-factory", "class": "btn-primary"}
                ]
            },
            {
                "title": "Quorum",
                "description": "Multi-agent code-review pipeline with a deterministic merge gate, packaged as a versioned, parameterized, tested skill library. Built as a Claude Code Mastery course mini-project.",
                "tech": ["Python", "Multi-Agent Review", "CI Gate"],
                "icon": "fas fa-code-branch",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Quorum_AV", "class": "btn-primary"}
                ]
            },
            {
                "title": "Agent Config Sync",
                "description": "Sanitized public mirror of a private deployment, published for the Kaggle AI Agents Intensive capstone. Generates an AI assistant's global instructions and skill library for multiple runtimes from a single source of truth.",
                "tech": ["Python", "Agent Configuration", "Kaggle Capstone"],
                "icon": "fas fa-arrows-rotate",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/agent-config-sync-public", "class": "btn-primary"}
                ]
            },
            {
                "title": "Spec-Driven Feature Factory",
                "description": "URL shortening service built spec-first, where every line of code answers to a documented requirement. Demonstrates spec-driven development and YAML prompt engineering; built as a Claude Code course assignment.",
                "tech": ["Python", "Spec-Driven Development"],
                "icon": "fas fa-file-contract",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Spec-Driven_Feature_Factory", "class": "btn-primary"}
                ]
            },
            {
                "title": "ADK Expense Approval Agent",
                "description": "Expense-approval workflow on Google's Agent Development Kit where the routing gate is deterministic, not a model decision. A plain threshold comparison auto-approves small expenses and suspends larger ones on a RequestInput interrupt until a human approves or rejects, so the LLM never gates the money decision.",
                "tech": ["Python", "Google ADK", "Human-in-the-Loop", "Terraform"],
                "icon": "fas fa-user-check",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/adk-expense-approval-agent", "class": "btn-primary"}
                ]
            },
            {
                "title": "Yahoo Finance API",
                "description": "Four FastAPI endpoints over Yahoo Finance data (company profile, market snapshot, historical prices, and deterministic analytics) that validate input before every upstream call and return clear 400/404/422 errors. Coursework demo exercised in-process with TestClient; no LLM involved.",
                "tech": ["Python", "FastAPI", "Pydantic", "yfinance"],
                "icon": "fas fa-chart-line",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/04-yahoo-finance-api", "class": "btn-primary"}
                ]
            },
            {
                "title": "Study Assistant Quiz Generator",
                "description": "LangChain prompt chain that summarizes a PDF or pasted study material into key points, then writes multiple-choice questions as a Pydantic schema so malformed questions are dropped before anything is shown. Coursework project on prompt engineering and structured output.",
                "tech": ["Python", "LangChain", "OpenAI", "Pydantic"],
                "icon": "fas fa-graduation-cap",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/05-study-assistant-quiz-generator", "class": "btn-primary"}
                ]
            },
            {
                "title": "Financial Image Scans",
                "description": "Multimodal LangChain notebook that reads scanned financial-report pages into a typed list of figures, then writes summaries for an investor, analyst or auditor. Reading and writing are separate calls, so a misread figure stays visible instead of being buried in prose.",
                "tech": ["Python", "LangChain", "Vision Models", "Pydantic"],
                "icon": "fas fa-file-invoice-dollar",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/06-financial-image-scans", "class": "btn-primary"}
                ]
            },
            {
                "title": "Web Research ReAct Agent",
                "description": "ReAct loop built from scratch with no agent framework: plans research questions, answers each with a Tavily web-search tool, and compiles a sourced Markdown report. Tool calls are validated before they run, and search results are treated as untrusted input.",
                "tech": ["Python", "ReAct", "Planning Pattern", "Tavily"],
                "icon": "fas fa-magnifying-glass",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/07-web-research-react-agent", "class": "btn-primary"}
                ]
            },
            {
                "title": "Travel Assistant Agent",
                "description": "LangChain tool-calling agent that returns current weather and top attractions for a destination. A deterministic input validator runs before the model, shaped by should-fail tests that caught prompt-injection and newline-smuggling inputs. Both tools are read-only.",
                "tech": ["Python", "LangChain", "Tavily", "Input Validation"],
                "icon": "fas fa-plane-departure",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/08-travel-assistant-agent", "class": "btn-primary"}
                ]
            },
            {
                "title": "Competitor Intelligence Agent",
                "description": "Conversational LangChain agent with per-session SQLite memory that researches nearby retail competitors. Input gates run ahead of the model, an output check flags any cited URL a tool did not return, and footfall figures are labelled as estimates rather than measurements.",
                "tech": ["Python", "LangChain", "Tavily", "SQLite", "Guardrails"],
                "icon": "fas fa-store",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/09-competitor-intel-agent", "class": "btn-primary"}
                ]
            },
            {
                "title": "Logistics Optimization Crew",
                "description": "Two-agent CrewAI system for inventory turnover at a distributor. Metrics are computed in plain Python, an input gate resolves product names against a catalog so caller text never reaches the prompt, and an output gate checks the strategy only names requested SKUs.",
                "tech": ["Python", "CrewAI", "Guardrails"],
                "icon": "fas fa-truck",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/10-logistics-optimization-crew", "class": "btn-primary"}
                ]
            },
            {
                "title": "Multi-Agent EDA with AutoGen",
                "description": "Six AutoGen agents take a synthetic, deliberately dirty dataset from raw CSV to a critic-reviewed EDA report. Turn order is a plain-Python state machine, and every code block the agents write must pass a static AST gate before it is executed.",
                "tech": ["Python", "AutoGen (AG2)", "Multi-Agent Systems", "Code Gating"],
                "icon": "fas fa-chart-pie",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/11-eda-multiagent-autogen", "class": "btn-primary"}
                ]
            },
            {
                "title": "LangGraph Math Agent",
                "description": "LangGraph agent where the LLM decides and Python computes: four arithmetic tools with two-layer validation (including nan and inf, which Pydantic accepts), error strings instead of raised exceptions, and an audit record for every tool call.",
                "tech": ["Python", "LangGraph", "Pydantic", "Audit Logging"],
                "icon": "fas fa-calculator",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/12-langgraph-math-agent", "class": "btn-primary"}
                ]
            },
            {
                "title": "LangGraph Multi-Agent Research",
                "description": "Router agent sends each query to an LLM answerer, a Tavily web-search agent, or a RAG agent over a small knowledge base, and a summarizer produces the structured answer. Routing uses typed structured output so the graph only receives a valid route.",
                "tech": ["Python", "LangGraph", "RAG", "Tavily"],
                "icon": "fas fa-diagram-project",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/13-langgraph-multiagent-research", "class": "btn-primary"}
                ]
            },
            {
                "title": "Reflection Agents with AutoGen",
                "description": "Two-agent reflection loop: a Content Creator drafts, a Content Critic reviews for language clarity and technical accuracy, the Creator revises, and an LLM summarizes the exchange. Neither agent has tools, and the turn count is capped at 3 or 5.",
                "tech": ["Python", "AutoGen", "Reflection Pattern"],
                "icon": "fas fa-comments",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/AGENTs/tree/main/14-reflection-agents-autogen", "class": "btn-primary"}
                ]
            }
        ]
    },
    "ml": {
        "title": "ML Engineering",
        "icon": "fas fa-brain",
        "projects": [
            {
                "title": "NLP RAG Medical Assistant",
                "description": "Retrieval-Augmented Generation system built to help healthcare professionals find medical information from trusted sources, using the Merck Manual as its primary knowledge base.",
                "tech": ["RAG", "NLP", "Healthcare"],
                "icon": "fas fa-notes-medical",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/NLP_RAG_Medical_Assistant", "class": "btn-primary"}
                ]
            },
            {
                "title": "HuggingFace Sentiment Analysis",
                "description": "Sentiment analysis built on Hugging Face Transformers and PyTorch, demonstrating how to fine-tune a pre-trained transformer for a downstream classification task.",
                "tech": ["PyTorch", "Transformers", "Fine-Tuning"],
                "icon": "fas fa-face-smile",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/HuggingFace-Sentiment-Analysis", "class": "btn-primary"}
                ]
            },
            {
                "title": "Bank Churn Prediction",
                "description": "Neural network model for predicting bank customer churn, identifying accounts likely to leave so retention effort can be targeted.",
                "tech": ["Neural Networks", "Classification"],
                "icon": "fas fa-building-columns",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Bank_Churn_NN", "class": "btn-primary"}
                ]
            },
            {
                "title": "Visa Approval Prediction",
                "description": "XGBoost classifier predicting US visa application outcomes, used to surface the factors that most influence approval decisions.",
                "tech": ["XGBoost", "Classification"],
                "icon": "fas fa-passport",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/XGBoost_Visa_Approval_Prediction", "class": "btn-primary"}
                ]
            },
            {
                "title": "Loan Acceptance Prediction",
                "description": "Decision Tree classifier predicting personal loan acceptance, used to identify which existing bank customers are most likely to convert.",
                "tech": ["Decision Trees", "Classification"],
                "icon": "fas fa-hand-holding-dollar",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Loan_Acceptance_DecisionTree", "class": "btn-primary"}
                ]
            },
            {
                "title": "FoodHub Data Analysis",
                "description": "Exploratory analysis of food-delivery order data, surfacing customer ordering patterns and restaurant performance for a food aggregator.",
                "tech": ["Pandas", "EDA", "Visualization"],
                "icon": "fas fa-chart-pie",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/FoodHub-Data-Analysis", "class": "btn-primary"}
                ]
            },
            {
                "title": "XGBoost Regressor",
                "description": "XGBoost regressor applied to a continuous-target prediction task, covering feature preparation, training, tuning, and evaluation.",
                "tech": ["XGBoost", "Regression"],
                "icon": "fas fa-chart-simple",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/XGBoost-Regressor", "class": "btn-primary"}
                ]
            }
        ]
    },
    "cloud": {
        "title": "Cloud",
        "icon": "fas fa-cloud",
        "projects": [
            {
                "title": "Azure Resource Optimization Lab",
                "description": "End-to-end Azure fundamentals — ARM-based VM deployment with tagging, governance policies, and Azure Monitor alerts. Demonstrates cloud architecture, cost optimization, and observability with Infrastructure-as-Code (IaC).",
                "tech": ["Azure ARM Templates", "IaC", "Azure Monitor", "Governance"],
                "icon": "fab fa-microsoft",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Azure-Resource-Optimization-Lab", "class": "btn-primary"}
                ]
            }
,
            {
                "title": "BigQuery Release Pulse",
                "description": "Dashboard that tracks Google Cloud BigQuery release notes, slicing daily updates into individual release items and filtering them by type. Flask server with a vanilla HTML/JS client.",
                "tech": ["Flask", "BigQuery", "Google Cloud"],
                "icon": "fab fa-google",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/event-talks-app", "class": "btn-primary"}
                ]
            },
            {
                "title": "GCP Document Pipeline",
                "description": "Event-driven document ingestion on Google Cloud, provisioned end to end with Terraform. A GCS upload fires a storage notification onto Pub/Sub, an OIDC-authenticated push subscription invokes a Cloud Run service, Gemini extracts and classifies the document via Vertex AI, and the metadata lands in BigQuery behind a Streamlit dashboard.",
                "tech": ["Terraform", "Cloud Run", "Pub/Sub", "BigQuery", "Vertex AI"],
                "icon": "fas fa-diagram-project",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/gcp-document-pipeline", "class": "btn-primary"}
                ]
            }
        ]
    },
    "fun": {
        "title": "Just for Fun",
        "icon": "fas fa-gamepad",
        "projects": [
            {
                "title": "Static on Pier Nine — YARA-L 2.0 Search Trainer",
                "description": "Browser-only course that teaches Google SecOps Search queries in YARA-L 2.0 the way KC7 teaches KQL, then the step from search to detection: three original investigations, a query desk that returns rows (and detections in Rule mode) against fictional datasets, and a Casebook that teaches analyst note-keeping through to remediation and handoff.",
                "tech": ["YARA-L 2.0", "Google SecOps", "JavaScript", "Detection Engineering"],
                "icon": "fas fa-broadcast-tower",
                "links": [
                    {"label": "Play the Course", "url": "https://mwill20.github.io/KC7SecOpsClaude/", "class": "btn-success"},
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/KC7SecOpsClaude", "class": "btn-primary"}
                ]
            },
            {
                 "title": "Python-Dojo — Security Reps Playground",
                 "description": "A security gym for AI engineers to build muscle memory around sanitization, API management, and guardrail patterns using a Mastery Loop training engine.",
                 "tech": ["React", "Security", "AI Training"],
                 "icon": "fas fa-dumbbell",
                 "links": [
                     {"label": "View on GitHub", "url": "https://github.com/mwill20/Python-Dojo", "class": "btn-primary"}
                 ]
            }
,
            {
                "title": "Bushido-Code",
                "description": "Progressive Python training system organized as nine belts of ten kata each, using disciplined repetition, spaced review, and structured recall.",
                "tech": ["Python", "Spaced Repetition"],
                "icon": "fas fa-user-ninja",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Bushido-Code", "class": "btn-primary"}
                ]
            },
            {
                "title": "Claude Masterclass Kit",
                "description": "Self-updating personal study library for Claude Code that turns course material and product news into short reviewed lessons, kept organized and ready to study.",
                "tech": ["PowerShell", "Knowledge Management"],
                "icon": "fas fa-graduation-cap",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/claude-masterclass-kit", "class": "btn-primary"}
                ]
            },
            {
                "title": "Codebase Detective",
                "description": "Timed exercise in systematically exploring, mapping, auditing, and documenting an unfamiliar codebase - the BackdoorBox research library - in under five hours.",
                "tech": ["Code Audit", "Documentation"],
                "icon": "fas fa-magnifying-glass",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/CodebaseDetective", "class": "btn-primary"}
                ]
            },
            {
                "title": "HealthTrack API",
                "description": "Patient vital-signs REST API built as the hands-on teaching project for a Claude Code Mastery course week, used to demonstrate multi-session agent workflows against one codebase.",
                "tech": ["Python", "REST API", "Teaching Project"],
                "icon": "fas fa-heart-pulse",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/HealthTrack-_API_AV", "class": "btn-primary"}
                ]
            },
            {
                "title": "SqueezeRadarAI",
                "description": "Market-data explorer that pulls price, RSI, short interest, and volume for a given ticker and ranks a watchlist of heavily shorted stocks by a composite score. Built as a data-analysis exercise, not investment advice.",
                "tech": ["Python", "Market Data", "Analysis"],
                "icon": "fas fa-magnifying-glass-chart",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Easy_Squeeze_AI", "class": "btn-primary"},
                    {"label": "Live Demo", "url": "https://huggingface.co/spaces/mwill-AImission/squeeze-radar-ai", "class": "btn-success"}
                ]
            },
            {
                "title": "Google News CLI",
                "description": "Interactive terminal client for Google News: fetch headlines, search queries, filter by topic, and open articles in the browser with arrow-key selection. Reads the public RSS feeds, so it needs no API key.",
                "tech": ["Node.js", "CLI", "RSS"],
                "icon": "fas fa-newspaper",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/google-news-cli", "class": "btn-primary"}
                ]
            }
        ]
    }
}
