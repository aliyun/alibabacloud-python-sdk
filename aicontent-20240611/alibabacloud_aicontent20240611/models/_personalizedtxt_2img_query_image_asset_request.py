# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Personalizedtxt2imgQueryImageAssetRequest(DaraModel):
    def __init__(
        self,
        encode_format: str = None,
        image_id: str = None,
        model_id: str = None,
        prompt_id: str = None,
    ):
        self.encode_format = encode_format
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.prompt_id = prompt_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_format is not None:
            result['encodeFormat'] = self.encode_format

        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.prompt_id is not None:
            result['promptId'] = self.prompt_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encodeFormat') is not None:
            self.encode_format = m.get('encodeFormat')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('promptId') is not None:
            self.prompt_id = m.get('promptId')

        return self

