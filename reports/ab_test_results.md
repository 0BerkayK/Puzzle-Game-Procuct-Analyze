# Cookie Cats A/B Test Results

## Test Senaryosu
- **Hipotez:** Gate seviyesi 30 mu yoksa 40 mı retention üzerinde daha iyi etki yaratır?  
- **Kontrol Grubu:** Gate_30  
- **Varyant Grubu:** Gate_40  
- **Metrikler:** 1. gün ve 7. gün retention (retention_1 ve retention_7)  

---

## 1. Gün Retention
- **Gate_30 ortalama retention:** ~0.204  
- **Gate_40 ortalama retention:** ~0.204 (çıktılar segmentlere göre çok benzer)  
- **t-test p-value:** 0.0744  

**Yorum:**  
- 1. gün retention farkı istatistiksel olarak anlamlı değildir (p > 0.05).  
- Yani ilk gün için Gate_30 ve Gate_40 grupları arasında anlamlı bir fark gözlenmemektedir.

---

## 7. Gün Retention
- **Gate_30 ortalama retention:** ~0.0329  
- **Gate_40 ortalama retention:** ~0.2289  
- **t-test p-value:** 0.00155  

**Yorum:**  
- 7. gün retention farkı istatistiksel olarak anlamlıdır (p < 0.05).  
- Gate_40 varyantı, 7. gün retention’ı artırarak oyuncuların oyunda daha uzun süre kalmasını sağlamaktadır.  
- Bu sonuç, Gate seviyesinin retention üzerinde özellikle orta vadeli etkisi olduğunu göstermektedir.

---

## Genel Sonuç ve Öneriler
- Gate seviyesini **daha ileri bir seviyeye çekmek (Gate_40)** oyuncuların 7. gün retention’ını artırır.  
- 1. gün retention düşük olan **casual oyuncular** için ayrıca onboarding ve günlük ödül gibi ek özellikler önerilmektedir.  
- Sonraki adım: Bu varyantı temel alarak yeni özellikler ve sosyal bağlayıcı mekanikler tasarlanabilir, ve QA süreci ile test edilebilir.
