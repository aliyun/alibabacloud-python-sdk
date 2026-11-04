# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVoiceIntercomRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        scheme: str = None,
    ):
        # The DeviceName of the IPC device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The device ID of the IPC device. The ID is issued by IoT Platform and is the unique identifier of the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the ID.
        # 
        # >Notice:  As the unique identifier of the device, **IotId** has a one-to-one mapping with the combination of **ProductKey** and **DeviceName**. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If an **ID** value is available, you must specify the **ID**. Otherwise, the call fails.
        # - If the **Instance Overview** page or the **ID** value is not available, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The **ProductKey** of the product to which the IPC device belongs.
        # You can view the information about all products under the current account on the **Products** page in the IoT Platform console or by calling the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The connection protocol type for voice intercom. Valid values:
        # 
        # - **ws**: WebSocket. Call this operation to obtain the web voice call address when you implement the voice intercom feature on web clients. <props="china"><ph>For more information about how to implement the voice intercom feature between web clients and devices, see [Web voice intercom integration guide](https://help.aliyun.com/document_detail/2545966.html).</ph>
        # - **rtmp** (default): Real-Time Messaging Protocol (RTMP). Call this operation to obtain the corresponding voice call address when you implement the voice intercom feature by using players in Android and iOS applications. For more information about how to implement the voice intercom feature between Android and iOS applications and devices, see [Android voice intercom](https://help.aliyun.com/document_detail/260925.html) and [iOS voice intercom](https://help.aliyun.com/document_detail/253953.html).
        self.scheme = scheme

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

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        return self

