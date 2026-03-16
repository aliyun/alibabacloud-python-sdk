# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckUsedPropertyRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_id: int = None,
    ):
        self.business_channel = business_channel
        # The ID of the property. You can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        return self

