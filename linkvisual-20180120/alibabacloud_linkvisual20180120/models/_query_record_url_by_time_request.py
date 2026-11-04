# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordUrlByTimeRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        stream_type: int = None,
        url_valid_duration: int = None,
    ):
        # The start time of the query range. The value is a 10-digit timestamp in seconds.
        # 
        # The minimum value is 0, and the maximum value is 2147483647.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The DeviceName of the IP camera.
        # You can view the **DeviceName** on the **Devices** page of the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The end time of the query range. The value is a 10-digit timestamp in seconds.
        # 
        # The minimum value is 0, and the maximum value is 2147483647.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The IotId of the IP camera. The IotId is the unique identifier issued by IoT Platform for the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID.
        # 
        # You can view the **ID** of the current instance on the **Instance Overview** page of the IoT Platform console. If the instance has an ID, you must specify this ID. Otherwise, the call fails.
        # 
        # > If the public instance does not have an ID, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        self.iot_instance_id = iot_instance_id
        # The ProductKey of the product to which the IP camera belongs.
        # You can view the ProductKey on the **Products** page of the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The type of the video stream. Valid values:
        # 
        # - **0** (default): main stream
        # - **1**: sub stream
        self.stream_type = stream_type
        # The validity period of the URL. Valid values: 10 to 3600. Unit: seconds.
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')

        return self

