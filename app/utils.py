import torch

def result(keyword: str, top_k: int) -> [str]:
    """
    返回检索文件id

    参数:
    keyword (str): query
    top_k (int): 返回的文档数量

    返回:
    [str]: 返回的文档id
    """
    tensors = tokenize(keyword)
    result = token_match(tensors, top_k)
    if result is None:
        return []
    elif result[0][0].__class__ == int:
        return [(str(x[0]), x[1]) for x in result]
    else:
        return result

def tokenize(keyword: str) -> torch.Tensor:
    """
    生成query的向量

    参数:
    keyword (str): query

    返回:
    torch.tensor: query的向量
    """
    pass

def token_match(tokens: torch.Tensor, top_k: int) -> [(str | int, int)]:
    """
    稠密向量检索
    
    参数:
    tokens (torch.tensor): query的向量
    top_k (int): 返回的文档数量

    返回:
    [(str | int, int)]: (返回的文档id, score)
    """
    return [(31, 100), (32, 90)]