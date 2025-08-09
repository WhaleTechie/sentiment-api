from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn.functional as F

class SentimentModel:
    def __init__(self):
        self.model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.model.eval()

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad(): #prevents training mode, speeds up inference
            outputs = self.model(**inputs) #runs the forward pass on the model (PyTorch under the hood
            probs = F.softmax(outputs.logits, dim=1) #converts model’s raw scores (logits) into probabilities
            score, label_idx = torch.max(probs, dim=1) #picks the label with the highest probability.
            label = "POSITIVE" if label_idx.item() == 1 else "NEGATIVE"
            return {"label": label, "score": score.item()}
