<template>
  <div class="container-fluid text-center">
    <div class="row">
      <div class="col-2" style="background-color: black; height: 100vh;">
        <div class="row left_elements">
          <div class="alert alert-success" style="font-weight: bold;" role="alert">
            Wählen Sie ein Beispiel aus:
          </div>
        </div>
        <div class="row left_elements">
          <button type="button" class="btn btn-secondary left-btns" 
            :class="{'btn-success': ex01_isActive}" @click="ex01_setText">
            Beispiel 01: Quetion Answering (Zero-Shot vs Few-Shot)
          </button>
        </div>
        <div class="row left_elements">
          <button type="button" class="btn btn-secondary left-btns" 
            :class="{'btn-success': ex02_isActive}" @click="ex02_setText">
            Beispiel 02: Quetion Answering (Few-Shot vs Few-Shot Chain of Thought)
          </button>
        </div>
        <div class="row left_elements">
          <button type="button" class="btn btn-secondary left-btns" 
            :class="{'btn-success': ex03_isActive}" @click="ex03_setText">
            Beispiel 03: Quetion Answering (Zero-Shot vs Few-Shot Self-Consistency)
          </button>
        </div>
      </div>
      <div class="col-10" style="background-color: #343541;">
        <div class="row left_elements">
          <div class="col-8" style="float: left;">
            <div class="alert alert-success" style="font-weight: bold;" role="alert">
              Model: {{ modelName }}
            </div>
          </div>
          <div class="col-2 align-items-center">
            <button type="button" class="btn btn-secondary" :class="{'btn-success': openai_isActive}" @click="setModel('GPT 3.5 Turbo')">OpenAI API</button>
          </div>
          <div class="col-2 align-items-start">
            <button type="button" class="btn btn-secondary" :class="{'btn-success': together_isActive}" @click="setModel('llama-2-70b-chat')">Together API</button>
          </div>
          
        </div>
        <div class="row" id="ex01-question-answering" :style="contentRowStyle">
          <div class="col-6">
            <div class="row">
              <div class="col-12">
                <div class="alert alert-primary" role="alert">
                  {{promptType_01}}
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <textarea v-model="prompt_1" placeholder="Geben Sie Ihren Text ein" :style="textareaStyle01"></textarea>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <button class="btn btn-primary" @click="getAIResponse(this.prompt_1, 'zero_shot', this.modelName)" :disabled="loading">
                  <span v-if="loading_1" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                  <span v-else>Senden</span>
                </button>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <p style="color: white; height: auto; text-align: left;">Antwort: {{ aiResponse_1 }}</p>
              </div>
            </div>
          </div>
          <div class="col-6">
            <div class="row">
              <div class="col-12">
                <div class="alert alert-primary" role="alert">
                  {{promptType_02}}
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <textarea v-model="prompt_2" placeholder="Geben Sie Ihren Text ein" :style="textareaStyle02"></textarea>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <button class="btn btn-primary" @click="getAIResponse(this.prompt_2, 'few_shot', this.modelName)" :disabled="loading">
                  <span v-if="loading_2" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                  <span v-else>Senden</span>
                </button>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <p style="color: white; height: auto; text-align: left;">Antwort: {{ aiResponse_2 }}</p>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AIPrompt',
  data() {
    return {
      modelName: 'GPT 3.5 Turbo',
      prompt_1: '',
      prompt_2: '',
      aiResponse_1: '',
      aiResponse_2: '',
      loading_1: false,
      loading_2: false,
      prompting_type: "",
      textareaStyle01: {
        height: '200px',
      },
      textareaStyle02: {
        height: '200px',
      },
      openai_isActive: true,
      together_isActive : false,
      ex01_isActive: false,
      ex02_isActive : false,
      ex03_isActive : false,
      contentRowStyle: {
        height: '700px',
      },
      promptType_01: '',
      promptType_02: '',
    }
  },
  methods: {
    setModel(name) {
      this.modelName = name;
      if (name == 'GPT 3.5 Turbo') {
        this.openai_isActive = !this.openai_isActive;
        this.together_isActive = false;
      }
      if (name == 'llama-2-70b-chat') {
        this.openai_isActive = false;
        this.together_isActive = !this.together_isActive;
      }
      
      
    },
    ex01_setText() {
      this.promptType_01 = 'Zero-Shot Prompting'
      this.promptType_02 = 'Few-Shot Prompting'
      this.aiResponse_1 = ''
      this.aiResponse_2 = ''
      this.ex01_isActive = !this.ex01_isActive
      this.ex02_isActive = false
      this.ex03_isActive = false
      this.prompt_1 = "Was sind die empfohlenen Behandlungen für Bluthochdruck?";
      this.prompt_2 = "Frage 1: Was ist die Hauptfunktion des Herzens im menschlichen Körper?\n" +
                      "Antwort 1: Die Hauptfunktion des Herzens besteht darin, Blut durch den Körper zu " +
                      "pumpen, Sauerstoff und Nährstoffe zu den Geweben zu transportieren und Kohlendioxid " +
                      "sowie andere Abfallstoffe zu entfernen.\n\n" +
                      "Frage 2: Können Sie erklären, was die gewöhnliche Erkältung verursacht?\n" +
                      "Antwort 2: Die gewöhnliche Erkältung wird hauptsächlich durch Rhinoviren verursacht. " +
                      "Sie verbreitet sich durch luftgetragene Tröpfchen, wenn eine infizierte Person hustet oder " +
                      "niest, oder durch direkten Kontakt mit infizierten Oberflächen.\n\n" +
                      "Frage 3: Was sind die typischen Symptome von Diabetes?\n" +
                      "Antwort 3: Typische Symptome von Diabetes umfassen erhöhten Durst, häufiges " +
                      "Urinieren, Hunger, Müdigkeit und verschwommenes Sehen. In einigen Fällen kann es auch " +
                      "zu einem Gewichtsverlust kommen, trotz eines gesteigerten Appetits.\n\n" +
                      "Neue Frage: Was sind die empfohlenen Behandlungen für Bluthochdruck?"; 
      this.textareaStyle02.height = "355px";
                      
    },
    ex02_setText() {
      this.promptType_01 = 'Few-Shot Prompting'
      this.promptType_02 = 'Few-Shot-CoT Prompting'
      this.aiResponse_1 = ''
      this.aiResponse_2 = ''
      this.ex01_isActive = false
      this.ex02_isActive = !this.ex02_isActive
      this.ex03_isActive = false
      this.prompt_1 = "F: Roger hat 5 Tennisbälle. Er kauft noch 2 Dosen Tennisbälle. Jede Dose enthält 3 " +
                      "Tennisbälle. Wie viele Tennisbälle hat er jetzt?\n" +
                      "A: Die Antwort ist 11.\n\n" +
                      "F: Ein Jongleur kann 16 Bälle jonglieren. Die Hälfte der Bälle sind Golfbälle, und die Hälfte " +
                      "der Golfbälle sind blau. Wie viele blaue Golfbälle gibt es?\n" +
                      "A:";
      this.prompt_2 = "F: Roger hat 5 Tennisbälle. Er kauft noch 2 Dosen Tennisbälle. Jede Dose enthält 3 " +
                      "Tennisbälle. Wie viele Tennisbälle hat er jetzt?\n" +
                      "A: Roger startete mit 5 Bällen. 2 Dosen mit jeweils 3 Tennisbällen sind 6 Tennisbälle. 5 + 6 " +
                      "= 11. Die Antwort ist 11.\n\n" +
                      "F: Ein Jongleur kann 16 Bälle jonglieren. Die Hälfte der Bälle sind Golfbälle, und die Hälfte " +
                      "der Golfbälle sind blau. Wie viele blaue Golfbälle gibt es?\n"
                      "A:"; 
      this.textareaStyle01.height = "220px";
      this.textareaStyle02.height = "220px";
    },
    ex03_setText() {
      this.promptType_01 = 'Zero-Shot Prompting'
      this.promptType_02 = 'Few-Shot-Self-Consistency Prompting'
      this.aiResponse_1 = ''
      this.aiResponse_2 = ''
      this.ex01_isActive = false
      this.ex02_isActive = false
      this.ex03_isActive = !this.ex03_isActive
      this.prompt_1 = "Als ich 6 Jahre alt war, war meine Schwester halb so alt wie ich. Jetzt bin ich 70, wie alt ist " +
                      "meine Schwester??";
      this.prompt_2 = "F: In der Baumgruppe stehen 15 Bäume. Heute werden die Arbeiter der Baumgruppe " +
                      "Bäume pflanzen. Nachdem sie fertig sind, wird es 21 Bäume geben. Wie viele Bäume " +
                      "haben die Arbeiter heute gepflanzt?\n" +
                      "A: Wir starten mit 15 Bäumen. Später haben wir 21 Bäume. Die Differenz muss die Anzahl " +
                      "der gepflanzten Bäume sein. Also müssen sie 21 - 15 = 6 Bäume gepflanzt haben. Die " +
                      "Antwort ist 6.\n\n" +

                      "F: Wenn es 3 Autos auf dem Parkplatz gibt und 2 weitere Autos ankommen, wie viele " +
                      "Autos sind auf dem Parkplatz?\n" +
                      "A: Es sind bereits 3 Autos auf dem Parkplatz. 2 weitere kommen hinzu. Jetzt gibt es 3 + 2 = " +
                      "5 Autos. Die Antwort ist 5.\n\n" +

                      "F: Leah hatte 32 Schokoladen und ihre Schwester hatte 42. Wenn sie 35 gegessen haben, " +
                      "wie viele Stücke haben sie insgesamt noch übrig?\n" +
                      "A: Leah hatte 32 Schokoladen und Leahs Schwester hatte 42. Das bedeutet, ursprünglich " +
                      "gab es 32 + 42 = 74 Schokoladen. 35 wurden gegessen. Also haben sie insgesamt noch 74 " +
                      "- 35 = 39 Schokoladen. Die Antwort ist 39.\n\n" +

                      "F: Jason hatte 20 Lutscher. Er gab Denny einige Lutscher. Jetzt hat Jason 12 Lutscher. Wie " +
                      "viele Lutscher hat Jason an Denny gegeben?\n" +
                      "A: Jason hatte 20 Lutscher. Da er jetzt nur noch 12 hat, muss er den Rest an Denny " +
                      "gegeben haben. Die Anzahl der Lutscher, die er Denny gegeben hat, muss 20 - 12 = 8 " +
                      "Lutscher sein. Die Antwort ist 8.\n\n" +

                      "F: Shawn hatte fünf Spielzeuge. Zu Weihnachten bekam er je zwei Spielzeuge von seiner " +
                      "Mutter und seinem Vater. Wie viele Spielzeuge hat er jetzt?\n" +
                      "A: Er hat 5 Spielzeuge. Er bekam 2 von der Mutter, also hatte er danach 5 + 2 = 7 " +
                      "Spielzeuge. Dann bekam er noch 2 vom Vater, also insgesamt hat er jetzt 7 + 2 = 9 " +
                      "Spielzeuge. Die Antwort ist 9.\n\n" +

                      "F: Im Serverraum waren neun Computer. Von Montag bis Donnerstag wurden täglich fünf " +
                      "weitere Computer installiert. Wie viele Computer sind jetzt im Serverraum?\n" +
                      "A: Es gibt 4 Tage von Montag bis Donnerstag. Jeden Tag wurden 5 Computer hinzugefügt. " +
                      "Das bedeutet, insgesamt wurden 4 * 5 = 20 Computer hinzugefügt. Anfangs gab es 9 " +
                      "Computer, also gibt es jetzt 9 + 20 = 29 Computer. Die Antwort ist 29.\n\n" +

                      "F: Michael hatte 58 Golfbälle. Am Dienstag verlor er 23 Golfbälle. Am Mittwoch verlor er 2 " +
                      "weitere. Wie viele Golfbälle hatte er am Ende des Mittwochs?\n" +
                      "A: Michael hatte anfangs 58 Bälle. Er verlor 23 am Dienstag, also hatte er danach 58 - 23 = " +
                      "35 Bälle. Am Mittwoch verlor er 2 weitere, also hat er jetzt 35 - 2 = 33 Bälle. Die Antwort ist 33.\n\n" +

                      "F: Olivia hat 23 Dollar. Sie kaufte fünf Bagels für je 3 Dollar. Wie viel Geld hat sie übrig?\n" +
                      "A: Sie kaufte 5 Bagels für je 3 Dollar. Das bedeutet, sie gab 15 Dollar aus. Sie hat 8 Dollar übrig.\n\n" +

                      "F: Als ich 6 war, war meine Schwester halb so alt wie ich. Jetzt bin ich 70, wie alt ist meine Schwester?\n" +
                      "A:"; 
      this.textareaStyle02.height = "383px";
                      
    },
    async getAIResponse(prompt_text, prompt_type, modelName) {
      if (modelName == 'GPT 3.5 Turbo') {
        if (prompt_type == "few_shot"){
          this.loading_2 = true; // Set loading to true when the request starts
          try {
            const response = await axios.post('http://localhost:8000/openai/', `prompt=${prompt_text}`, {
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              }
            });
            this.aiResponse_2 = response.data.response;
            this.contentRowStyle.height = 'auto';
          } catch (error) {
            console.error("There was an error fetching the AI response:", error);
            // Handle error (e.g., show error message)
          } finally {
            this.loading_2 = false; // Reset loading state once the request is complete
          }
        }
        if (prompt_type == "zero_shot"){
          this.loading_1 = true; // Set loading to true when the request starts
          try {
            const response = await axios.post('http://localhost:8000/openai/', `prompt=${prompt_text}`, {
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              }
            });
            this.aiResponse_1 = response.data.response;
            this.contentRowStyle.height = 'auto';
          } catch (error) {
            console.error("There was an error fetching the AI response:", error);
            // Handle error (e.g., show error message)
          } finally {
            this.loading_1 = false; // Reset loading state once the request is complete
          }
        }
      }
      else if (modelName == 'llama-2-70b-chat') 
      {
        if (prompt_type == "few_shot"){
          this.loading_2 = true; // Set loading to true when the request starts
          try {
            const response = await axios.post('http://localhost:8000/together/', `prompt=${prompt_text}`, {
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              }
            });
            this.aiResponse_2 = response.data.response;
            this.contentRowStyle.height = 'auto';
          } catch (error) {
            console.error("There was an error fetching the AI response:", error);
            // Handle error (e.g., show error message)
          } finally {
            this.loading_2 = false; // Reset loading state once the request is complete
          }
        }
        if (prompt_type == "zero_shot"){
          this.loading_1 = true; // Set loading to true when the request starts
          try {
            const response = await axios.post('http://localhost:8000/together/', `prompt=${prompt_text}`, {
              headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
              }
            });
            this.aiResponse_1 = response.data.response;
            this.contentRowStyle.height = 'auto';
          } catch (error) {
            console.error("There was an error fetching the AI response:", error);
            // Handle error (e.g., show error message)
          } finally {
            this.loading_1 = false; // Reset loading state once the request is complete
          }
        }
      }
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  text-align: center;
  color: #2c3e50;
  
}
html, body {
  height: 100%;
  margin: 0; /* Remove default margin */
  background-color: #343541 !important;
}
.row .left_elements {
  padding: 10px;
}
.left_elements .left-btns {
  padding: 30px;
  font-weight: bold;
}
textarea {
  width: 100%;
  margin-bottom: 20px !important;
}
#ex01-question-answering {
  display: show;
}

</style>
