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
        # The number of images to generate. Note: Due to resource limits in the test environment, you can generate up to 10 images per request. The system automatically sets values greater than 10 to 10.
        self.image_number = image_number
        # The model ID to use for the inference job.
        # 
        # This parameter is required.
        self.model_id = model_id
        # An English prompt describing the image to generate. Replace the subject with . For example, change "a man in the snow" to "a in the snow", and "a photo of a girl" to "a photo of a ".
        # 
        # This parameter is required.
        self.prompt = prompt
        # The seed for the random number generator. Using the same seed ensures reproducible results. The value must be between -1 and 2,147,483,647. If the value is outside this range or is not specified, the system automatically generates a suitable seed.
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

