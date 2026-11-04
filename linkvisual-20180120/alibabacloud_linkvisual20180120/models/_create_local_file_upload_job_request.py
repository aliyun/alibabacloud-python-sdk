# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class CreateLocalFileUploadJobRequest(DaraModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        time_slot: List[main_models.CreateLocalFileUploadJobRequestTimeSlot] = None,
    ):
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If the instance has an ID, you must specify the ID. Otherwise, the call fails.
        # - If the instance does not have an <props="intl"><ph>**Instance Overview** page or </ph>ID, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The list of time slots.
        self.time_slot = time_slot

    def validate(self):
        if self.time_slot:
            for v1 in self.time_slot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        result['TimeSlot'] = []
        if self.time_slot is not None:
            for k1 in self.time_slot:
                result['TimeSlot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        self.time_slot = []
        if m.get('TimeSlot') is not None:
            for k1 in m.get('TimeSlot'):
                temp_model = main_models.CreateLocalFileUploadJobRequestTimeSlot()
                self.time_slot.append(temp_model.from_map(k1))

        return self

class CreateLocalFileUploadJobRequestTimeSlot(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        product_key: str = None,
        start_time: int = None,
    ):
        # The name of the video device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The end time for uploading the local video recording. The time is a 10-digit UNIX timestamp in seconds.
        # >The maximum time range for a single local video recording upload job is 1 hour.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the video device. The ID is issued by IoT Platform and uniquely identifies the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** uniquely identifies the device and has a one-to-one mapping with the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The ProductKey of the product to which the video device belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The start time for uploading the local video recording. The time is a 10-digit UNIX timestamp in seconds.
        # >The maximum time range for a single local video recording upload job is 1 hour.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

