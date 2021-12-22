Naver Series
---
> 🙏sorry for about immature english

<h3>1. search</h3>

***

**params**

| Name    | Type |
|---------|------|
| keyword | str  |
```py
#request example
import NaverSeries

NaverSeries.search('쇼미더')
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
