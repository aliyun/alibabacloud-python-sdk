# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectFaceAttributesRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        material_value: str = None,
    ):
        # Identifier for the business scenario using real-person authentication services.
        self.biz_type = biz_type
        # The photo to be detected, see the instructions for uploading image addresses for format description. A maximum of 5 faces can be detected in a single image.
        # 
        # This parameter is required.
        self.material_value = material_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.material_value is not None:
            result['MaterialValue'] = self.material_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('MaterialValue') is not None:
            self.material_value = m.get('MaterialValue')

        return self

