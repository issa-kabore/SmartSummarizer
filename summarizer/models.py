from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load French summarizer
fr_model_name = "plguillou/t5-base-fr-sum-cnndm"
tokenizer_fr = AutoTokenizer.from_pretrained(fr_model_name)
model_fr = AutoModelForSeq2SeqLM.from_pretrained(fr_model_name)
summarizer_fr = pipeline("summarization", model=model_fr, tokenizer=tokenizer_fr)

# Load English summarizer
en_model_name = "facebook/bart-large-cnn"
tokenizer_en = AutoTokenizer.from_pretrained(en_model_name)
model_en = AutoModelForSeq2SeqLM.from_pretrained(en_model_name)
summarizer_en = pipeline("summarization", model=model_en, tokenizer=tokenizer_en)