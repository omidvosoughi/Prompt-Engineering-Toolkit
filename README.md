# Prompt Engineering Toolkit

Diese Anwendung beinhaltet Beispiele, um zu demonstrieren, wie man verschiedene Große Sprachmodelle (LLMs) und APIs für das Prompt Engineering verwendet. Sie ist als Werkzeug konzipiert, das zeigt, wie verschiedene Prompting-Techniken angewendet werden können, um spezifische Ergebnisse mit modernsten Sprachmodellen zu erzielen.

Prompt Engineering ist eine Technik, die verwendet wird, um effektiv mit KI-Sprachmodellen zu kommunizieren, indem sie dazu angeleitet werden, gewünschte Antworten zu generieren. Es spielt eine entscheidende Rolle dabei, den Nutzen und die Genauigkeit der Antworten von Modellen wie GPT (Generative Pre-trained Transformer) und anderen zu maximieren, indem die Eingabeaufforderungen sorgfältig gestaltet werden. Manche bekannten Prompt-Engineering-Techniken sind wie folgt:

 - Zero-shot Prompting: Interaktion mit dem Modell ohne Bereitstellung von Beispielen, basierend allein auf den Anweisungen des Prompts.
 - Few-shot Prompting: Beinhaltet einige Beispiele im Prompt, um die Antworten des Modells in eine bestimmte Richtung zu lenken.
 - Chain-of-thought Prompting: Ermutigt das Modell, "laut zu denken", indem komplexe Probleme in einfachere Schritte zerlegt werden.
 - Self-Consistency: Umfasst die Generierung mehrerer Antworten und Auswahl der konsistentesten, um Zuverlässigkeit zu gewährleisten.
 - Retrieval Augmented Generation (RAG): Verbessert Antworten durch Integration externer Informationen, die aus einer Datenbank oder dem Internet abgerufen werden.
 - Fine-tuning: Passt das Modell durch Training an einem spezifischen Datensatz an, um es auf spezielle Bedürfnisse oder Domänen zuzuschneiden.
 
# Verwendete Sprachmodelle

Diese Anwendung nutzt zwei fortschrittliche Sprachmodelle, um verschiedene Techniken des Prompt Engineerings zu demonstrieren:

 - GPT 3.5 Turbo von OpenAI API: Bekannt für seine Effizienz und breite Wissensbasis.
 - llama-2-70b-chat von Together.ai API: Ausgezeichnet durch seine Fähigkeit, menschenähnlichen Text auf Basis eines umfangreichen Internetwissens zu generieren.
 

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Anforderungen erfüllt haben:

- Sie haben [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) auf Ihrem System installiert.
- [Docker](https://docs.docker.com/engine/install/) and Docker Compose sind auf Ihrem System installiert.

## Projektstruktur

- `/frontend`: Dieses Verzeichnis enthält die Vue.js-Anwendung.
- `/backend`: Dieses Verzeichnis enthält die FastAPI-Anwendung.
- `docker-compose.yml`: Diese Datei definiert die Multi-Container-Docker-Anwendung.

## Ausführen der Anwendung

Um die Anwendung zu starten und auszuführen, folgen Sie diesen Schritten:

### 1. Klonen Sie das Repository.

```bash
git clone https://github.com/omidvosoughi/Prompt-Engineering-Toolkit.git
cd Prompt-Engineering-Toolkit
```

### 2. Mit Docker Compose bauen und ausführen

Verwenden Sie 'docker-compose', um sowohl die Frontend- als auch die Backend-Dienste zu bauen und auszuführen.

- Unter Linux:
```bash
sudo docker-compose up --build
```

- Unter Windows: Stellen Sie zunächst sicher, dass Ihr Docker Desktop gestartet ist, und führen Sie dann den folgenden Befehl aus
```bash
docker-compose up --build
```

Wenn es einen Fehler beim Installieren von Frontend-Abhängigkeiten über Docker gibt, verwenden Sie die folgenden Befehle. Stellen Sie sicher, dass vor der Ausführung dieses Befehls [Node.js](https://nodejs.org/en/download) auf Ihrem System installiert sein muss.
```bash
cd frontend
npm install
cd ..
docker-compose up --build
```

### 3. API Schlüsseleinstellung

- Erstellen Sie eine `.env`-Datei im Projektstamm, wenn es keine gibt.
- Fügen Sie Ihre API-Schlüssel für OpenAI und Together.ai hinzu:

```makefile
OPENAI_API_KEY=<dein_openai_api_schlüssel>
TOGETHER_AI_API_KEY=<dein_together_ai_api_schlüssel>
```

### 4. Zugriff auf die Anwendung

Nachdem die Container gestartet und in Betrieb sind, können Sie über den folgenden Link in Ihrem Webbrowser auf die Anwendung zugreifen.

- [http://localhost](http://localhost)




