# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordUrlRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        file_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        product_key: str = None,
        seek_time: int = None,
        url_valid_duration: int = None,
    ):
        # The DeviceName of the IP camera.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The name of the cloud recording file. You can call the [QueryRecord](https://help.aliyun.com/document_detail/107922.html) operation to query the file name.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The IotId of the IP camera. The IotId is the unique identifier that is issued by IoT Platform to the device. You can call the IoT Platform [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the IotId.
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
        # The ProductKey of the product to which the IP camera belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The playback offset time of the recording, in seconds. Default value: 0.
        self.seek_time = seek_time
        # The validity period of the URL, in seconds. Valid values: 10 to 3600.
        self.url_valid_duration = url_valid_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time

        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')

        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')

        return self

