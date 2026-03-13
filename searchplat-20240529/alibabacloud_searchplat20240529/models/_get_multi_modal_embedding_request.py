# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMultiModalEmbeddingRequest(DaraModel):
    def __init__(
        self,
        input: List[main_models.GetMultiModalEmbeddingRequestInput] = None,
        options: Dict[str, Any] = None,
    ):
        self.input = input
        self.options = options

    def validate(self):
        if self.input:
            for v1 in self.input:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['input'] = []
        if self.input is not None:
            for k1 in self.input:
                result['input'].append(k1.to_map() if k1 else None)

        if self.options is not None:
            result['options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.input = []
        if m.get('input') is not None:
            for k1 in m.get('input'):
                temp_model = main_models.GetMultiModalEmbeddingRequestInput()
                self.input.append(temp_model.from_map(k1))

        if m.get('options') is not None:
            self.options = m.get('options')

        return self

class GetMultiModalEmbeddingRequestInput(DaraModel):
    def __init__(
        self,
        image: str = None,
        text: str = None,
    ):
        self.image = image
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

