---
title: Regression Series
toc: true
layout: post 
hide: false 
categories: [machine learning]
---

## Background

Inspired by [chapter 4](https://github.com/chrismattmann/MLwithTensorFlow2ed/blob/master/ch04/Listing%204.01-4.06.ipynb) of [Chris Mattman's](https://scienceandtechnology.jpl.nasa.gov/dr-chris-mattmann) book [Machine Learning with Tensorflow 2nd Edition](https://www.manning.com/books/machine-learning-with-tensorflow). I followed along with his tutorial on using regression to model the call volume of [New York City's 311 service](https://www.kaggle.com/new-york-city/ny-311-service-requests). I attempted using a newer 2019 dataset than the 2014 one used in the book and was not able to reproduce the results well, which perplexed me and made we want to dig in deeper into regression, which I'd already explored some in [my interpolation tutorials]({{ site.baseurl }}/tutorial1/), however this time I want to dig in more to *iterative methods*, the kind made famous by deep learning and related techniques.

Rather than get bogged down in the implementation details of a single library I worked through a derived line fitting example using two different machine learning libraries: [Flux.jl](https://fluxml.ai/Flux.jl/stable/) and [Tensorflow 2](https://www.tensorflow.org/). Links to both of these tutorials can be found below:

- [Regression with Tensorflow 2]({{ site.baseurl }}/regression_tf2/)
- [Regression with Flux.jl]({{ site.baseurl }}/regression_flux/)

In both I'll assume you are familiar with the Vandermonde interpolation techniques, these were discussed in more detail in past posts: [Vandermonde Interpolation]({{ site.baseurl }}/tutorial1/)

Why not always use linear algebra type solutions? Vandermonde works great for small problems where the number of data instances is $N < 100$ or so. However when the number instances required number of monomial terms grows this Vandermonde matrix becomes large and cannot be inverted accurately. It's in these big data regime domains (especially in imaging!) that these iterative techniques have proven to be powerful and why I want to learn more! Enjoy these posts as I explore these libraries to get started with regression.
