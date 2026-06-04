# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateColumnBusinessMetadataShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_attributes_shrink: str = None,
        description: str = None,
        id: str = None,
    ):
        self.custom_attributes_shrink = custom_attributes_shrink
        # The field business description.
        self.description = description
        # The field ID. You can refer to the response from the ListColumns operation. You can also refer to the [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_attributes_shrink is not None:
            result['CustomAttributes'] = self.custom_attributes_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAttributes') is not None:
            self.custom_attributes_shrink = m.get('CustomAttributes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

