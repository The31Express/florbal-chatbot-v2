Projekt: Chatbot, který pomáhá se začátky s florbalem

Jak chatbot funguje? Úplně jednoduše; napíšeme dotaz do okénka na stránce, stisknete "Odeslat". Hned na to se dotaz odešle na AI na internetu (Gemma3:27b), ta odpoví a odpověď se zobrazí na stránce. Následná konverzace se ukládá do databáze.

Spuštění: docker compose up --build

Port: 8081

Endpointy:
GET /ping
GET /status
GET /save
POST /ai

Databáze: PostgreSQL, ukládá dotaz a odpověď

Test lze na URL http://localhost:8081/ping
