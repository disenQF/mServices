# Tornado实现的微服务
## 1、基本使用

## 2. requests库测试
### 2.1 get
`  resp = requests.get(url, params={
       'wd': 'disen'
  })
  print(resp.text)`
  
### 2.2 post
 ` resp = requests.post(url, data={
     'wd': 'jack'
  })
  print(resp.text)`
  
### 3 跨域请求的前端代码
<pre>
        let options = {
            method: 'post',
            body: JSON.stringify({
                'name': 'disen',
                'pwd': '123444'
            }),
            headers: {
              'Content-Type': 'application/json'
            },
            mode: 'cors'
        };
        fetch('http://10.36.174.2:8000/user', options)
            .then(response=>response.json())
            .then(data=>{
                $('result').innerHTML = data.msg;
            })
 </pre>