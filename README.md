# SQLi-reproduction

1. 安裝 Flask 套件
   
   ```pip install Flask```
   
2. 執行程式

   ```python3 SQLi_reproduction.py```

3. 使用瀏覽器開啟以下連結

   ```http://127.0.0.1:5000```

4. 在 `Username` 輸入框輸入：`' OR 1=1;--`

5. 點擊 `Login` 按鈕就會看到登入成功，表示成功完成 SQLi 了
