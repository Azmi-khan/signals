#  Digital Signal Processing –

This repository contains my complete solutions for **Lab 4** of the *Digital Signal Processing* course.  
It includes both the **original lab questions** and the **Python implementations** that analyze and visualize various signal behaviors using **NumPy**, **SciPy**, and **Matplotlib**.

---

##  Overview

| Section | Topic | Lab Question | Python Code |
|----------|--------|--------------|--------------|
| 4.1 | Sine Signal Sampling | [lab4_part1.md](lab_questions/lab4_part1.md) | [lab_4_pt1.py](src/lab_4_pt1.py) |
| 4.2 | Fourier Synthesis | [lab4_part2.md](lab_questions/lab4_part2.md) | [lab_4_pt2.py](src/lab_4_pt2.py) |
| 4.3 | Discrete Fourier Transform (DFT) | [lab4_part3.md](lab_questions/lab4_part3.md) | [lab_4_pt3.py](src/lab_4_pt3.py) |

Each section explores a fundamental signal-processing concept:
- **4.1:** Sampling and discrete sinusoidal signals  
- **4.2:** Fourier series synthesis and time shifting of sawtooth waves  
- **4.3:** Frequency analysis using the Discrete Fourier Transform (DFT)

---

##  Concepts Covered

- Discrete-time sinusoidal signal generation  
- Fourier series representation of periodic signals  
- Frequency-domain representation via DFT and FFT  
- Phase shifts and sampling effects  
- Visualization of time and frequency domain responses  

---

##  Folder Structure

```
signal-processing-lab4/
│
├── lab_questions/         # Lab instructions (Markdown formatted)
│   ├── lab4_part1.md
│   ├── lab4_part2.md
│   └── lab4_part3.md
│
├── src/                   # My Python solutions
│   ├── lab_4_pt1.py
│   ├── lab_4_pt2.py
│   └── lab_4_pt3.py
│
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignored files (e.g., __pycache__)
```

---

##  Setup Instructions

###  Clone the repository
```bash
git clone https://github.com/yourusername/signal-processing-lab4.git
cd signal-processing-lab4
```

###  Install dependencies
```bash
pip install -r requirements.txt
```

###  Run individual lab parts
```bash
python src/lab_4_pt1.py
python src/lab_4_pt2.py
python src/lab_4_pt3.py
```

Each script displays the respective signal plots and frequency analyses using Matplotlib.

---

##  Example Topics Illustrated

- **Stem plots** for sampled sine waves  
- **Fourier synthesis** of sawtooth signals up to the 5th harmonic  
- **FFT amplitude spectra** for cosine, sawtooth, and square waves  
- **Phase and time-shift demonstrations**

---

##  Author

**Name:** *Azmi Rehman Khan*  
**Course:** Electric signal processing  
**Institution:** *Technische hochschule Ingolstadt*  
**Year:** 2025  

---

##  License

This project is intended for educational and reference purposes.  
Feel free to use and modify the code for your own learning or lab reports.

---

>  *“Understanding signals in both time and frequency domains reveals the beauty of digital processing.”*