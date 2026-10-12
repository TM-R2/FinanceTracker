# Finance Analyzer

Finance Analyzer is a personal finance application for analyzing bank account statements and transaction history.

The main goals of this project are:

- Import bank statements (starting with CSV exports)
- Automatically categorize transactions
- Visualize income and expenses
- Use AI and machine learning to improve transaction classification
- Demonstrate modern software engineering practices using Python, FastAPI, Docker, and CI/CD

---

## Architecture

Planned components:

- FastAPI Backend
- PostgreSQL Database
- Analytics Dashboard
- Transaction Categorization Service
- AI-powered Classification Engine

---

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend

- Plotly Dash / Streamlit (initial MVP)
- Future: React

### DevOps

- Docker
- Docker Compose
- GitHub Actions

### AI / Machine Learning

- Sentence Transformers
- Scikit-learn
- Custom Classification Models

---

## Project Status

### MVP

- [ ] Project Setup
- [ ] Data Model & PostgreSQL
- [ ] Bank CSV Import
- [ ] Transaction Management
- [ ] Categories
- [ ] Dashboard & Visualization
- [ ] GitHub Actions CI
- [ ] Docker Deployment

### ML

- [ ] Rule Engine & Normalization
- [ ] Embedding Service
- [ ] Transaction Classifier
- [ ] Human-in-the-Loop Feedback

### Production Ready

- [ ] Monitoring & Logging
- [ ] Security Hardening
- [ ] Open Banking Integration


---

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd finance-analyzer
```

Start the application:

```bash
docker compose up -d
```

Run the backend locally:

```bash
uvicorn app.main:app --reload
```

---

## Roadmap

### MVP

- Bank statement import
- PostgreSQL persistence
- Transaction management
- Financial dashboard
- Basic CI/CD

### AI Categorization

- Rule-based classification
- Embeddings
- Machine learning model
- User feedback loop

### Production Ready

- Monitoring
- Security improvements
- Open Banking integration
- Advanced analytics

---

## License

This project is licensed under the MIT License.
