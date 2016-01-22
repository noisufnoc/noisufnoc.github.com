Date: 2016-01-22
Title: Pelican Power!
Tags: blog, pelican, python
Category: blog
Author: Mike

![pelican power suit](http://i.imgur.com/MyYkRgnl.png "Pelican Power Suit")

I can't guarantee that I'm going to blog all that often, but I've decided to dust this domain off and put out a little bit of content.  I am using [Pelican](http://blog.getpelican.com/), which is a [Python](https://www.python.org/) based static blog generator, and since everything is flat files I am able to host it on my [GitHub](https://github.com/noisufnoc/)

This post, in part is to remind me how to actually publish to GitHub.  I haddn't touched this site in over two years, and couldn't rember the commands I was using to build things so that GitHub pages would serve them up.  After some serious grepping through my bookmarks, I was able to find the original blogger that gave me the info for getting started with Pelican.  [Alex Clark's Blog](http://blog.aclark.net//2012/09/21/yes-this-blog-is-now-powered-by-pelican/) has some great information for customizing Pelican to run on GitHub pages.  Most importantly, this set of commands to make the blog and commit it.

```
# make publish; git commit -a -m "Super descriptive commit message"; git push
```

Don't forget to add any new files that aren't initially tracked by git.

That's all for now, please forgive any misspellings.  Since Pelican uses MarkDown, I'm just writing this entry in vim.  Perhaps I can get the vimspell plugin working...and blog about it later.
