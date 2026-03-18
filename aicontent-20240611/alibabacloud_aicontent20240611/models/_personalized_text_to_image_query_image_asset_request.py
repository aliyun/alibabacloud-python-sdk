# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PersonalizedTextToImageQueryImageAssetRequest(DaraModel):
    def __init__(
        self,
        encode_format: str = None,
        image_id: str = None,
    ):
        self.encode_format = encode_format
        # This parameter is required.
        self.image_id = image_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encodeFormat') is not None:
            self.encode_format = m.get('encodeFormat')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        return self

