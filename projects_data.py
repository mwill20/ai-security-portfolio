
projects = {
    "mcp": {
        "title": "MCP Ecosystem",
        "icon": "fas fa-cogs",
        "description": "The Model Context Protocol (MCP) is a scalable framework designed to enable modular AI Agents and tools to communicate and collaborate seamlessly. My ecosystem includes core servers and diverse agents.",
        "projects": [
             {
                "title": "MCP Core Server",
                "description": "Central Python server hosting AI models and exposing them via MCP. Provides a unified interface for AI services and manages communication between different components in the ecosystem.",
                "icon": "fas fa-server",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/mcp-tools", "class": "btn-primary"}
                ]
            },
            {
                "title": "Unified Demo Interface",
                "description": "Access all tools through a single interface.",
                "icon": "fas fa-desktop",
                "links": [
                    {"label": "Try Live Demo", "url": "#", "class": "btn-primary"}
                ]
            },
            {
                "title": "Calculator Tool",
                "description": "Advanced calculator tool with support for complex mathematical operations and unit conversions.",
                "icon": "fas fa-calculator",
                "links": [
                    {"label": "Try Demo", "url": "#", "class": "btn-primary"}
                ]
            },
            {
                "title": "Sentiment Analysis Tool",
                "description": "Analyze the sentiment of text using advanced NLP models. Supports multiple languages and provides confidence scores.",
                "icon": "fas fa-smile",
                "links": [
                    {"label": "Try Demo", "url": "#", "class": "btn-primary"}
                ]
            },
            {
                "title": "Weather Tool",
                "description": "Get current weather conditions and forecasts for any location worldwide. Includes detailed metrics and weather alerts.",
                "icon": "fas fa-cloud-sun",
                "links": [
                    {"label": "Try Demo", "url": "#", "class": "btn-primary"}
                ]
            },
            {
                "title": "TypeScript MCP Agent",
                "description": "Lightweight TypeScript agent with web automation capabilities. Connects to the MCP Core Server to perform tasks and process information.",
                "icon": "fab fa-js",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/mcp-tiny-agent", "class": "btn-primary"}
                ]
            },
             {
                "title": "Productivity Agent",
                "description": "Automates Windows tasks, analyzes system logs using AI, and helps manage your digital workspace efficiently.",
                "icon": "fas fa-robot",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/PersonalProductivityAgent", "class": "btn-primary"}
                ]
            }
        ]
    },
    "security": {
        "title": "Security",
        "icon": "fas fa-shield-alt",
        "projects": [
            {
                "title": "SecureCLI-Tuner",
                "description": "Security-first LLM fine-tuned for Agentic DevOps that translates natural language into safe, valid Bash commands while achieving a 100% adversarial attack blocking rate. Implements a \"Defense in Depth\" architecture with sanitized QLoRA fine-tuning and three-layer runtime guardrail system.",
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
                    {"label": "View Project", "url": "/sagevault", "class": "btn-primary"},
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/SageVault", "class": "btn-secondary"}
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
                "title": "Smart Security Camera",
                "description": "An intelligent security system with face detection and motion tracking, built with Python and OpenCV.",
                "icon": "fas fa-server",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/smart-security-camera", "class": "btn-primary"}]
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
                "badge": "Publication",
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
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Trust-Bench-SecureEval-Ops", "class": "btn-primary"}
                ]
            },
            {
                "title": "Trust Bench Demo",
                "description": "A LangGraph-based multi-agent workflow that inspects software repositories for security leaks, code quality gaps, and documentation health. Features a collaborative system of specialized agents working together to provide comprehensive repository analysis.",
                "badge": "Demo",
                "tech": ["Python", "LangGraph", "Multi-Agent Systems", "Security Analysis"],
                "icon": "fas fa-laptop-code",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Trust_Bench", "class": "btn-primary"},
                    {"label": "Watch Demo", "url": "https://1drv.ms/v/c/2c8c41c39e8a63cb/EQil7I1iewdEuzPdQGBqVOYBHaRg9tBcyogZvmKUXKFLyw?e=8Dl8P5", "class": "btn-secondary"}
                ]
            }
        ]
    },
    "ml": {
        "title": "ML Engineering",
        "icon": "fas fa-cogs",
        "projects": [
            {
                "title": "HuggingFace Sentiment Analysis",
                "description": "A Neural Network for emotion detection in text using PyTorch and the HuggingFace Transformers library.",
                "icon": "fas fa-tools",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/HuggingFace-Sentiment-Analysis", "class": "btn-primary"}]
            },
            {
                "title": "XGBoost Regressor",
                "description": "Advanced regression analysis using the XGBoost algorithm, including feature importance and model evaluation.",
                "icon": "fas fa-chart-candlestick",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/XGBoost-Regressor", "class": "btn-primary"}]
            },
            {
                "title": "Bank Churn Neural Network",
                "description": "Predicting customer churn using a neural network model built with TensorFlow/Keras, helping banks identify at-risk customers.",
                "icon": "fas fa-network-wired",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/Bank_Churn_NN", "class": "btn-primary"}]
            },
            {
                "title": "Visa Approval Prediction",
                "description": "Machine learning model using XGBoost to predict visa approval outcomes based on applicant data and historical patterns.",
                "icon": "fas fa-passport",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/XGBoost_Visa_Approval_Prediction", "class": "btn-primary"}]
            },
            {
                "title": "Loan Acceptance Predictor",
                "description": "Decision tree model for predicting loan approval decisions, including feature importance analysis and model interpretation.",
                "icon": "fas fa-hand-holding-usd",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/Loan_Acceptance_DecisionTree", "class": "btn-primary"}]
            },
            {
                "title": "FoodHub Data Analysis",
                "description": "Comprehensive analysis of FoodHub's food delivery data, including customer behavior, order patterns, and restaurant performance metrics.",
                "icon": "fas fa-utensils",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/FoodHub-Data-Analysis", "class": "btn-primary"}]
            },
             {
                "title": "NLP RAG Medical Assistant",
                "description": "Retrieval-Augmented Generation (RAG) system for medical information retrieval and question answering using NLP and vector databases.",
                "icon": "fas fa-user-md",
                "links": [{"label": "View on GitHub", "url": "https://github.com/mwill20/NLP_RAG_Medical_Assistant", "class": "btn-primary"}]
            },
            {
                "title": "SuperKart Sales Forecasting",
                "description": "End-to-end machine learning solution for retail sales prediction. Features include data preprocessing, feature engineering, and model deployment with FastAPI.",
                "icon": "fas fa-chart-line",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Model-Deployment", "class": "btn-primary"},
                    {"label": "Live Demo", "url": "https://huggingface.co/spaces/mwill-AImission/superkart-sales-forecast-frontend", "class": "btn-secondary"}
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
        ]

    },
    "fun": {
        "title": "Just for Fun",
        "icon": "fas fa-gamepad",
        "projects": [
            {
                 "title": "Python-Dojo – Security Reps Playground v1",
                 "description": "A playful security \"gym\" for AI engineers to build muscle memory around sanitization, API management, and guardrail patterns using a Mastery Loop training engine.",
                 "tech": ["React", "Security", "AI Training"],
                 "icon": "fas fa-dumbbell",
                 "links": [
                     {"label": "Live Demo", "url": "#", "class": "btn-primary"},
                     {"label": "View on GitHub", "url": "#", "class": "btn-secondary"}
                 ]
            },
            {
                "title": "SqueezeRadarAI 🚀",
                "description": "A simple yet powerful tool for identifying potential short squeeze opportunities in the stock market.",
                "tech": ["Python", "Gradio", "yfinance", "Stock Analysis"],
                "icon": "fas fa-chart-line",
                "links": [
                    {"label": "View on GitHub", "url": "https://github.com/mwill20/Easy_Squeeze_AI", "class": "btn-primary"},
                    {"label": "Try Live Demo", "url": "https://huggingface.co/spaces/mwill-AImission/squeeze-radar-ai", "class": "btn-secondary"}
                ]
            }
        ]
    }
}
