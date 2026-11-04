# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchQueryVisionDeviceInfoRequest(DaraModel):
    def __init__(
        self,
        device_name_list: List[str] = None,
        iot_id_list: List[str] = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        self.device_name_list = device_name_list
        self.iot_id_list = iot_id_list
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list

        if self.iot_id_list is not None:
            result['IotIdList'] = self.iot_id_list

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')

        if m.get('IotIdList') is not None:
            self.iot_id_list = m.get('IotIdList')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

