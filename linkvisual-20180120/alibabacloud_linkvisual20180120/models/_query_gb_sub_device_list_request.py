# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryGbSubDeviceListRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        page_start: int = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        self.page_size = page_size
        self.page_start = page_start
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_start is not None:
            result['PageStart'] = self.page_start

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

