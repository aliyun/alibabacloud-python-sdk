# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGbDeviceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        device_name: str = None,
        gb_id: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        password: str = None,
        product_key: str = None,
    ):
        self.description = description
        self.device_name = device_name
        self.gb_id = gb_id
        self.iot_id = iot_id
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        self.password = password
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.gb_id is not None:
            result['GbId'] = self.gb_id

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

