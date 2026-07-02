### **HNSW**

**HNSW** (**Hierarchical Navigable Small World**) is a high-performance algorithm for **approximate nearest neighbor (ANN)** search. It’s widely used in vector databases and embeddings-based retrieval systems (e.g., Pinecone, FAISS, Milvus, Vespa).

---

### 🔍 What HNSW

HNSW is a **graph-based index** that organizes vectors into multiple layers of _small-world graphs_. This structure allows very fast navigation toward the nearest neighbors of a query vector.

---

### 🚀 Why It’s Fast

HNSW builds a hierarchy:

- **Upper layers:** sparse graph → fast, coarse navigation
- **Lower layers:** dense graph → fine-grained search
  A query starts at the top layer and greedily moves to closer nodes as it descends.  
  This drastically reduces search time while keeping high recall.[[Recall Vs Precision]].

---

### 🧠 Key Concepts

#### 1. **Small-World Graph**

Each node (vector) links to neighbors such that:

- Local connections keep navigation accurate
- Long-range connections keep navigation fast

#### 2. **Greedy Search**

At each layer, the algorithm moves to the neighbor closest to the query until no better neighbor exists.

#### 3. **Layers**

Each vector is assigned a random "level":

- Higher levels → fewer nodes
- Level 0 → contains all vectors

#### 4. **ef and M Parameters**

- **M**: max number of neighbors per node (controls graph degree, affects memory and speed)
- **efConstruction**: accuracy–speed tradeoff during building
- **efSearch**: accuracy–speed tradeoff during querying  
  Higher values → better recall, slower runtime.

---

### Performance Characteristics

- **Time complexity (query):** ~O(log n)
- **Build time:** relatively expensive but often worth it
- **Memory use:** higher than tree-based methods (due to graph edges)

---

### Typical Use Cases

- Semantic search with embeddings
- Recommendation systems
- Image, audio, or video similarity search
- Large vector databases (millions to billions of vectors)

---

### Tools That Use HNSW

- **FAISS** (Facebook/Meta)
- **hnswlib**
- **Pinecone**
- **Milvus**
- **Weaviate**
- **Elasticsearch / OpenSearch (k-NN plugin)**

---
