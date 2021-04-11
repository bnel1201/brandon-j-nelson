---
title: Markdown publish, is there a better way to update links with Pandoc?
toc: true
layout: post 
hide: false
comments: true 
categories: [machine learning]
permalink: /markdown_publish/
---

## Problem statement

A key feature where Pandoc fit in was being able to save outs versions to html where I could more comfortably read and digest what I am trying to say as well as export to .docx word files to send to my advisers for the track changes features. Something that always bugged me is that when I export all of my markdown files to html or word, the links don't update, so when I am navigating around the html or word files and click a hyperlink I'm taken to the raw markdown file which breaks the flow.

This small Python package gives me the control to update those links to match my output file format so that when I'm reading my html notes and click on a link it takes me to the html version of that document. The package also has some specialty tweaks to manage working with word files which aren't always perfect when working with Pandoc.

I am still learning on how to better use Pandoc, I'm sure there is some filter, flag, or method to automatically update the links as I've done or fix the .docx issues I've had to work around but as a I learn more I'll update this package appropriately. And if there comes a point I don't need it anymore because I am able to fully utilize Pandoc this will be a good place to document that as well. Anyway, I've enjoy using Pandoc and writing with Markdown and found the scripts and module included here to help me out in the process!

You can check it out for yourself here: [markdown-publish](https://github.com/bnel1201/markdown-publish)

If you have better solutions, scripts, or better Pandoc tips please let me know in the comments below.
