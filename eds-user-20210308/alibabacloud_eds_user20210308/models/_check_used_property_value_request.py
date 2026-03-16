# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckUsedPropertyValueRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_id: int = None,
        property_value_id: int = None,
    ):
        self.business_channel = business_channel
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The ID of the property value. You can call the [ListProperty](~~ListProperty~~) operation to query the ID of the property value.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id

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

        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        return self

