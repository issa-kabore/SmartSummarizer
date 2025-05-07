from summarizer import INPUT_MIN_SIZE
from summarizer.models import summarizer_fr, summarizer_en
from summarizer.utils import detect_language, read_file


def generate_summary(text=None, file=None, min_length=30, max_length=100, do_sample=False):
    content = text or ""
    if file:
        content = read_file(file)
    content = content.strip()

    if not content or len(content.split()) < INPUT_MIN_SIZE:
        return "⚠️ Input too short or empty."
    
    # Model selection based on language detection
    lang = detect_language(content)
    if lang == "fr":
        summarizer = summarizer_fr
    elif lang == "en":
        summarizer = summarizer_en
    else:
        return f"❌ Unsupported language: {lang}"

    try:
        summary = summarizer(content, min_length=min_length, max_length=max_length, do_sample=do_sample)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"❌ Error: {str(e)}"
