current python 3.9.13

## CREATE VENV 

```bash
python -m venv myenv
. myenv/bin/active
```

## INSTALL REQUIREMENTS

```bash
pip install -r requirements.txt
```

## START SERVER

```bash
uvicorn wsgi:app --reload
```

## RUN DOCKER 

```bash
docker run -p 8080:8080 nqcccccc/api-nude-detect 
```

## SAMPLE JQUERY

```js
var settings = {
  "url": "localhost:8000/nude-detect",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "img_urls":[
        "https://gaixinh.photo/wp-content/uploads/2021/12/hinh-anh-nguoi-dep.jpg",
        "https://xnxxx.to/wp-content/uploads/2020/10/31.jpg",
        "https://2sao.vietnamnetjsc.vn/images/2019/09/28/22/00/hotboy-02.jpg",
        "https://anh.24h.com.vn/upload/3-2015/images/2015-07-18/1437190628-1437120175-untitled-11.jpg",
        "https://vnn-imgs-f.vgcloud.vn/2022/02/15/17/ca-si-thieu-bao-trang-khoe-eo-thon-mong-cong-3.jpg",
        "https://t.vietgiaitri.com/2019/03/9/thieu-bao-tram-ban-gai-son-tung-dep-ruc-ro-va-su-that-ve-gia-the-b58.jpg",
        "http://9xlove.xyz/wp-content/uploads/2015/08/84.jpg"
      ]
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

PARAMS: img_urls -> array of images path

## SAMPLE RESPONSE

```bash
{
  "result": true, ## true if post request contains nude image(s) and false otherwise
  "nude_arr": [   ## contains nude image(s) name. empty if result is false
    "31.jpg",
    "84.jpg"
  ]
}
```