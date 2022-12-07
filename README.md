#CSCI 6509 P07-Sentiment Analysis of Apple company

##The main code file is code-v1.ipynb
<p> the data processing we referred to several package documentation, such as pandas, matplotlib, seaborn.
     documentation of those package could be found at links below : </p>
<pre><code>
https://pandas.pydata.org/docs/user_guide/dsintro.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
https://seaborn.pydata.org/tutorial.html
</code></pre>
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





