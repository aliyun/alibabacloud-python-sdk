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
        self.image_number = image_number
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.prompt = prompt
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

