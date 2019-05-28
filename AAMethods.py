""" Katie Lunceford and Jon Li
"""

class AAMethods:
"""
    Chapter 3 discusses how languages can be modeled mathematically, and there
have been several different models suggested to map languages. Languages can be
broken down into events, and these events will have certain regularities.
However, it is common and frustrating when language use deviates from these
regularities. For example, grammatical structures are some of these
regularities. One way to look at languages is through distributions of the
frequencies of words. The most commonly accepted of these distributions is the
Zipf distribution. Words with similar frequencies tend to share common
attributes, such as more common words tend to be shorter and less specific in
meaning. Distributional variations can often be very telling of authorship.
There are many different ways to measure how reliable certain cues or texts are.
One measure of this is the level of entropy. Texts with more entropy are more
unpredictable. It is also to examine cross-entropy, which is the degree to which
a text differs from an inferred distribution. Kolmogorov Complexity is another
way to measure the predictability of a text, measuring the smallest possible
algorithm needed to describe the text, but it is not always attainable. Matrices
and vector spaces as vectors can describe a large number of measurements, but it
can be problematic when the dimensions get too large. Finally, there are three
phases to authorship attribution: canonicization (treating similar realizations
as identical to create a finite set), determination of the event set (partioning
the input-stream into non-overlapping events), and statistical inference (used
to determine final results).
    Chapter 5 details some specific methods that are used for authorship
attribution analysis. The two main types of analysis are unsupervised analysis
and super analysis. Unsupervised analysis does to assume any attributes of the
input from the start. Instead it simply looks for patterns within the data. PCA,
a method of describing variance within the data, can show the closeness between
separate data items. Data items that are closer are more likely to be written by
the same author. Another example of unsupervised analysis is MDS, which
calculates differences as distances through multidimensional scaling. Cluster
analysis assumes a distance between the data items and groups them into the
closest pairs. On the other hand, supervised analysis requires some information
about the documents before analysis. The basic form of supervised analysis is
using simple statistics to see how language use differs between texts. Although
alone these simple tests are not overly accurate, they can be combined to create
more advanced tests that are more accurate. Another example of supervised
learning is LDA, which is similar to PCA but uses categorized data to infer
differences along the categories. Distance-based methods use vector spaces.
General machine learning techniques include neural networks, decision trees, and
naïve Bayes classifiers. Finally, there are support vector machines, which are
a relatively new and mathematically advanced topic. Overall, the chapter details
the benefits and pitfalls of each of the different methods. Each method has its
benefits but has also been shown to be unreliable when examining certain types
of data.

This class never actually ended up getting used in our final project
"""
    pass
