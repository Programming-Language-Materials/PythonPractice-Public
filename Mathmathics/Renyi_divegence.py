import torch

def Renyi_Divergence(x, y, T, alpha=0.99):
    """
    Renyi divergence. (generalisation of the Shannon entropy and the Kullback–Leibler divergence.)

    x: output of the last layer of student model
    y: output of the last layer of teacher model

    If alpha = 1, R_loss = KL_loss

    D_R(p||q) = (1/(alpha-1)) * log (sum p^alpha / q^(alpha-1))
    """
    n, _ = x.size()
    x = F.softmax(x / T, dim=1).pow(alpha - 1)
    y = F.softmax(y / T, dim=1).pow(alpha)

    return torch.log(torch.sum(y.div(x))) / (n * (alpha - 1))