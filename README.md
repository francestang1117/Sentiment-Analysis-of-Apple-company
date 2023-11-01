# CSCI 6509 P07-Sentiment Analysis of Apple company
## The details and the analysis of the project is in report.pdf
## The main code file is code.ipynb
<p> the data processing we referred to several package documentation, such as pandas, matplotlib, seaborn, sklearn.
     documentation of those package could be found at links below : </p>

<https://pandas.pydata.org/docs/user_guide/dsintro.html>. 

<https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html>. 

<https://seaborn.pydata.org/tutorial.html>

# Data visualization 
## boxplot
<p> most of methods at data visualization part are from the documentation of package seaborn, matplotlib, and pandas. the codes below are located at In [126], I referred some online solutions. The codes are modified based on our dataset and the style we want. The core part is I refer to the way to pivot dataset, so that I can have a stacked plot with three different categories. </p>
<p>code in our project</p>
<pre><code>
fig, ax=plt.subplots(figsize=(12,8))
df_stack = data4.pivot_table(index="year",
               columns="afinn_sentiment", 
               values="number",
               aggfunc=sum)
df_stack.plot.bar(stacked=True, ax=ax,color=['red', 'skyblue', 'green'])
plt.xlabel("Year", fontsize=10)
plt.ylabel("Number", fontsize=10)
plt.grid(False)
</code></pre>

<p>codes reference from online source, which can be found at:</p> 
<pre><code>
https://www.geeksforgeeks.org/how-to-create-boxplots-by-group-in-matplotlib/

fig, ax=plt.subplots(figsize=(15,8))

df_stack = df.pivot_table(index="Year",
               columns="Category", 
               values="Number",
               aggfunc=sum)
df_stack = df_stack.reindex(np.arange(2000, 2022))

df_stack.plot.bar(stacked=True, ax=ax)

plt.xlabel("Year", fontsize=15)
plt.ylabel("Number", fontsize=15)
</code></pre>

## Other figures
<p> The code of visualizations refers to the examples in the documents for the packages and some online websites. The link is below: </p>

<https://seaborn.pydata.org/generated/seaborn.histplot.html>. 

<https://github.com/amueller/word_cloud/tree/master/examples>.   

<https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html>.   

<https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/axhspan_demo.html#sphx-glr-gallery-subplots-axes-and-figures-axhspan-demo-py>.    

<https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html#sphx-glr-gallery-lines-bars-and-markers-timeline-py>.   

<https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html>

# Supervised learning approaches: Naive Bayes classifier and SVM
<p> The code of models refer to the links below: </p>

<https://scikit-learn.org/stable/modules/naive_bayes.html>    

<https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC>.      

<https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html>       

<https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html>       

<https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html>         

# Spearman correlation
<p> Spearman correlation implementation refers to the link below: </p>

<https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html>

# Lexicon-based approaches: VADER and AFINN
<p> Vader and Afinn implementation refers to the links below: </p>

<https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader>.  

<https://github.com/fnielsen/afinn>




