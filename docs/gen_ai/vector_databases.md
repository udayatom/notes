**Vector Databases**

Traditional databases search exact values:

```sql
SELECT * FROM documents
WHERE title = 'Machine Learning'
```

Vector databases search by semantic similarity.

Example:

Query:

"How can I improve my neural network?"

Vector DB can retrieve documents containing:

Deep learning optimization
Hyperparameter tuning
Training strategies

even if the exact words don't match.

**2. Embeddings (Most Important Concept)**

    A vector database stores embeddings, not raw text.

    What is an Embedding?

    An embedding is a numerical representation of text.

        Example:

        "Cat" → [0.23, -0.45, 0.89, ...]
        "Kitten" → [0.21, -0.41, 0.92, ...]

    Similar meanings produce vectors that are close together.

Learn:

- Text embeddings
- Sentence embeddings
- Dense vectors
- Embedding dimensions

Popular embedding models:

- OpenAI Embeddings
- Sentence Transformers
- Cohere Embeddings

**3. Vector Similarity Search**

    After converting text into vectors, we compare them.

    Common similarity metrics:

    Cosine Similarity

    Most common.

        1 = identical
        0 = unrelated
       -1 = opposite

**Euclidean Distance** - Measures geometric distance.

**Dot Product** - Often used in optimized systems.

    Interview Question:

    Why is cosine similarity preferred for embeddings?

    Answer:
    Because direction matters more than magnitude.

**4. Vector Database Architecture**

    Basic flow:

        Documents
        ↓
        Chunking
        ↓
        Embedding Model
        ↓
        Vector Creation
        ↓
        Vector Database
        ↓
        Similarity Search
        ↓
        LLM

This is the foundation of RAG.

**5. Chunking Strategies**

    LLMs cannot embed huge documents efficiently.

    Split documents into chunks.

        Fixed Chunking
        500 characters
        100 overlap
        Recursive Chunking

    Split by:

        Paragraph
        Sentence
        Word
        Semantic Chunking

    Split based on meaning.

    Learn:

        Chunk size
        Chunk overlap
        Context window

    Important interview question:

    Why does chunk size affect retrieval quality?

**6. Metadata Filtering**

    Store additional information.

    Example:

        {
        "document": "AI Notes",
        "department": "Engineering",
        "year": 2025
        }

        Search:

        Find AI notes
        WHERE year = 2025

    Vector search + metadata filtering = powerful retrieval.

**7. Indexing**

Without indexes:

Search all vectors

Too slow for millions of records.

Common indexing algorithms:

[HNSW](/gen_ai/hnsw.md)-(Hierarchical Navigable Small World)

Most popular.

IVF

Inverted File Index

PQ

Product Quantization

Used for compression.

Must understand:

Exact search
Approximate Nearest Neighbor (ANN)
Recall vs Speed tradeoff

**8. Nearest Neighbor Search**

Goal:

    Query Vector
    ↓
    Find Top-K Similar Vectors

Example:

    Top 5 documents
    Top 10 chunks

Important terms:

- KNN
- ANN
- Top-K Retrieval

**9. RAG (Retrieval Augmented Generation)**

The most common Vector DB use case.

Flow:

        User Question
        ↓
        Embedding
        ↓
        Vector Search
        ↓
        Relevant Documents
        ↓
        Prompt Construction
        ↓
        LLM Response

Learn:

Naive RAG
Advanced RAG
Hybrid Search
Agentic RAG

**10. Hybrid Search**

    Combine:

    Vector Search

    - Keyword Search

    Example:

    User searches:

    AWS EC2 pricing

    Keyword matching may matter more than semantics.

    Popular combination:

    BM25 + Vector Search

    Learn:

    - Sparse embeddings
    - Dense embeddings
    - Hybrid retrieval

**11. Re-ranking**

    After retrieval:

        Top 50 documents

    Use a reranker model:

        Top 50
        ↓
        Top 5

    Improves answer quality significantly.

    Popular rerankers:

    - Cohere Rerank
    - Cross Encoders (Sentence Transformers)

**12. Popular Vector Databases**

Managed - Pinecone - Weaviate - Qdrant
Open Source - Milvus - ChromaDB - FAISS

For learning: - ChromaDB - FAISS - Qdrant

**13. Evaluation Metrics**

How do you know retrieval is good?

Learn:

**Precision** - Relevant results returned.

**Recall** - How many relevant results were found.

**MRR** - Mean Reciprocal Rank.

**NDCG** - Ranking quality metric.

Important in production RAG systems.

**14. Production Concepts**

    Data Ingestion Pipeline
        PDF
        DOCX
        HTML
        Database
        API
    Incremental Updates- Add new vectors without rebuilding everything.

    Deduplication - Avoid duplicate chunks.

    Versioning - Track embedding model versions.

**15. Scaling Concepts**

For enterprise projects learn:

    - Sharding
    - Replication
    - Distributed Vector Search
    - Multi-tenancy
    - Caching
    - Latency optimization

**16. Security Concepts**

Important for enterprise GenAI:

Row-level security
Metadata access control
Encryption at rest
Encryption in transit
Tenant isolation

17. End-to-End GenAI Architecture
    User
    ↓
    Frontend
    ↓
    API
    ↓
    Embedding Model
    ↓
    Vector DB
    ↓
    Retriever
    ↓
    Reranker
    ↓
    Prompt Builder
    ↓
    LLM
    ↓
    Response
    Must-Learn Topics (80/20 Rule)

Focus on these first:

✅ Embeddings

✅ Cosine Similarity

✅ Chunking

✅ Vector Search

✅ Metadata Filtering

✅ ANN / HNSW

✅ RAG Architecture

✅ Hybrid Search

✅ Re-ranking

✅ Vector DBs (FAISS, ChromaDB, Qdrant)

Suggested Learning Order (1 Week)

Day 1

Embeddings
Vector representations
Similarity metrics

Day 2

Chunking
Metadata
Retrieval

Day 3

FAISS basics
ChromaDB basics

Day 4

RAG architecture

Day 5

Hybrid Search
Reranking

Day 6

Qdrant or Pinecone

Day 7

Build a PDF Q&A chatbot using RAG
