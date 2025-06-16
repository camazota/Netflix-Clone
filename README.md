# Netflix Klon - Netflix Clone

[TR]
Bu proje, Netflix’in giriş sayfasının birebir klonu olarak geliştirilmiş; popüler filmleri görselleriyle birlikte, tamamen responsive ve orijinal tasarıma sadık kalınarak hazırlanmış bir film sayfasıdır. Eğitim amaçlı olarak, aynı işlevselliği Node.js (Express), Go (Fiber) ve Python (socket) kullanarak geliştirilmiş farklı web sunucusu örnekleri içerir.

[ENG]
This project is developed as an exact clone of Netflix’s landing page; it lists popular movies with their images, fully responsive and faithful to the original design. For educational purposes, it includes different web server implementations providing the same functionality using Node.js (Express), Go (Fiber), and Python (socket).


## Özellikler - Features

[TR]
- Popüler filmler listesi JSON API üzerinden sağlanır.
- Statik dosya servisi (CSS, resimler) mevcuttur.
- Ana sayfa HTML ile sunulur.
- Üç farklı dilde web sunucusu implementasyonları:
  - Node.js (Express)
  - Go (Fiber framework)
  - Python (socket modülü ile temel HTTP sunucusu)

[ENG]
- Popular movies list served via a JSON API.
- Static file service (CSS, images) available.
- Homepage served as HTML.
- Three different web server implementations in:
  - Node.js (Express)
  - Go (Fiber framework)
  - Python (basic HTTP server using socket module)


## Gereksinimler - Requirements

- Node.js (v22.15.0)
- Python 3.13.4
- Go (1.24.2)


## Klasör Yapısı - Folder Structure

netflix-clone-page/
├── source-codes/
│ ├── Golang/ # Go (Fiber) server
│ ├── Nodejs/ # Node.js Express server
│ └── Python/ # Python Socket server 
├── static/ # CSS, images, JavaScript, etc. 
├── templates/ # HTML files 
└── Netflix.exe # Compiled Go (Fiber) executable 



## Çalıştırma - How to Run

### Node.js Server

[TR]
1. Node.js yüklü olduğundan emin olun. [Node.js indir](https://nodejs.org/)
2. Terminalde proje dizinine gidin:
   ```bash
   cd source-codes/Nodejs
3. Sunucuyu başlatın
   ```bash
   npm start
4. Tarayıcıda http://127.0.0.1:8080 adresini açın

[ENG]
1. Make sure you have Node.js installed. [Download Node.js](https://nodejs.org/)
2. Change to the project directory in the terminal:
   ``` bash
   cd source codes/Nodejs
3. Start the server
   ``` bash
   npm start
4. Open http://127.0.0.1:8080 in the browser



### Go (Fiber) Server

[TR]
1. Netflix.exe derlenmiş halidir. Direkt çalıştırabilirsiniz.

[ENG]
1. Netflix.exe is the compiled version. You can run it directly.


### Python (socket) Server

[TR]
1. Sisteminizde python yüklü olduğundan emin olun. [Python indir](https://python.org/)
2. Terminalde proje dizinine gidin:
   ```bash
   cd source-codes/Python
3. Sunucuyu başlatın
   ```bash
   python server.py
4. Tarayıcıda http://127.0.0.1:8080 adresini açın

[ENG]
1. Make sure you have python installed on your system. [Download Python](https://python.org/)
2. Go to the project directory in the terminal:
   ```bash
   cd source-codes/Python
3. Start the server
   ```bash
   python server.py
4. Open http://127.0.0.1:8080 in the browser


## Lisans - Licence

[TR]
Bu proje MIT Lisansı ile lisanslanmıştır.  
Netflix marka ve içerikleri telif hakkına tabi olup, bu içeriklerin ticari kullanımı yasaktır.  
Proje sadece eğitim ve kişisel kullanım amaçlıdır.Projenin amacı asla dağıtım veya ticari değildir

[ENG]
This project is licensed under the MIT License.
Netflix brand and content are subject to copyright and commercial use of these contents is prohibited.
The project is for educational and personal use only. The purpose of the project is never distribution or commercial


#### İletişim - Contact

[TR]
iletişim: akbasd507@gmail.com

[ENG]
contact: akbasd507@gmail.com