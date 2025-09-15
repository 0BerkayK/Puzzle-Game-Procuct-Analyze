# Cookie Cats Puzzle Game Analysis Project

This project has been prepared in line with the job responsibilities and required qualifications of Vento Games' Product Specialist job posting.



## Proje Hakkında
Bu proje, Cookie Cats adlı mobil bulmaca oyunu üzerinden **veri odaklı oyun geliştirme ve analiz süreçlerini** simüle etmek için hazırlanmıştır. Amaç, oyuncu davranışlarını anlamak, A/B testleri ile iyileştirme fırsatlarını belirlemek, mobil oyun pazarını benchmark etmek ve QA süreçlerini yönetmektir.

---

## Proje Kapsamı
Proje, dört temel alana odaklanmıştır:

1. **Feature Geliştirme ve Analizi**
   - Segment bazlı retention analizi
   - Data-driven ve yaratıcı öneriler 
   - Önerilen oyun özellikleri ve iyileştirme alanları

2. **A/B Test Planlama ve Analizi**
   - A/B test senaryoları ve hipotezler
   - 1-day ve 7-day retention üzerine testler
   - İstatistiksel analiz (t-test)
   - Sonuç raporu 

3. **Mobil Oyun Pazarı Araştırması**
   - Benchmark veri seti oluşturma veya simülasyon
   - Cookie Cats vs. benchmark karşılaştırması
   - Market trendleri ve oyuncu segmentlerine göre öneriler
   - Analiz notebook ve rapor 

4. **QA ve Test Planlama**
   - Retention ve feature logic QA kontrolleri
   - A/B test varyant dağılım kontrolü
   - 7-day bonus feature testi
   - QA checklist 
   - QA notebook

---

## Proje Yapısı

``` bash 
│
├── data/
│   └── cookie_cats.csv                # Kaggle’dan indirilen veri seti
│   └── puzzle_games_benchmark.csv     # Benchmark veri seti
├── notebooks/
│   ├── 01_cookiecats_eda.ipynb        # Keşifsel veri analizi (EDA)
│   ├── 02_feature_ideas.ipynb         # Özellik geliştirme (veri odaklı + yaratıcı fikirler)
│   ├── 03_ab_test_analysis.ipynb      # A/B test planı + istatistiksel analiz
│   ├── 04_market_research.ipynb       # Mobil oyun pazarı araştırması + benchmark
│   └── 05_qa_plan.ipynb               # QA senaryoları & kalite standartları
│
├── scripts/
│   ├── generate_benchmark_csv.py      # puzzle_games_benchmark.csv yi üretmek için kullanılan script
│
├── dashboards/
│   └── ab_test_results.pbix           # Power BI / Tableau / Looker Studio dashboard
│
├── reports/
│   ├── feature_recommendations.md     # Veri odaklı yeni özellik önerileri
│   ├── ab_test_results.md             # Test sonuçları & yorumlar
│   ├── market_trends.md               # Pazar araştırması raporu
│   └── qa_checklist.md                # QA planı & kalite kriterleri
│
├── README.md                          # Proje açıklaması
└── requirements.txt                   # Gerekli Python kütüphaneleri


```

## Kullanılan Veri Setleri

Proje boyunca aşağıdaki veri setleri kullanılmıştır:

1. **Cookie Cats A/B Dataset**  
   - Açıklama: Cookie Cats mobil bulmaca oyunu üzerinden toplanmış oyuncu davranışları, retention ve A/B test varyantlarını içeren veri seti.  
   - İçerik: 
     - `user_id` : Oyuncu kimliği
     - `version` : A/B test varyantı (ör. gate_30, gate_40)
     - `sum_gamerounds` : Oyuncunun toplam oyun turu sayısı
     - `retention_1` : 1. gün retention (True/False)
     - `retention_7` : 7. gün retention (True/False)
     - Diğer feature sütunları (bonus_7day, vb.)
   - Kaynak / Link: [Cookie Cats A/B Dataset on Kaggle](https://www.kaggle.com/datasets/marwandiab/cookie-catsdataset?utm_source=chatgpt.com)

2. **Puzzle Games Benchmark Dataset**  
   - Açıklama: Benchmark amacıyla simüle edilmiş puzzle oyunları verisi.  
   - İçerik: `game`, `publisher`, `retention_1`, `retention_7`  
   - Bu dataset proje içinde `data/puzzle_games_benchmark.csv` olarak oluşturulmuştur.
  



## Kullanılan Teknolojiler
- **Python:** pandas, numpy, matplotlib, seaborn, scipy  
- **Jupyter Notebook:** Analiz ve görselleştirme  
- **Markdown:** Rapor ve QA dokümantasyonu  

---

## Nasıl Kullanılır?
1. Repository’yi klonlayın.
2. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install -r requirements.txt

