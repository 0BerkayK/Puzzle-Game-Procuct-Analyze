# Puzzle-Game-Procuct-Analyze
This project has been prepared in line with the job responsibilities and required qualifications of Vento Games' Product Specialist job posting.



Veri Seti Hakkında (Cookie Cats A/B Dataset)

Oyun türü: Match-3 tarzı puzzle oyunu .

Deney: Oyuncular rastgele 2 gruba ayrılıyor:

Kontrol (Gate_30): Oyuncular 30. seviyede “gate” (geçiş engeli) ile karşılaşıyor.

Varyant (Gate_40): Gate seviyesi 40’a çekilmiş.

Amaç: Gate’in konumu, retention (1-day, 7-day) ve oyuncu bağlılığı üzerinde nasıl etki yaratıyor?

Kolonlar (dataset’te tipik olanlar):

userid: oyuncu kimliği

version: Gate_30 / Gate_40

sum_gamerounds: toplam oynanan round sayısı

retention_1: 1. günde geri dönüp dönmedi (binary)

retention_7: 7. günde geri dönüp dönmedi (binary)



🔹 Adım A – Veri odaklı & yaratıcı özellik geliştirme

Veri temizleme + keşifsel analiz (EDA) → hangi gruptaki oyuncular daha çok round oynuyor, retention oranı nasıl?

Retention ve oynanış davranışlarına göre özellik önerisi çıkaracağız. (örn. “early engagement bonus”, “yardımcı ipucu”, “günlük ödül sistemi”).

🔹 Adım B – A/B test planı ve istatistiksel analiz

Kontrol vs varyant gruplarının retention farkını test et (ki-kare testi veya z-testi).

Sonuçları görselleştir (bar chart: retention_1 ve retention_7 karşılaştırması).

Etki büyüklüğünü (effect size) ölç → fark iş açısından anlamlı mı?

🔹 Adım C – Mobil oyun pazar araştırması

Benzer puzzle oyunlarının retention benchmark’larını bulacağız.

“Cookie Cats” sonuçlarını sektör ortalamasıyla kıyaslayıp, hangi metriklerin iyileştirilmesi gerektiğini paylaşacağız.

🔹 Adım D – QA süreci & kalite kontrol

Yeni önerilen özellik için QA test senaryoları oluşturacağız (örnek: günlük ödül sistemi eklenirse test edilecek fonksiyonellikler).

Hangi kalite kriterlerine (stabilite, UX, performans) bakılması gerektiğini belirleyeceğiz.

``` bash 
│
├── data/
│   └── cookie_cats.csv                # Kaggle’dan indirilen veri seti
│
├── notebooks/
│   ├── 01_cookiecats_eda.ipynb        # Keşifsel veri analizi (EDA)
│   ├── 02_feature_ideas.ipynb         # Özellik geliştirme (veri odaklı + yaratıcı fikirler)
│   ├── 03_ab_test_analysis.ipynb      # A/B test planı + istatistiksel analiz
│   ├── 04_market_research.ipynb       # Mobil oyun pazarı araştırması + benchmark
│   └── 05_qa_plan.ipynb               # QA senaryoları & kalite standartları
│
├── scripts/
│   ├── data_preprocessing.py          # Veri temizleme & preprocessing scripti
│   ├── ab_test_functions.py           # Hipotez testleri, metrik hesaplama fonksiyonları
│   └── visualization_utils.py         # Grafik çizim fonksiyonları
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
