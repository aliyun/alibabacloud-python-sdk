# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PersonalizedTextToImageAddInferenceJobRequest(DaraModel):
    def __init__(
        self,
        image_number: int = None,
        image_url: List[str] = None,
        prompt: str = None,
        seed: int = None,
        strength: float = None,
        train_steps: int = None,
    ):
        # The number of images to generate. Note: The maximum is 10 images per request in the test environment. If the value exceeds 10, it is treated as 10.
        self.image_number = image_number
        # An array containing one or more image URLs. For example, `["url_1", "url_2", ...]`.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The English prompt for image generation. Use the placeholder for the subject. For example, change "a man in the snow" to "a in the snow".
        # 
        # This parameter is required.
        self.prompt = prompt
        # A random seed to ensure reproducible image generation. The value must be within `[-1, 2147483647]`. If the value is outside this range or omitted, the system automatically generates a seed.
        self.seed = seed
        # Determines the influence of the reference image.
        # Valid values: `0.3`, `0.4`, `0.5`, `0.6`, `0.7`, and `0.8`.
        # A lower value decreases the influence of the reference image and increases the influence of the text prompt.
        # The default is `0.5`, and you typically do not need to change this value.
        self.strength = strength
        # The number of training steps for the model.
        self.train_steps = train_steps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_number is not None:
            result['imageNumber'] = self.image_number

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.seed is not None:
            result['seed'] = self.seed

        if self.strength is not None:
            result['strength'] = self.strength

        if self.train_steps is not None:
            result['trainSteps'] = self.train_steps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageNumber') is not None:
            self.image_number = m.get('imageNumber')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('seed') is not None:
            self.seed = m.get('seed')

        if m.get('strength') is not None:
            self.strength = m.get('strength')

        if m.get('trainSteps') is not None:
            self.train_steps = m.get('trainSteps')

        return self

