PROJECT NAME : Lyric Search Engine

project description:
	Users often find themselves with fragments of song lyrics lingering in their minds, yearning to retrieve the complete set of lyrics. Our solution employs a sophisticated retrieval model to address this issue. When users provide a query consisting of fragmented lyrics, our Vector Space Model (VSM) comes into play. By leveraging VSM, we recommend a curated list of song lyrics that closely match the user's input, enabling them to effortlessly locate the desired lyrics and complete the musical puzzle.

Group members:
	1.SAI SWETHA M   --> S20200010143
	2.HESHVITHA M    --> S20200010138
    
Project Drive Link:

https://github.com/SaiSwetha-0902/LyricFinder
    
How to run:
  1.unzip the file
  2.go to the current folder (source code)
  3.type on console : python main.py
  
Components:

1. *Document Indexing:*
   In this phase, we compile a comprehensive dictionary of all unique words across documents. The dictionary includes keys for each word and posting lists containing document IDs along with word frequencies within those documents.

2. *Query Retrieval:*
   Through the calculation of term frequency (tf) and inverse document frequency (idf), we assign weights to each document, forming vectors. Simultaneously, we create a vector for the user's query. Using cosine similarity, we assess the similarity between the query vector and each document vector. The documents are then ranked, and the top 10 are presented to the user.

3. *Filtered Searches:*
   a. Genre-Based Search:
      Searches are conducted based on document genres. If the user specifies a genre, we return the top 10 documents associated with both the entered genre and their similarity scores.

   b. Artist-Based Search:
      Searches are performed based on artist names. If the user provides an artist's name, we retrieve documents related to that artist.

4. *Feedback-driven Refinement:*
   Leveraging relevance feedback from users, we enhance the query using the Rocchio algorithm. The updated query is employed to calculate cosine similarity against each document, and the top 10 documents are then returned.

5. *Performance Evaluation:*
   Key performance metrics, including Precision, Recall, and Average Precision, are computed. Additionally, a graphical representation illustrating the Precision-Recall trade-off offers a comprehensive assessment of the retrieval model's effectiveness.


Contribution:
	
     1. SAI SWETHA M                    --> Indexing,Refining Search based on artist name,
                                            Capturing Feedback (using Rocchio Algorithm)
     2. HESHVITHA M                     --> Searching,Refining Search based on genre,Assessment
                                            component

#
