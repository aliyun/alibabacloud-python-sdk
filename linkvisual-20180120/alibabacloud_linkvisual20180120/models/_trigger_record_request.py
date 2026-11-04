# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerRecordRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        pre_record_duration: int = None,
        product_key: str = None,
        record_duration: int = None,
        stream_type: int = None,
    ):
        # The DeviceName of the IPC device. You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The IotId of the IPC device. The IotId is the unique identifier that is issued by IoT Platform to the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID.
        # 
        # <props="china">You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console. If the instance has an ID, you must specify the ID. Otherwise, the call fails.
        # 
        # <props="china">
        # > If the public instance does not have an ID, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        # 
        # <props="intl">You do not need to specify this parameter.
        self.iot_instance_id = iot_instance_id
        # The pre-recording duration. Valid values: 0 to 10. Unit: seconds.
        # 
        # >The pre-recording duration is generated only when the device supports the pre-recording feature. Otherwise, the pre-recording duration is 0.
        self.pre_record_duration = pre_record_duration
        # The ProductKey of the product to which the IPC device belongs. You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The recording duration, including the pre-recording duration. Valid values: 10 to 7200. Unit: seconds.
        # 
        # > The maximum length of a single recording file is 30 minutes. If the recording duration exceeds 30 minutes, the recording is automatically split into multiple recording files.
        # 
        # This parameter is required.
        self.record_duration = record_duration
        # The stream type. Valid values:
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
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

