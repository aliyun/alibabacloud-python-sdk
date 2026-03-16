# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetUserPropertyValueRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        property_id: int = None,
        property_value_id: int = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.business_channel = business_channel
        # The property ID. You can call the [ListProperty](~~ListProperty~~) operation to query the property ID.
        # 
        # This parameter is required.
        self.property_id = property_id
        # The ID of the property value. You can call the [ListProperty](~~ListProperty~~) operation to query the ID of the property value.
        # 
        # This parameter is required.
        self.property_value_id = property_value_id
        # The ID of the convenience user. You can call the [DescribeUsers](~~DescribeUsers~~) operation to query the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username of the convenience user.
        # 
        # This parameter is required.
        self.user_name = user_name

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

        if self.user_name is not None:
            result['UserName'] = self.user_name

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

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

