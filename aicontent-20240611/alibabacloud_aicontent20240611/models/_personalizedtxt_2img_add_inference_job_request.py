# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Personalizedtxt2imgAddInferenceJobRequest(DaraModel):
    def __init__(
        self,
        image_number: int = None,
        model_id: str = None,
        prompt: str = None,
        seed: int = None,
    ):
        # The number of images to generate. Note: Due to resource limits in the test environment, a maximum of 10 images can be generated at a time. If this value is greater than 10, it is treated as 10.
        self.image_number = image_number
        # The ID of the model training task. Specifies the model to use for inference.
        # 
        # This parameter is required.
        self.model_id = model_id
        # The English prompt that describes the image to be generated. Replace the character to be generated with <special-token>. For example, change "a man in the snow" to "a <special-token> in the snow" and "a photo of a girl" to "a photo of a <special-token>".
        # 
        # This parameter is required.
        self.prompt = prompt
        # The random seed. A fixed seed generates the same image and ensures the reproducibility of the results. Note: The input value must be in the range of [-1, 2147483647]. If the input value is out of this range or not provided, a suitable seed is automatically generated.
        self.seed = seed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_number is not None:
            result['imageNumber'] = self.image_number

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.seed is not None:
            result['seed'] = self.seed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageNumber') is not None:
            self.image_number = m.get('imageNumber')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('seed') is not None:
            self.seed = m.get('seed')

        return self

