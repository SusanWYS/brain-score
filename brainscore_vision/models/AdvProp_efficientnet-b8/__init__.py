from brainscore_vision import model_registry
from brainscore_vision.model_helpers.brain_transformation import ModelCommitment
from .model import get_model, get_layers

model_registry['AdvProp_efficientnet-b8'] = lambda: ModelCommitment(identifier='AdvProp_efficientnet-b8', activations_model=get_model('AdvProp_efficientnet-b8'), layers=get_layers('AdvProp_efficientnet-b8'))