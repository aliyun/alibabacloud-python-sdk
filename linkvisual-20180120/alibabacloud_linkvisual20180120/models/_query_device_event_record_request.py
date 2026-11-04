# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDeviceEventRecordRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        event_id: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
    ):
        # The DeviceName of the IP camera (IPC) device.
        # You can view the **DeviceName** on the **Devices** page of the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The ID of the intelligent alert event. You can call the [QueryDeviceEvent](https://help.aliyun.com/document_detail/107916.html) operation to obtain the event ID.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The IotId of the IP camera (IPC) device. The IotId is the globally unique identifier of the device that is issued by IoT Platform. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the globally unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The ID of the instance.
        # 
        # <props="china">You can view the **ID** of the instance on the **Instance Overview** page of the IoT Platform console. If your instance has an ID, you must specify the ID. Otherwise, the call fails.
        # 
        # <props="china">
        # > If your public instance does not have an ID, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        # 
        # <props="intl">You do not need to specify this parameter.
        self.iot_instance_id = iot_instance_id
        # The ProductKey of the product to which the IP camera (IPC) device belongs.
        # You can view the ProductKey on the **Products** page of the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information of all products under the current account.
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

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

