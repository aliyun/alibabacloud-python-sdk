# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearFaceDeviceDBRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_instance_id: str = None,
        isolation_id: str = None,
        product_key: str = None,
    ):
        # The name of the device corresponding to the V-series edge all-in-one machine. On the **Basic Information** tab of the **Host Details** page for the V-series edge all-in-one machine in the Edge Computing console, find the **Video Gateway** information and obtain the **DeviceName** value.
        # 
        # This parameter is required.
        self.device_name = device_name
        # The instance ID.
        # 
        # You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console. If an ID value exists, you must pass this ID value. Otherwise, the call fails.
        # 
        # > If a public instance does not have an ID value, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        self.iot_instance_id = iot_instance_id
        # The business isolation ID.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The unique identifier of the product to which the device corresponding to the V-series edge all-in-one machine belongs. On the **Basic Information** tab of the **Host Details** page for the V-series edge all-in-one machine in the Edge Computing console, find the **Video Gateway** information and obtain the **ProductKey** value.
        # 
        # This parameter is required.
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

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

