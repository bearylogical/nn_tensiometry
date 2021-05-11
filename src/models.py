import tensorflow as tf


class BaseModel:
    def __init__(self) -> None:
        self.model = None
    
    def build_model(self) -> None:
        raise NotImplementedError('Not Implemented')

    def compile_model(self) -> None:
        raise NotImplementedError('Not Implemented')

    def train(self)-> None:
        raise NotImplementedError('Not Implemented')

class PhysicsNNModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

    def build_model(self) -> None:
        return super().build_model()
    
    def compile_model(self) -> None:
        return super().compile_model()

    def train(self) -> None:
        return super().train()

class PhysicsNNModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()

    def build_model(self) -> None:
        model.
    
    def compile_model(self) -> None:
        return super().compile_model()

    def train(self) -> None:
        return super().train()



