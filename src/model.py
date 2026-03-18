from ultralytics import RTDETR


def load_rtdetr(model_name="../rtdetr-l.pt"):
    model = RTDETR(model_name)
    return model
