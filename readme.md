## What is this?
For blogs that run on jekyll, all the posts need some informations, such as the title, and the time when it's created of the post.  
Therefore, everytime you write your post, you have to write down the informations of your post based on the format. EVERYTIME. Which sucks.  
So with this markdown maker script, you can make your formatted post file for your jekyll blog.

## How to use it?
1. Download the script, md_maker.py to your computer.  
2. Go to the directory where you want to make your post.
3. Execute the md_maker.py script with python3. Like:
```bash
python3 md_maker.py <mode> <simple file name>
```

## What kind of modes that I can choose?
- a
  - automatically sets the time based on your computer time.
- m
  - you can manually set the time by the following questions after you execute the script.

## Wait, what is the `simple file name?`
Jekyll posts have this kind of format to all of their posts.
`{date_year}-{date_month}-{date_day}-{simple_filename}.md`  
Now you got it? You don't have to type the time informations and the filename extension, which is the `.md`.

So, this is an example which creates a post which time is current time, with a simple file name "test_post"  
```bash
python3 -a test_post
```
Then, you'll get a file with the name of `{date_year}-{date_month}-{date_day}-test_post.md`.
