# Human disease network identifies a common genetic architecture between Hodgkin's lymphoma and autoimmune disease.

## Methods

We constructed a human disease network based on shared genetic susceptibility loci between complex diseases. We relied only on systematic GWAS data to avoid any knowledge bias when characterizing disease based on genetic association.

**Disease-associated loci**: Using an [existing implementation](https://dx.doi.org/10.15363/thinklab.d80), we extracted associations between diseases (in the Disease Ontology) and loci from the [GWAS Catalog](https://dx.doi.org/10.1093/nar/gkt1229). We included only high confidence associations by requiring a sample size of at least 1000 individuals and a p-value of at most 5×10<sup>-8</sup>. For each lead SNP, an LD-defined region containing the SNP (locus) was computed. Our approach assumes that the causal SNP lies within this region. Overlapping loci for the same disease were consolidated, yielding a total of 1,625 disease-loci associations ([`data/loci.tsv`](data/loci.tsv)). Diseases with fewer than 3 associated loci were excluded from further analysis.

**Disease categorization**: We manually classified diseases into three categories: Autoimmune, Solid Cancer, Hematologic Cancer ([`input/doid-categories.tsv`](input/doid-categories.tsv)).

**Disease similarity**: Next, we removed diseases without any loci overlap with other diseases leaving 82 diseases. Then, we computed the genetic similarity of all disease pairs ([`data/disease-similarity.tsv`](data/disease-similarity.tsv), [notebook](disease-similarities.ipynb)). Similarity was defined as the [weighted Dice coefficient](http://dl.acm.org/citation.cfm?id=972695.972699) between two locus sets. Commonly associated loci were downweighted: a locus received weight equal to the inverse squareroot of the number of overlapping loci. 433 disease pairs had non-zero genetic similarity (at least one overlapping locus). The similar pairs formed a single connected component containing all diseases.

**Disease proximity**: We calculated network proximities for all diseases pairs using a [random walk with restart](https://dx.doi.org/10.1145/1014052.1014135) ([notebook](walk.ipynb), [`data/proximities.tsv`](data/proximities.tsv)). A separate walk was performed for each disease, seeded by disease similarity. At every step until convergence, the walker restarted with probability equal to 0.2.

**Network visualization**: Since our similarity and proximity scores are not symmetric, we averaged the directed scores into a single undirected score per disease pair ([notebook](network.ipynb), [`data/network.tsv`](data/network.tsv), [browser](http://htmlpreview.github.io/?https://github.com/dhimmel/hodgkins/blob/master/tables.html)). We created a similarity network and a proximity network using scores as edge weights. We visualized the networks using a [Fruchterman-Reingold](https://dx.doi.org/10.1002/spe.4380211102) force-directed layout.

## Results

Both the similarity and proximity networks displayed distint autoimmune and solid cancer clusters. This finding supports the hypothesis that genetic associations provide insight into disease pathophysiology. For example, the tight clustering displayed by autoimmune diseases suggests their etiology is primarily immune and that the site of their pathologic manifestation is secondary.

The network includes three hematologic cancers. Hodgkin's lymphoma (HL) is separated from the solid cancer cluster and instead placed with autoimmune diseases. Alternatively, multiple myeloma (MM) clusters with solid cancers. These findings are preliminary due to the small number of associated loci: 7 for HL, 5 for MM. Chronic lymphocytic leukemia (CLL), which has 27 loci, shared genetic etiology with both autoimmune diseases and solid cancers and was located between the two clusters in the network.

![Hodgkin's lymphoma clusters with autoimmune diseases rather than solid cancers in a genetic proximity network](figure/proximity-network.png?raw=true "Proximity network. Autoimmune diseases are purple and solid cancers are orange.")
**Figure 1: Disease proximity network shows Hodgkin's lymphoma as genetically related to autoimmune disease rather than solid cancer.**

![Proximities to autoimmune diseases and solid cancers for each disease](figure/disease-proximities.png?raw=true "Pairwise disease proximities")
**Figure 2: Proximities to autoimmune diseases and solid cancers for each disease.** Each panel shows the proximity from its titled disease to other diseases. Proximities are only displayed for autoimmune diseases, solid cancers, and Hodgkin's lymphoma. Higher proximities indicate greater relatedness. The *p*-value indicates whether the mean proximity to autoimmune diseases (including MS, excluding HL) was different than the mean proximity to solid cancers. 

![Proximity distributions between disease categories](figure/pairwise-proximities.png?raw=true "The *p*-value" reports a difference in means of the two distributions.)
**Figure 3: Proximity distributions between disease categories.** Distributions are plotted for all proximities between diseases of the titled category and diseases of the colored category. The *p*-values indicate whether the mean proximity to autoimmune diseases differed from the mean proximity to solid cancers. The top panel shows autoimmune diseases were more related to other autoimmune diseases than solid cancers. The bottom panel shows solid cancers were more related to other solid cancers than autoimmune diseases. The middle panel shows that, in aggregate, hematologic cancers were related to both autoimmune diseases and solid cancers.

![Proximities to autoimmune diseases and solid cancers for MS and HL](figure/ms-hl-dotplot.png?raw=true "Proximities to autoimmune diseases and solid cancers for MS and HL")
**Figure 4: Proximities to autoimmune diseases and solid cancers for MS and HL.** As expected, MS was more related to autoimmune diseases than solid cancers. Similarly, Hodgkin's lymphoma was also more related to autoimmune diseases than solid cancers.

## Execution

This analysis can be reproduced by running the notebooks in the following order:

1. `disease-similarities.ipynb`
2. `walk.ipynb`
3. `plotting.ipynb`
3. `network.ipynb`
