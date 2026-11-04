# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeletePictureRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_id_list: List[str] = None,
        product_key: str = None,
    ):
        # The DeviceName of the IPC device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The IotId of the IPC device. The IotId is a unique identifier issued by IoT Platform for the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is a unique identifier for the device and has a one-to-one mapping with the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # >Notice: 
        # - If the instance has an ID, you must specify the ID. Otherwise, the call fails.
        # - If the instance does not have an <props="intl"><ph>**Instance Overview** page or an </ph>ID, you do not need to specify this parameter.
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The list of picture IDs. Picture IDs are generated when you call the [TriggerCapturePicture](https://help.aliyun.com/document_detail/107914.html) operation.
        # > You can specify up to 50 picture IDs in a single call.
        # 
        # This parameter is required.
        self.picture_id_list = picture_id_list
        # The ProductKey of the product to which the IPC device belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
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

        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list

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

        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

