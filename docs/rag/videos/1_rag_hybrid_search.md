<iframe
  width="500" 
  height="500" 
  src="https://www.youtube.com/embed/--EIpKnedMc"
  frameborder="0"
  allowfullscreen>
</iframe>

#### Why Production RAG Failed?

Failed becuase of chunking strategies, Instead of selecting the particular chunking strategy, pick the relevant chunk strategy based on the document type.

![alt text](./assets/1_rag.png)

#### How to fix

If the document mixup of the variable data format(text, table), need to use the sematic chunking. It dynmaically chunking based on the document's context.

If the documents updates need to update the embeddings on the specific chunk.

Need to handle metadata and use the citation

#### Retrieval Technique

Combine the result with BM25+vector along with Reciprocal Rank fusion technique.
