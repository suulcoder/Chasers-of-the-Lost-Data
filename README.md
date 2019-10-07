# Chasers-of-the-Lost-Data
The Challenge Help find ways to improve the performance of machine learning and predictive models by filling in gaps in the datasets prior to model training. This entails finding methods to computationally recover or approximate data that is missing due to sensor issues or signal noise that compromises experimental data collection. This work is inspired by data collection during additive manufacturing (AM) processes where sensors capture build characteristics in-situ, but it has applications across many NASA domains.

Background

The data are missing…….

Machine learning (ML) and artificial intelligence (AI) together have the potential to reshape how scientists and engineers use experimental data. Among the many valuable implementations of ML/AI, some examples include autonomy research to find previously undetectable patterns, to supplement or validate physics-based modeling, or otherwise to draw conclusions from very large datasets that would take humans months or even years to process.

A fundamental component of ML and data-driven modeling is having a comprehensive dataset, from which numerous, possibly even hundreds of features can be extracted. The model then “learns” through a process called training how to make predictions based on those features. Every ML algorithm requires vast amounts of data, with complex algorithms like neural networks often requiring thousands of records or observations in a dataset to properly train a model.

While there is great potential in using experimental data for ML/AI, one potential drawback is that experimental data is often compromised during the data collection process. Data collection is driven by sensors monitoring some system, and depending on the experimental environment or setup, those sensors can have limitations. Hardware can be unreliable, unmonitored sensors can fail, and signal noise is always a potential liability. One such example is current research into additive manufacturing (AM) process characterization for material science research. More commonly known as 3-D printing, AM is being explored as a cost-effective and efficient method for creating physical components for aeronautics. However, the in-situ sensor data collected during the AM also captures noise, thereby yielding incomplete datasets.

This issue limits the ability to use ML to predict structure characteristics and to model how parts may perform and therefore understand their structural integrity. Inspired by data loss in AM research with the goal of building accurate ML models, your challenge is to identify ways to computationally recover what is lost when datasets have gaps and excessive noise.

Potential Considerations

Researchers investigate a wide variety of scientific and engineering domains, so methods that can be applied to different types of data from different types of sensors are especially useful. Scientists and engineers also need to ensure that the methods they use in their work can be evaluated and validated by others, so understanding how your approach’s performance might be measured is also helpful. Potential ideas of applications could include (but are not limited to) imputation methods, matrix completion, and tensor completion.

Programming beginners are invited to create a method that can approximate missing data from datasets in Comma Separated Value (CSV) format. Intermediate and advanced programmers are invited to create methods to approximate the missing data and evaluate that method by building a ML model and describing the improvement in that model’s performance before and after the data recovery method was applied.

Listed below are some potential (but not required) additional considerations and recommendations. The challenge of handling missing data is something that confounds many researchers, but is especially critical for implementing machine learning approaches, which use data-driven models to make their predictions.

    Characteristics vary widely among different datasets; however, an approach that can be generalizable to many different applications would be particularly useful.
    Methods should consider mixed data (categorical and continuous data types).
    Source code and models should be open and free for reuse by the public.
    Code in popular open-source ML programming languages, such as Python or R, is useful.
    Code should include documentation on model parameters chosen, and why.
    Although test data for method development may include small datasets, consideration should be given to the feasibility of applications of those methods to large datasets (gigabytes or larger).

Example Resources

NASA data sets suitable for exploring missing data elements are provided in the resources. Each of these can be downloaded in CSV format, and each contains a mixture of categorical and continuous variables. Some amount of data is missing in each of these datasets.

Python libraries for imputation and matrix completion algorithms are provided below. These are examples, not meant to be an all-inclusive list of libraries available. Likewise, these are not the only techniques that can be explored for this problem. Participants are not bound to these libraries listed below and are encouraged to seek out the best possible method for developing their solutions.

    https://scikit-learn.org/stable/modules/impute.html
    https://pypi.org/project/impyute/
    https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html
    https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html

NASA in no way endorses any non-U.S. Government entity and is not responsible for information contained on non-U.S. Government websites.
