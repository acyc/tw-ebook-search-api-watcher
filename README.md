# tw-ebook-watcher

Just a simple script that would make the query and do the filtering based on the item in `watch-list`.
Use this on-demand or with scheduling such as cron.

####  Prerequisite

- A host with [TaiwanEbookSearch-API](https://github.com/Taiwan-Ebook-Lover/TaiwanEbookSearch-API) installed.
- create file named `watch-list`

#### Usage

```bash
python3 ebook-watcher.py [apiDomain]
```

- **apiDomain** is the domain name where `TaiwanEbookSearch-API` installed.

example:

```bash
python3 ebook-watcher.py http://localhost:7777
```

#### watch-list

- one line one item
- item is pipe-delimited 3 parts.
  - first part is code for book store, comma-delimited for more than 1 store
  - second part is the query keyword send to `TaiwanEbookSearch-API`
  - third part is the regular expression to filter through the response of `TaiwanEbookSearch-API`, currenly only look for title.
- check `watch-list.example` for example

#### output

Book URL comes with match found.

```
bash$ python3 ebook-watcher.py http://localhost:7777
================================================
search for: 咒術迴戰 http://localhost:7777/search?q=%E5%92%92%E8%A1%93%E8%BF%B4%E6%88%B0
filtering the book title with pattern: 咒術迴戰.*(12|13|14|夏去秋返)

match found @kobo
咒術迴戰 (12)
https://www.kobo.com/tw/zh/ebook/aSNQ2ZSQGDikVfI5ZbVk5w

================================================
search for: 憂國的莫里亞蒂 http://localhost:7777/search?q=%E6%86%82%E5%9C%8B%E7%9A%84%E8%8E%AB%E9%87%8C%E4%BA%9E%E8%92%82
filtering the book title with pattern: 憂國的莫里亞蒂.*(6|7|8)

match found @kobo
憂國的莫里亞蒂 (6)
https://www.kobo.com/tw/zh/ebook/UHADpkc-YDWFML7a9RTO6Q

================================================
```
