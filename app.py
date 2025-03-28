from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
import os


app = Flask(__name__)

# OpenAI API anahtarını ortam değişkeninden alıyoruz
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


@app.route('/sentiment-segmentation', methods=['POST'])
def sentiment_segmentation():
    data = request.get_json()
    text = data.get("text", "")

    # Prompt: Metni segmentlere ayır, her segmenti numaralandır ve segmentin duygusal tonunu belirt (Pozitif, Negatif, Nötr)
    prompt = (
        f"Lütfen aşağıdaki metni anlamlı segmentlere ayır ve her bir segmentin duygusal tonunu belirle.\n"
        f"Duygusal tonlar: Pozitif, Negatif, Nötr.\n"
        f"Her segment için numara, segment metni ve duygu etiketini belirt.\n\n"
        f"Metin: \"{text}\"\n\n"
        "Örnek çıktı formatı:\n"
        "1. Segment: <segment metni> - Duygu: Pozitif\n"
        "2. Segment: <segment metni> - Duygu: Negatif\n"
        "..."
    )

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Kullanılacak model; ihtiyaca göre değiştirilebilir
            prompt=prompt,
            max_tokens=300,  # Metnin uzunluğuna göre ayarlanabilir
            temperature=0.5
        )

        result = response.choices[0].text.strip()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
