````markdown
# 📝 To-Do List Application

**English | [Tiếng Việt](#-ứng-dụng-danh-sách-công-việc)**

A feature-rich to-do list application with local storage functionality built with Python and Tkinter.

## ✨ Features

- ✅ **Add Tasks** - Quickly add new tasks with Enter key support
- ✓ **Toggle Completion** - Mark tasks as complete or incomplete
- ✎ **Edit Tasks** - Modify existing tasks
- 🗑️ **Delete Tasks** - Remove individual tasks or all at once
- 📊 **Statistics Dashboard** - View total, completed, and remaining tasks
- 🔍 **Filter Tasks** - View all, active, or completed tasks
- 💾 **Local Storage** - Automatically save to JSON file
- 📅 **Task Details** - View creation date and completion timestamp
- 📤 **Export** - Export all tasks to JSON format
- 🎯 **Keyboard Shortcuts**:
  - **Enter** - Add or search task
  - **Space** - Toggle selected task completion
  - **Delete** - Delete selected task
  - **Double-click** - Open task menu

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sonviplm1-ops/english-game.git
   cd english-game
   ```

2. **Run the application**
   ```bash
   python todo_app.py
   ```

## 📖 Usage Guide

### Adding Tasks
1. Type your task in the input field
2. Press **Enter** or click **Add** button
3. Task will be added to your list and automatically saved

### Managing Tasks
- **Double-click** on a task to open the context menu
- **Toggle Completion** - Mark task as done
- **Edit** - Modify the task text
- **View Details** - See creation date and completion time
- **Delete** - Remove the task

### Filtering
Select from three filter options:
- **All** - View all tasks
- **Active** - View only incomplete tasks
- **Completed** - View only completed tasks

### Statistics
View real-time statistics:
- **Total Tasks** - Total number of tasks
- **Completed** - Number of finished tasks
- **Remaining** - Number of pending tasks

### Buttons
- **Clear Completed** - Remove all completed tasks at once
- **Delete All** - Delete all tasks (cannot be undone)
- **Export** - Save all tasks to external JSON file

## 💾 Local Storage

Tasks are automatically saved to `todos.json` file in the same directory. The file includes:
- Task text
- Completion status
- Creation timestamp
- Completion timestamp

### Data Format
```json
[
  {
    "id": 1,
    "task": "Buy groceries",
    "completed": false,
    "created_at": "2026-05-24 12:30:00",
    "completed_at": null
  }
]
```

## 🎨 User Interface

- **Header** - Blue banner with app title
- **Input Section** - Add new tasks easily
- **Statistics Dashboard** - Quick overview of your tasks
- **Filter Panel** - Toggle between different views
- **Task List** - Scrollable list with visual indicators
- **Action Buttons** - Manage your tasks efficiently

## 🔧 Customization

### Change Colors
Edit the color codes in `todo_app.py`:
- `#1976D2` - Header/Primary color (Blue)
- `#4CAF50` - Success color (Green)
- `#FF9800` - Warning color (Orange)
- `#F44336` - Danger color (Red)

### Window Size
Modify these constants:
```python
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
```

## 📁 Project Structure

```
english-game/
├── todo_app.py         # Main To-Do List application
├── todos.json          # Local storage file (auto-created)
└── todos_export.json   # Exported tasks (optional)
```

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Enter | Add task or submit |
| Space | Toggle selected task |
| Delete | Delete selected task |
| Double-click | Open task menu |

## 🐛 Troubleshooting

### Tasks not saving?
- Check file permissions in the directory
- Ensure `todos.json` file is not open in another program
- Try exporting to verify data is working

### Cannot edit tasks?
- Make sure to double-click on the task
- Select the task first, then use the menu

### Missing tasks after restart?
- Check if `todos.json` file exists in the same directory
- Verify the file is not corrupted by opening in a text editor

## 🚀 Future Enhancements

- Add task priority levels
- Implement due dates and reminders
- Add task categories/tags
- Support for recurring tasks
- Dark mode theme
- Cloud synchronization

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

# 📝 Ứng dụng Danh Sách Công Việc

**[English](#-to-do-list-application) | Tiếng Việt**

Một ứng dụng danh sách công việc giàu tính năng với chức năng lưu trữ cục bộ được xây dựng bằng Python và Tkinter.

## ✨ Các Tính Năng

- ✅ **Thêm Công Việc** - Thêm công việc mới nhanh chóng, hỗ trợ phím Enter
- ✓ **Đánh Dấu Hoàn Thành** - Đánh dấu công việc là hoàn thành hoặc chưa hoàn thành
- ✎ **Chỉnh Sửa Công Việc** - Sửa đổi công việc hiện có
- 🗑️ **Xóa Công Việc** - Xóa công việc riêng lẻ hoặc tất cả
- 📊 **Bảng Điều Khiển Thống Kê** - Xem tổng số, hoàn thành và công việc còn lại
- 🔍 **Lọc Công Việc** - Xem tất cả, hoạt động hoặc công việc đã hoàn thành
- 💾 **Lưu Trữ Cục Bộ** - Tự động lưu vào tệp JSON
- 📅 **Chi Tiết Công Việc** - Xem ngày tạo và thời gian hoàn thành
- 📤 **Xuất Dữ Liệu** - Xuất tất cả công việc sang định dạng JSON
- 🎯 **Phím Tắt**:
  - **Enter** - Thêm hoặc tìm kiếm công việc
  - **Space** - Chuyển đổi hoàn thành công việc được chọn
  - **Delete** - Xóa công việc được chọn
  - **Nhấp đôi** - Mở menu công việc

## 🚀 Bắt Đầu

### Yêu Cầu Tiên Quyết
- Python 3.7 trở lên

### Cài Đặt

1. **Clone repository**
   ```bash
   git clone https://github.com/sonviplm1-ops/english-game.git
   cd english-game
   ```

2. **Chạy ứng dụng**
   ```bash
   python todo_app.py
   ```

## 📖 Hướng Dẫn Sử Dụng

### Thêm Công Việc
1. Nhập công việc trong trường nhập liệu
2. Nhấn **Enter** hoặc nút **Add**
3. Công việc sẽ được thêm vào danh sách và tự động lưu

### Quản Lý Công Việc
- **Nhấp đôi** vào công việc để mở menu ngữ cảnh
- **Chuyển Đổi Hoàn Thành** - Đánh dấu công việc là hoàn thành
- **Chỉnh Sửa** - Sửa đổi văn bản công việc
- **Xem Chi Tiết** - Xem ngày tạo và thời gian hoàn thành
- **Xóa** - Xóa công việc

### Lọc
Chọn từ ba tùy chọn lọc:
- **Tất Cả** - Xem tất cả công việc
- **Hoạt Động** - Xem chỉ các công việc chưa hoàn thành
- **Hoàn Thành** - Xem chỉ các công việc đã hoàn thành

### Thống Kê
Xem thống kê theo thời gian thực:
- **Tổng Công Việc** - Tổng số công việc
- **Hoàn Thành** - Số công việc đã hoàn thành
- **Còn Lại** - Số công việc đang chờ xử lý

### Nút
- **Xóa Hoàn Thành** - Xóa tất cả các công việc đã hoàn thành
- **Xóa Tất Cả** - Xóa tất cả công việc (không thể hoàn tác)
- **Xuất** - Lưu tất cả công việc vào tệp JSON bên ngoài

## 💾 Lưu Trữ Cục Bộ

Công việc được tự động lưu vào tệp `todos.json` trong cùng thư mục. Tệp bao gồm:
- Văn bản công việc
- Trạng thái hoàn thành
- Dấu thời gian tạo
- Dấu thời gian hoàn thành

### Định Dạng Dữ Liệu
```json
[
  {
    "id": 1,
    "task": "Mua đồ tạp hóa",
    "completed": false,
    "created_at": "2026-05-24 12:30:00",
    "completed_at": null
  }
]
```

## 🎨 Giao Diện Người Dùng

- **Header** - Banner màu xanh với tiêu đề ứng dụng
- **Phần Nhập Liệu** - Thêm công việc mới dễ dàng
- **Bảng Điều Khiển Thống Kê** - Tổng quan nhanh về công việc của bạn
- **Bảng Lọc** - Chuyển đổi giữa các chế độ xem khác nhau
- **Danh Sách Công Việc** - Danh sách có thể cuộn với các chỉ báo trực quan
- **Nút Hành Động** - Quản lý công việc hiệu quả

## 🔧 Tùy Chỉnh

### Thay Đổi Màu Sắc
Chỉnh sửa các mã màu trong `todo_app.py`:
- `#1976D2` - Màu header/chính (Xanh)
- `#4CAF50` - Màu thành công (Xanh lá)
- `#FF9800` - Màu cảnh báo (Cam)
- `#F44336` - Màu nguy hiểm (Đỏ)

### Kích Thước Cửa Sổ
Sửa đổi các hằng số này:
```python
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
```

## 📁 Cấu Trúc Dự Án

```
english-game/
├── todo_app.py         # Ứng dụng Danh Sách Công Việc chính
├── todos.json          # Tệp lưu trữ cục bộ (tự động tạo)
└── todos_export.json   # Công việc đã xuất (tùy chọn)
```

## ⌨️ Phím Tắt

| Phím Tắt | Hành Động |
|----------|-----------|
| Enter | Thêm công việc hoặc gửi |
| Space | Chuyển đổi công việc được chọn |
| Delete | Xóa công việc được chọn |
| Nhấp đôi | Mở menu công việc |

## 🐛 Khắc Phục Sự Cố

### Công việc không được lưu?
- Kiểm tra quyền tệp trong thư mục
- Đảm bảo tệp `todos.json` không mở trong chương trình khác
- Thử xuất để xác minh dữ liệu đang hoạt động

### Không thể chỉnh sửa công việc?
- Hãy chắc chắn nhấp đôi vào công việc
- Chọn công việc trước, sau đó sử dụng menu

### Công việc bị thiếu sau khi khởi động lại?
- Kiểm tra xem tệp `todos.json` có tồn tại trong cùng thư mục không
- Xác minh tệp không bị hỏng bằng cách mở trong trình chỉnh sửa văn bản

## 🚀 Cải Tiến Tương Lai

- Thêm mức độ ưu tiên công việc
- Triển khai ngày hết hạn và nhắc nhở
- Thêm danh mục/thẻ công việc
- Hỗ trợ các công việc lặp lại
- Chế độ tối
- Đồng bộ hóa đám mây

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

**Happy Task Management! 📝✨**
````
