````markdown
# 🌤️ Weather Dashboard

**English | [Tiếng Việt](#-bảng-điều-khiển-thời-tiết)**

A beautiful weather dashboard application that fetches real-time weather data from OpenWeatherMap API using Python and Tkinter.

## ✨ Features

- 🌍 **Real-time Weather Data** - Fetch current weather from any city worldwide
- 📍 **City Search** - Search weather by city name
- 🌡️ **Current Weather Display** - Temperature, feels like, weather description
- 📊 **Detailed Metrics** - Humidity, wind speed, pressure, visibility, UV index
- 📅 **5-Day Forecast** - View weather predictions for the next 5 days
- 🎨 **Dark Theme UI** - Modern, easy-on-the-eyes interface
- ⚡ **Fast API Integration** - Real-time data updates with timeout handling
- 🔄 **Auto-load** - Loads default city (Hanoi) on startup
- 📱 **Responsive Design** - Clean and organized layout

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Internet connection (for API calls)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sonviplm1-ops/english-game.git
   cd english-game
   ```

2. **Install dependencies**
   ```bash
   pip install requests pillow
   ```

3. **Run the application**
   ```bash
   python weather_dashboard.py
   ```

## 📖 Usage Guide

### Searching for Weather
1. Enter a city name in the search field
2. Press **Enter** or click **Search** button
3. Current weather and 5-day forecast will be displayed

### Understanding the Display

#### Current Weather Section
- **City Name** - Location and country code
- **Temperature** - Current temperature in Celsius
- **Description** - Weather condition (e.g., "Partly Cloudy")
- **Feels Like** - Perceived temperature
- **Humidity** - Moisture level in percentage
- **Wind Speed** - Wind velocity in m/s
- **Pressure** - Atmospheric pressure in hPa
- **Visibility** - Visibility distance in km
- **UV Index** - Ultraviolet radiation level

#### 5-Day Forecast
- Daily forecast cards showing:
  - Day of week and date
  - High temperature
  - Weather condition
  - Humidity level

### Keyboard Shortcuts
- **Enter** - Search for city weather

## 🔑 API Configuration

The application uses OpenWeatherMap free API with a default key. For production use:

1. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Edit `weather_dashboard.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

### Free vs Paid Plans
- **Free Plan**: Current weather and 5-day forecast (Sufficient for this app)
- **Paid Plan**: Extended forecasts, historical data, more API calls

## 🎨 UI Components

- **Header** - Dark blue banner with title and search bar
- **Current Weather Panel** - Large display of current conditions
- **Details Grid** - 3-column layout showing key metrics
- **Forecast Cards** - 5 cards showing daily predictions
- **Status Bar** - Shows last update time and status messages

## 📊 Weather Data Format

The application fetches data from OpenWeatherMap API in JSON format:

```json
{
  "name": "Hanoi",
  "sys": {"country": "VN"},
  "main": {
    "temp": 28.5,
    "feels_like": 32.1,
    "humidity": 75,
    "pressure": 1013
  },
  "weather": [{"main": "Clouds", "description": "overcast clouds"}],
  "wind": {"speed": 5.2},
  "visibility": 10000
}
```

## 🔧 Customization

### Change Temperature Units
Modify the API call in `search_weather()`:
```python
# Change metric to imperial for Fahrenheit
current_url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=imperial"
```

### Change Default City
Edit the last lines:
```python
root.after(500, lambda: app.city_entry.insert(0, "Tokyo") or app.search_weather())
```

### Change Colors
Edit color codes in `setup_ui()`:
- `#0d47a1` - Header background
- `#2a2a2a` - Content background
- `#FFD700` - Highlighted text (Gold)
- `#87CEEB` - Secondary text (Sky Blue)

## 📁 Project Structure

```
english-game/
├── weather_dashboard.py    # Main Weather Dashboard application
├── WEATHER_README.md       # This file
├── requirements.txt        # Updated with requests and pillow
└── ...
```

## 🐛 Troubleshooting

### "City not found" error
- Check spelling of city name
- Use English city names
- Try with country code (e.g., "London, UK")

### Connection timeout
- Check internet connection
- Verify API service is available
- Try again after a few seconds

### Weather data not updating
- Ensure API key is valid
- Check if API call limit is reached (free tier: 60 calls/minute)
- Verify city name is correct

### Blank forecast cards
- API might be slow to respond
- Try searching again
- Check if forecast data is available for the city

## 🌐 API Rate Limits

**Free Plan:**
- 60 API calls per minute
- 1,000,000 API calls per month
- Data update frequency: Every 10 minutes

## 📝 Weather Conditions

The API supports various weather conditions:
- Clear
- Clouds
- Drizzle
- Rain
- Thunderstorm
- Snow
- Mist
- Smoke
- Haze
- Dust
- Fog
- Sand
- Ash
- Squall
- Tornado

## 🚀 Future Enhancements

- Add weather alerts for severe conditions
- Implement location auto-detection
- Save favorite cities
- Add historical weather data
- Export weather reports
- Add more weather metrics (dew point, wind direction)
- Implement weather charts/graphs
- Add multiple unit systems (Celsius, Fahrenheit, Kelvin)
- Dark/Light theme toggle

## 📚 Resources

- [OpenWeatherMap API](https://openweathermap.org/api)
- [OpenWeatherMap Documentation](https://openweathermap.org/current)
- [API Response Example](https://openweathermap.org/weather-conditions)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**sonviplm1-ops**

## 🙏 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📧 Contact

📧 **Email:** sonviplm1@gmail.com

For questions or suggestions, feel free to reach out!

---

# 🌤️ Bảng Điều Khiển Thời Tiết

**[English](#-weather-dashboard) | Tiếng Việt**

Một ứng dụng bảng điều khiển thời tiết tuyệt đẹp lấy dữ liệu thời tiết thực tế từ API OpenWeatherMap bằng Python và Tkinter.

## ✨ Các Tính Năng

- 🌍 **Dữ Liệu Thời Tiết Thực Tế** - Lấy thời tiết hiện tại từ bất kỳ thành phố trên thế giới
- 📍 **Tìm Kiếm Thành Phố** - Tìm kiếm thời tiết theo tên thành phố
- 🌡️ **Hiển Thị Thời Tiết Hiện Tại** - Nhiệt độ, cảm giác, mô tả thời tiết
- 📊 **Các Chỉ Số Chi Tiết** - Độ ẩm, tốc độ gió, áp suất, tầm nhìn, chỉ số UV
- 📅 **Dự Báo 5 Ngày** - Xem dự báo thời tiết cho 5 ngày tới
- 🎨 **Giao Diện Chủ Đề Tối** - Giao diện hiện đại, dễ nhìn
- ⚡ **Tích Hợp API Nhanh** - Cập nhật dữ liệu thực tế với xử lý timeout
- 🔄 **Tự Động Tải** - Tải thành phố mặc định (Hà Nội) khi khởi động
- 📱 **Thiết Kế Đáp Ứng** - Bố cục sạch sẽ và có tổ chức

## 🚀 Bắt Đầu

### Yêu Cầu Tiên Quyết
- Python 3.7 trở lên
- Kết nối Internet (để gọi API)

### Cài Đặt

1. **Clone repository**
   ```bash
   git clone https://github.com/sonviplm1-ops/english-game.git
   cd english-game
   ```

2. **Cài đặt dependencies**
   ```bash
   pip install requests pillow
   ```

3. **Chạy ứng dụng**
   ```bash
   python weather_dashboard.py
   ```

## 📖 Hướng Dẫn Sử Dụng

### Tìm Kiếm Thời Tiết
1. Nhập tên thành phố vào trường tìm kiếm
2. Nhấn **Enter** hoặc nút **Search**
3. Thời tiết hiện tại và dự báo 5 ngày sẽ được hiển thị

### Hiểu Cách Hiển Thị

#### Phần Thời Tiết Hiện Tại
- **Tên Thành Phố** - Vị trí và mã quốc gia
- **Nhiệt Độ** - Nhiệt độ hiện tại theo độ C
- **Mô Tả** - Điều kiện thời tiết (ví dụ: "Mây Rải Rác")
- **Cảm Giác** - Nhiệt độ cảm nhận được
- **Độ Ẩm** - Mức độ ẩm tính bằng phần trăm
- **Tốc Độ Gió** - Vận tốc gió tính bằng m/s
- **Áp Suất** - Áp suất khí quyển tính bằng hPa
- **Tầm Nhìn** - Khoảng cách tầm nhìn tính bằng km
- **Chỉ Số UV** - Mức bức xạ tia cực tím

#### Dự Báo 5 Ngày
- Các thẻ dự báo hàng ngày hiển thị:
  - Thứ và ngày
  - Nhiệt độ cao nhất
  - Điều kiện thời tiết
  - Mức độ ẩm

### Phím Tắt
- **Enter** - Tìm kiếm thời tiết thành phố

## 🔑 Cấu Hình API

Ứng dụng sử dụng API miễn phí của OpenWeatherMap với khóa mặc định. Để sử dụng cho sản xuất:

1. Nhận khóa API miễn phí từ [OpenWeatherMap](https://openweathermap.org/api)
2. Chỉnh sửa `weather_dashboard.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

### Kế Hoạch Miễn Phí vs Trả Phí
- **Kế Hoạch Miễn Phí**: Thời tiết hiện tại và dự báo 5 ngày (Đủ cho ứng dụng này)
- **Kế Hoạch Trả Phí**: Dự báo mở rộng, dữ liệu lịch sử, nhiều cuộc gọi API

## 🎨 Các Thành Phần UI

- **Header** - Banner xanh tối với tiêu đề và thanh tìm kiếm
- **Bảng Thời Tiết Hiện Tại** - Hiển thị lớn các điều kiện hiện tại
- **Lưới Chi Tiết** - Bố cục 3 cột hiển thị các chỉ số chính
- **Thẻ Dự Báo** - 5 thẻ hiển thị dự báo hàng ngày
- **Thanh Trạng Thái** - Hiển thị thời gian cập nhật cuối cùng và tin nhắn trạng thái

## 📊 Định Dạng Dữ Liệu Thời Tiết

Ứng dụng lấy dữ liệu từ API OpenWeatherMap ở định dạng JSON:

```json
{
  "name": "Hà Nội",
  "sys": {"country": "VN"},
  "main": {
    "temp": 28.5,
    "feels_like": 32.1,
    "humidity": 75,
    "pressure": 1013
  },
  "weather": [{"main": "Clouds", "description": "mây che phủ"}],
  "wind": {"speed": 5.2},
  "visibility": 10000
}
```

## 🔧 Tùy Chỉnh

### Thay Đổi Đơn Vị Nhiệt Độ
Sửa đổi cuộc gọi API trong `search_weather()`:
```python
# Thay metric thành imperial cho Fahrenheit
current_url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=imperial"
```

### Thay Đổi Thành Phố Mặc Định
Chỉnh sửa những dòng cuối cùng:
```python
root.after(500, lambda: app.city_entry.insert(0, "Tokyo") or app.search_weather())
```

### Thay Đổi Màu Sắc
Chỉnh sửa mã màu trong `setup_ui()`:
- `#0d47a1` - Nền header
- `#2a2a2a` - Nền nội dung
- `#FFD700` - Văn bản nổi bật (Vàng)
- `#87CEEB` - Văn bản phụ (Xanh Dương Nhạt)

## 📁 Cấu Trúc Dự Án

```
english-game/
├── weather_dashboard.py    # Ứng dụng Bảng Điều Khiển Thời Tiết chính
├── WEATHER_README.md       # Tệp này
├── requirements.txt        # Cập nhật với requests và pillow
└── ...
```

## 🐛 Khắc Phục Sự Cố

### Lỗi "City not found" (Thành phố không tìm thấy)
- Kiểm tra chính tả tên thành phố
- Sử dụng tên thành phố tiếng Anh
- Thử với mã quốc gia (ví dụ: "London, UK")

### Timeout kết nối
- Kiểm tra kết nối Internet
- Xác minh dịch vụ API có sẵn
- Thử lại sau vài giây

### Dữ liệu thời tiết không cập nhật
- Đảm bảo khóa API hợp lệ
- Kiểm tra xem giới hạn cuộc gọi API đã đạt chưa (tier miễn phí: 60 cuộc gọi/phút)
- Xác minh tên thành phố chính xác

### Thẻ dự báo trống
- API có thể phản hồi chậm
- Thử tìm kiếm lại
- Kiểm tra xem dữ liệu dự báo có sẵn cho thành phố không

## 🌐 Giới Hạn Tỷ Lệ API

**Kế Hoạch Miễn Phí:**
- 60 cuộc gọi API mỗi phút
- 1.000.000 cuộc gọi API mỗi tháng
- Tần suất cập nhật dữ liệu: Mỗi 10 phút

## 📝 Các Điều Kiện Thời Tiết

API hỗ trợ các điều kiện thời tiết khác nhau:
- Thoáng
- Mây
- Mưa phùn
- Mưa
- Bão có sét
- Tuyết
- Sương mù
- Khói
- Sương
- Bụi
- Sương mù dày
- Cát
- Tro
- Gió giật
- Lốc xoáy

## 🚀 Cải Tiến Tương Lai

- Thêm cảnh báo thời tiết cho điều kiện nghiêm trọng
- Triển khai tự động phát hiện vị trí
- Lưu các thành phố yêu thích
- Thêm dữ liệu thời tiết lịch sử
- Xuất báo cáo thời tiết
- Thêm nhiều chỉ số thời tiết (điểm sương, hướng gió)
- Triển khai biểu đồ/đồ thị thời tiết
- Thêm nhiều hệ thống đơn vị (Celsius, Fahrenheit, Kelvin)
- Chuyển đổi chủ đề tối/sáng

## 📚 Tài Nguyên

- [API OpenWeatherMap](https://openweathermap.org/api)
- [Tài Liệu OpenWeatherMap](https://openweathermap.org/current)
- [Ví Dụ Phản Hồi API](https://openweathermap.org/weather-conditions)

## 📝 Giấy Phép

Dự án này là mã nguồn mở và có sẵn theo Giấy phép MIT.

## 👤 Tác Giả

**sonviplm1-ops**

## 🙏 Đóng Góp

Chúng tôi hoan nghênh những đóng góp! Hãy thoải mái:
- Báo cáo lỗi
- Đề xuất các tính năng mới
- Gửi yêu cầu kéo
- Cải thiện tài liệu

## 📧 Liên Hệ

📧 **Email:** sonviplm1@gmail.com

Nếu có câu hỏi hoặc gợi ý, hãy liên hệ với chúng tôi!

---

**Happy Weather Checking! 🌤️✨**
````
