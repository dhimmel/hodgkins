# Human disease network identifies a common genetic architecture between Hodgkin's lymphoma and autoimmune disease.


## Methods

We constructed a human disease network based on shared genetic susceptibility loci between complex diseases. We relied only on systematic GWAS data to avoid any knowledge bias when characterizing disease based on genetic association.

Using an [existing implementation](https://dx.doi.org/10.15363/thinklab.d80), we extracted associations between diseases (in the Disease Ontology) and loci from the [GWAS Catalog](https://dx.doi.org/10.1093/nar/gkt1229). We included only high confidence associations by requiring a sample size of at least 1000 individuals and a p-value of at most 5×10<sup>-8</sup>. For each lead SNP, an LD-defined region containing the SNP (locus) was computed. Our approach assumes that the causal SNP lies within this region. Overlapping loci for the same disease were consolidated, yielding a total of 1,625 disease-loci associations ([`data/loci.tsv`](data/loci.tsv)). Diseases with fewer than 3 associated loci were excluded from further analysis.

Next, we computed the genetic similarity of all disease pairs ([`data/disease-similarity.tsv`](data/disease-similarity.tsv), [notebook](disease-similarities.ipynb)). Similarity was defined as the [weighted Dice coefficient](http://dl.acm.org/citation.cfm?id=972695.972699) between two locus sets. Commonly associated loci were downweighted: a locus received weight equal to the inverse squareroot of the number of overlapping loci.
