# Prompt Günlüğü ve YZ Beyanı

Kullanılan araç: Claude (Anthropic), claude.ai

Aşağıdaki istemler sohbette aynen bu şekilde gönderildi.

| İstemim | YZ ne yaptı? | Ben ne yaptım? |
|---|---|---|
| Aşağıdaki notlarımı Markdown biçiminde bir README'ye dönüştür. Bir başlık, bir liste ve bir bağlantı olsun. Cümlelerimi değiştirme, yalnızca düzenle: [tanıtım, ilgi alanları, ders beklentisi ve "Kodlama ve YZ'nin mesleğimdeki yeri" notlarım] | Notları başlıklara ayırdı, ilgi alanlarını ve beklentiyi listeye çevirdi, üniversite sitesini bağlantı yaptı. Cümlelere dokunmadı; paragrafın 104 kelime olduğunu ve 100–150 aralığında kaldığını kontrol etti. | Paragrafı YZ'nin sunduğu iki taslaktan seçtim (sosyolojide dijital veri ve araç yazma odaklı olanı) ve README'nin depoda düzgün göründüğünü kontrol ettim. |
| Python'da kullanıcıdan adını ve doğum yılını alıp yaşını hesaplayan, kişiye özel bir karşılama mesajı yazan bir program yaz. Her satırı Türkçe yorumla açıkla. Ardından input() ve int() satırlarını, hiç kod bilmeyen birine anlatır gibi açıkla. | merhaba.py'yi her satırı yorumlu yazdı; input()'u "soru sorup cevabı not eden anketör", int()'i "formdaki yazıyı rakama çeviren kişi" benzetmesiyle anlattı. Testte 2031 girilince yaşın −5 çıktığını, "yirmi" yazılınca programın çöktüğünü gösterdi. | Çıktının ekran görüntüsünü aldım. Gelecek yıl sorununu düzeltmeye karar verdim. |
| Doğum yılı bu yıldan büyükse uyarı vermek istiyorum. Kodu yazma; hangi Python yapısını kullanmam gerektiğini bir ipucuyla anlat. | Kod yazmadan if/else kullanmam gerektiğini, karşılaştırmanın simdiki_yil satırından sonra gelmesi gerektiğini, ">" işaretini ve girinti kuralını anlattı; değişikliği kurmam için seçenekler sundu. | Koşulda ">" işaretini, "Bu yıl henüz gelmedi, lütfen doğum yılını kontrol et." mesajını seçtim ve 120 yaş kontrolünü eklememeye karar verdim; YZ seçimlerimi koda yerleştirdi. 2003, 2026, 2027 ve 2031 ile test edildi. |
| Şu değişiklik için kısa ve anlamlı bir Türkçe commit mesajı öner: merhaba.py dosyasına, doğum yılı şu anki yıldan büyükse "Bu yıl henüz gelmedi" uyarısı veren bir if/else kontrolü ekledim. | Üç commit mesajı önerdi. | "Doğum yılı bu yıldan büyükse uyarı veren if/else eklendi" mesajını kullandım. |

## Bilinen sınır

Doğum yılına sayı yerine yazı (ör. "yirmi") girilirse int() dönüşümü ValueError verir ve program kapanır. Bu kontrolü bu sürüme eklemedim.

## YZ Kullanım Beyan Formu

| Alan | Yanıtım |
|---|---|
| Kullanılan YZ aracı/araçları | Claude (Anthropic), claude.ai |
| Kullanma amacı | README notlarını Markdown'a dönüştürme ve paragraf taslağı, merhaba.py programını yazdırma ve açıklatma, kendi değişikliğim için ipucu ve seçenekler alma, commit mesajı önerisi |
| Kontrol ve sorumluluk | Yapay zekâ tarafından üretilen içeriği gözden geçirdiğimi, gerekli düzeltmeleri yaptığımı ve teslim ettiğim çalışmanın doğruluğundan ve akademik dürüstlüğünden sorumlu olduğumu beyan ederim. |
| Öğrencinin adı-soyadı | Zeynep Yağmur Saklı |
| Tarih ve İmza | 20.11.2026 – Zeynep Yağmur Saklı |

## Kaynak

Anthropic. (2026). *Claude* [Büyük dil modeli]. https://claude.ai
