Naver Series
---
> 🙏sorry for about immature english

<h3>Installation</h3>

--- 
```
python3 -m pip install Naver-Series
```
[![](https://img.shields.io/badge/Pypi-link-green?style=for-the-badge)](https://pypi.org/project/Naver-Series/1.1.3.Beta/)

---

**option**

| Symbol | Description                                                                         |
|--------|-------------------------------------------------------------------------------------|
| *      | If this character is included, there is no need to use it. Or not contain the value |




<h3>1. search</h3>

***

**params**

| Name    | Type                      | Description |
|---------|---------------------------|-------------|
| keyword | str                       |             |
| *focus  | 'comic', 'novel', 'ebook' | sort type   | 
```py
#request example
import NaverSeries

NaverSeries.search('쇼미더', focus='comic')
```


**response**

| Name     | Type        |
|----------|-------------|
| contents | list\<dict> |


**contents**

| Name\<str> | Value-Type | Description            |
|------------|------------|------------------------|
| title      | str        | name of book           |
| id         | int        | id of book (productNo) |
| author     | list\<str> |  authors of book       |

```py
    #response example
    {
        'contents': 
            [
                {
                    'title': '쇼미더 엔터(총 201화/완결)',
                    'id': 4189091,
                    'author': ['베베꼬인']
                },
                
                {
                    'title': '쇼미더 엔터 [단행본](총 8권/완결)',
                    'id': 5332770,
                    'author': ['베베꼬인']
                }, 
                
                {
                    'title': '쇼미더럭키짱!(총 58화/미완결)',
                    'id': 6733269,
                    'author': ['김성모', '박태준']
                },
                
                {
                    'title': '쇼 미 더 스타크래프트 (스타크래프트로 배우는 군사·경제·정치)',
                    'id': 3430966,
                    'author': ['이성원 저']
                }
            ]
    }
```

<br>

<h3>2. get Info</h3>

***


**params**

| Name | Type | Description |
|------|-----|-------------|
| id   | int |  book id    |

```py
    #request example
    import NaverSeries
    
    book = NaverSeries.getInfo(5133669)
    print(book)
```

**response**

| Name\<str>     | Value-Type | Description         |
|----------------|------------|---------------------|
| title          | str        | name of book        |
| *description   | str        | description of book |
| img            | str        | thumbnail of book   |
| *total_episode | int        | size of all episode |
| *author        | list\<str> | authors of book     |
| rating         | float      | rating of book      |
| url            | str        | link of book        |

```py
#response example

    {
        'title': '전지적 독자 시점 [독점]',
        'description': "'이건 내가 아는 그 전개다'\n한순간에 세계가 멸망하고, 새로운 세상이 펼쳐졌다.\n오직 나만이 완주했던 소설 세계에서 평범했던 독자의 새로운 삶이 시작된다.",
        'img': 'https://comicthumb-phinf.pstatic.net/20200812_154/pocket_1597221311633UO5eI_JPEG/__1000x1500_v2.jpg?type=m260',
        'total_episode': 88,
        'author': ['슬리피-C', '싱숑', 'UMI'],
        'rating': 9.9,
        'url': 'https://series.naver.com/comic/detail.series?productNo=5133669'
    }

```