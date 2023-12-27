import nltk
import pyter

# Install the punkt package for tokenization
nltk.download('punkt')

# Texts to compare
reference_text = "Привіт, як справи?"
candidate_text = "Привіт, як ся маєш?"

# Tokenize the texts
reference_tokens = nltk.word_tokenize(reference_text.lower())
candidate_tokens = nltk.word_tokenize(candidate_text.lower())

# BLEU score
bleu_score = nltk.translate.bleu_score.sentence_bleu([reference_tokens], candidate_tokens)

# METEOR score
meteor_score = nltk.translate.meteor_score.single_meteor_score(reference_text, candidate_text)

# TER score
ter_score = pyter.ter(reference_tokens, candidate_tokens)

# ROUGE score
rouge = nltk.translate.bleu_score.SmoothingFunction()
rouge_score = nltk.translate.bleu_score.sentence_bleu([reference_tokens], candidate_tokens, smoothing_function=rouge.method1)

# Display scores
print(f"BLEU Score: {bleu_score}")
print(f"METEOR Score: {meteor_score}")
print(f"TER Score: {ter_score}")
print(f"ROUGE Score: {rouge_score}")
