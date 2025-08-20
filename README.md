#Google Dorking

1. Reads `domains.txt` (with lines like `*.example.com`).
2. Cleans each domain (remove the leading `*.` since Google dork someetimes doesn’t support wildcards in some conditions).
3. Groups them in batches of 10 domains.
4. Saves them into `dorks.txt`
5. For each batch, outputs a Google dork in the form:

```
(site:example1.com OR site:example2.com OR ... site:example10.com) inurl:"/web/guest/home" //change this for other dorks
```

<img width="612" height="153" alt="image" src="https://github.com/user-attachments/assets/b4d35f72-c3dd-4317-b6e3-4fd4fd9fd1a5" />
