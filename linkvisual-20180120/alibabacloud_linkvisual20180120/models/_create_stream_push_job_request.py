# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStreamPushJobRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_type: int = None,
        product_key: str = None,
        push_url: str = None,
        stream_type: int = None,
    ):
        # The name of the device. You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The ID of the device. The ID is issued by IoT Platform and is the unique identifier of the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  As the unique identifier of the device, **IotId** has a one-to-one mapping with the combination of **ProductKey** and **DeviceName**. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the ID of the current instance on the **Instance Overview** tab in the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The type of the stream pushing job. Valid values:
        # 
        # - **1** (default): continuous job.
        # - **2**: triggered job, which ends after an interruption.
        self.job_type = job_type
        # The **ProductKey** of the product to which the device belongs. You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The push URL. The maximum length is 500 bytes.
        # 
        # This parameter is required.
        self.push_url = push_url
        # The type of the video stream. Valid values:
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
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.push_url is not None:
            result['PushUrl'] = self.push_url

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

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

