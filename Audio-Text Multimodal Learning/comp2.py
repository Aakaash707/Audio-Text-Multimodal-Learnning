from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

def find(sentences): 
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/bert-base-nli-mean-tokens")
    model = AutoModel.from_pretrained("sentence-transformers/bert-base-nli-mean-tokens")

    tokens = {'input_ids':[], 'attention_mask':[]}

    for sentence in sentences:
        new_tokens = tokenizer.encode_plus(sentence, max_length = 128,
                                        truncation = True,   padding = 'max_length',
                                        return_tensors = 'pt')
        tokens['input_ids'].append(new_tokens['input_ids'][0])
        tokens['attention_mask'].append(new_tokens['attention_mask'][0])

    tokens['input_ids'] = torch.stack(tokens['input_ids'])
    tokens['attention_mask'] = torch.stack(tokens['attention_mask'])

    outputs = model(**tokens)

    embeddings = outputs.last_hidden_state

    attention = tokens["attention_mask"]
    mask = attention.unsqueeze(-1).expand(embeddings.shape).float()

    mask_embeddings = embeddings * mask

    summed = torch.sum(mask_embeddings, 1)

    counts = torch.clamp(mask.sum(1), min=1e-9)

    mean_pooled = summed/counts
    mean_pooled = mean_pooled.detach().numpy()
    return cosine_similarity([mean_pooled[0]], mean_pooled[1:])