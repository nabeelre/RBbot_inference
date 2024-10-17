import json
import torch
import numpy as np

import RBbot_inference.architectures as arch

latest_model = "RBbot-quiet-shadow-131"


def load_model(model_name, model_root="models"):
    """
    Loads model saved as state_dict and applies DANN architecture
    """
    if model_name == "latest":
        model_name = latest_model

    with open(f"{model_root}/{model_name}-config.json") as f:
        config = json.load(f)

    model = arch.DANN(config)
    model.load_state_dict(
        torch.load(f'models/{model_name}.pth',
                   weights_only=True,
                   map_location=torch.device('cpu'))
    )
    model.eval()
    return model


if __name__ == "__main__":
    model = load_model("latest")

    trips = np.load("examples/ZTF_exs.npy")

    # Convert numpy array triplets to pytorch tensor and put them on the device
    trips_tensor = torch.Tensor(trips).to('cpu')

    # Run the model on the triplets
    output = model(trips_tensor)
    scores = output[0].detach().cpu().numpy()

    print(scores)

    # Scores should be nearly (not necessarily exactly) equivalent across devices
    # [0.58898365 0.0105183  0.3106985  0.98181677 0.98905903]
