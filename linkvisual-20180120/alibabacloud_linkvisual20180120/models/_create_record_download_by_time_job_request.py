# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecordDownloadByTimeJobRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        record_type: int = None,
        stream_type: int = None,
    ):
        # The start time. The value must be a 10-digit UNIX timestamp in seconds. Valid values: 0 to 2147483647.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The DeviceName of the video device. You can view the **DeviceName** of devices under a specified product on the **Devices** page in the [IoT Platform console](https://iot.console.aliyun.com/devices) or by calling the [QueryDevice](https://help.aliyun.com/document_detail/69905.html) operation.
        # 
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The end time. The value must be a 10-digit UNIX timestamp in seconds. Valid values: 0 to 2147483647. The value must be greater than the start time specified by **BeginTime**.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the video device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the ID.
        # 
        # >Notice:  **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the ID of the current instance on the **Instance Overview** tab in the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The **ProductKey** of the product to which the video device belongs.
        # 
        # You can view the information about all products under the current instance on the **Products** page in the [IoT Platform console](https://iot.console.aliyun.com/product) or by calling the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation.
        # 
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The recording type. Valid values:
        # 
        # - **0**: continuous recording.
        # - **1**: event recording.
        # - **2**: on-demand recording.
        # - **4**: local-to-cloud recording.
        # - **Empty**: all recordings.
        self.record_type = record_type
        # The stream type. Valid values:
        # 
        # - **0** (default): main stream.
        # - **1**: sub stream.
        self.stream_type = stream_type

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

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

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

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

