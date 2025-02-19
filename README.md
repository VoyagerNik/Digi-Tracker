# **Digi Tracker**

## **Overview**
Digi Tracker is a time-tracking application built with **Tkinter** for the GUI and **threading** for parallel execution. It allows users to track their application usage, visualize data with **matplotlib**, and store records using **MySQL**. The program enables users to **pause and resume tracking indefinitely** and generates insights through graphical representations.

---

## **Features**
- Real-time application usage tracking.
- **Pause/Resume** functionality for flexible tracking.
- **Quick results** (session-wise) and **weekly reports** displayed through graphs.
- Stores tracking data in a **MySQL database**.
- Custom **GUI with images and icons** for an enhanced user experience.
- **Feedback and rating** options for users.

---

## **Technologies Used**
- **Python 3.9**
- **Tkinter** – GUI development
- **Matplotlib** – Data visualization
- **Win32gui** – Application tracking
- **Threading** – Parallel execution
- **MySQL 8.0** – Database management
- **Psutil** – Process management
- **Pillow** – Image handling
- **Pandas** – Data manipulation

---

## **Installation**

### **Prerequisites**
- **Python 3.9** installed
- **MySQL 8.0** installed and running

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/digi-tracker.git
cd digi-tracker
```

### **Step 2: Install Required Packages**
```bash
pip install -r requirements.txt
```

### **Step 3: Set Up the Database**
- Create a MySQL database named **firstcodes**.
- Import any provided SQL files from the `database/` folder (if available).

### **Step 4: Run the Application**
```bash
cd src
python main.py
```

---

## **Usage**
1. **Start the Tracker** – Click the "Start" button to begin tracking.
2. **Pause/Resume** – Use the pause/play buttons as needed.
3. **Stop Tracking** – Click "Stop" to save data.
4. **View Graphs** – Check session-wise and weekly insights.
5. **Settings** – Provide feedback or rate the application.

---

## **Future Enhancements**
- **Website-level tracking** for individual websites.
- **Improved graphical representations** for better insights.
- **Enhanced tracking accuracy** by eliminating minor timing errors.
- **Pre-tracking weekly insights** for user convenience.

---

## **Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## **License**
This project is licensed under the **[MIT License](LICENSE)**.

---

## **Credits**
- Stack Overflow  
- GeeksforGeeks  
- GitHub  
- Codemy.com  
- Sumita Arora
