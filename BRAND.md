# Bronla sosial media bələdçisi

Bronla: gözəllik ustaları (bərbər, saç ustası, dırnaq ustası, vizajist) üçün qəbul tətbiqi.
Funksiyalar: qəbul təqvimi, müştərinin linkdən özü yazılması, WhatsApp xatırlatması və toplu mesaj, müştəri kartı, rəylər, hesabat.

## Qaydalar
- Ünvan hər yerdə `bronla.me` yazılır (bronla.az yox).
- Şüar: "Bronla, gəl!". "Zəng et. Bronla. Gəl." heç yerdə yazılmır.
- Dil: Azərbaycan dili, "siz" forması, emoji yoxdur.
- Vəziyyət: hazırda veb tətbiqdir, tezliklə App Store və Google Play-də olacaq. Mağazalarda olduğunu yazmaq olmaz.
- Posterlərdəki ad və rəqəmlər nümunədir; real statistika, real müştəri rəyi və qiymət kimi təqdim etmək olmaz. Qiymət yazılmır.
- Rənglər: #1747D8, qradiyent #0B2A8F → #2A63F5, mətn #0B1B33. Loqo: `design/lib.py` içindəki "təsdiqli b".
- Format: 1080×1350 JPEG. Yuxarıda iki hissəli başlıq (fakt + mavi sual və ya nəticə), bir sətir izah, ortada bir vizual metafora, aşağıda loqo və bronla.me.

## Fayllar
- `posts.json`: paylaşım növbəsi. `instagram` və `facebook` sahələri boşdursa, hələ paylaşılmayıb.
- `posts/`: hazır posterlər.
- `design/`: posterləri çəkən kod (Python + Playwright, Chrome ilə).
