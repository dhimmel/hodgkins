# Human disease network identifies a common genetic architecture between Hodgkin's lymphoma and autoimmune disease.


## Methods

We constructed a human disease network based on shared genetic susceptibility loci between complex diseases. We relied only on systematic GWAS data to avoid any knowledge bias when characterizing disease based on genetic association.

**Disease-associated loci**: Using an [existing implementation](https://dx.doi.org/10.15363/thinklab.d80), we extracted associations between diseases (in the Disease Ontology) and loci from the [GWAS Catalog](https://dx.doi.org/10.1093/nar/gkt1229). We included only high confidence associations by requiring a sample size of at least 1000 individuals and a p-value of at most 5×10<sup>-8</sup>. For each lead SNP, an LD-defined region containing the SNP (locus) was computed. Our approach assumes that the causal SNP lies within this region. Overlapping loci for the same disease were consolidated, yielding a total of 1,625 disease-loci associations ([`data/loci.tsv`](data/loci.tsv)). Diseases with fewer than 3 associated loci were excluded from further analysis.

**Disease categorization**: We manually classified diseases into three categories: Autoimmune, Solid Cancer, Hematologic Cancer ([`input/doid-categories.tsv`](input/doid-categories.tsv)).

**Disease similarity**: Next, we removed diseases without any loci overlap with other diseases leaving 82 diseases. Then, we computed the genetic similarity of all disease pairs ([`data/disease-similarity.tsv`](data/disease-similarity.tsv), [notebook](disease-similarities.ipynb)). Similarity was defined as the [weighted Dice coefficient](http://dl.acm.org/citation.cfm?id=972695.972699) between two locus sets. Commonly associated loci were downweighted: a locus received weight equal to the inverse squareroot of the number of overlapping loci. 433 disease pairs had non-zero genetic similarity (at least one overlapping locus). The similar pairs formed a single connected component containing all diseases.

**Disease proximity**: We calculated network proximities for all diseases pairs using a [random walk with restart](https://dx.doi.org/10.1145/1014052.1014135) ([notebook](master/walk.ipynb), [`data/proximities.tsv`](data/proximities.tsv)). A separate walk was performed for each disease, seeded by disease similarity. At every step until convergence, the walker restarted with probability equal to 0.2.

**Network visualization**: Since our similarity and proximity scores are not symmetric, we averaged the directed scores into a single undirected score per disease pair ([notebook](master/network.ipynb), [`data/network.tsv`](data/network.tsv)). We created a similarity network and a proximity network using scores as edge weights. We visualized the networks using a [Fruchterman-Reingold](https://dx.doi.org/10.1002/spe.4380211102) force-directed layout.



