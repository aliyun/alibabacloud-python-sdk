# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStreamPushJobRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_id: str = None,
        product_key: str = None,
    ):
        # The DeviceName of the device.
        # You can view the **DeviceName** on the **Devices** page of the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The ID of the device. This is the unique identifier issued by IoT Platform for the device. You can call [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) of IoT Platform to query the device ID.
        # 
        # >Notice:  **IotId** is the globally unique identifier of a device and corresponds to a combination of **ProductKey** and **DeviceName** on a one-to-one basis. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify **IotId** together with **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the ID of the current instance on the **Overview** tab of the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ProductKey of the product to which the device belongs.
        # You can view the ProductKey on the **Products** page of the IoT Platform console or call [QueryProductList](https://help.aliyun.com/document_detail/69271.html) to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
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

        if self.job_id is not None:
            result['JobId'] = self.job_id

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

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

