# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePurchasedDeviceResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        order_id: str = None,
        region: str = None,
        register_code: str = None,
        request_id: str = None,
        sub_type: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.id = id
        self.name = name
        self.order_id = order_id
        self.region = region
        self.register_code = register_code
        self.request_id = request_id
        self.sub_type = sub_type
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region is not None:
            result['Region'] = self.region

        if self.register_code is not None:
            result['RegisterCode'] = self.register_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

