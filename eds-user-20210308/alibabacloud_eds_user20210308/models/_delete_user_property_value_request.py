# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserPropertyValueRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_id: int = None,
        property_value_id: int = None,
        user_id: int = None,
    ):
        self.business_channel = business_channel
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The property value ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property value ID.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id
        # The user ID. You can call the [DescribeUsers](~~DescribeUsers~~) operation to query the user ID, which is the return value of the `Id` parameter.
        # 
        # This parameter is required.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

