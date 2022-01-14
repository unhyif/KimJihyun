# My Movie Reviews

- 구현한 기능: 1 - 11
- 구현하지 못한 기능: X

---

## 🔥 Challenge 🔥

### Frontend

- Bootstrap 활용
- 별점 데이터 값에 따른 별 icon 출력

```Javascript
const rating = document.querySelectorAll(".stars");
rating.forEach((value) => {
  let ratingStars = "";
  for (let i = 0; i < Math.floor(value.innerText); i++) {
    ratingStars += '<i class="fas fa-star"></i>';
  }
  if (value.innerText % 1) {
    ratingStars += '<i class="fas fa-star-half"></i>';
  } // x.5점일 경우 half star icon 추가
  value.innerHTML = ratingStars;
});
```

### Backend

- 개봉년도, 장르, 별점 field에 `choices` 사용
- `@property decorator`를 통해 만든 분->시간 변환 메소드를 template에서 object의 property처럼 사용

```Python
# models.py
@property
    def minute_to_hour(self):
        h, m = "", ""
        if self.running_time//60:
            h = f"{self.running_time//60}시간 "
        if self.running_time%60:
            m = f"{self.running_time%60}분"
        return h+m
```

```Html
<span>{{review.minute_to_hour}}</span>
```
