# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreatePropertyRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_key: str = None,
        property_values: List[str] = None,
    ):
        self.business_channel = business_channel
        # The property name.
        # 
        # This parameter is required.
        self.property_key = property_key
        # The values of the property. You can specify up to 50 values for a property.
        self.property_values = property_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.property_key is not None:
            result['PropertyKey'] = self.property_key

        if self.property_values is not None:
            result['PropertyValues'] = self.property_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')

        return self

