# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDevicePictureFileRequest(DaraModel):
    def __init__(
        self,
        capture_id: str = None,
        device_name: str = None,
        expire_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_type: int = None,
        product_key: str = None,
        thumb_width: int = None,
    ):
        # The ID of the image generated when a snapshot capture event occurs:
        # - For active snapshot capture, see [TriggerCapturePicture](https://help.aliyun.com/document_detail/107914.html) for the image ID.
        # - For snapshot capture triggered by an intelligent alert event, see [QueryDeviceEvent](https://help.aliyun.com/document_detail/107916.html) for the image ID.
        # 
        # This parameter is required.
        self.capture_id = capture_id
        # The DeviceName of the IPC device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # Specifies the expiration time of the image URL. Unit: minutes. Valid values: 1 to 43200.
        self.expire_time = expire_time
        # The IotId of the IPC device. The IotId is the globally unique identifier (GUID) that is issued by IoT Platform to the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the IotId.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the globally unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the **ID** of the current instance on the **Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If the instance has an ID, you must specify the ID. Otherwise, the call fails.
        # - If the <props="intl"><ph>**Overview** page is not displayed or the instance does not have an </ph>ID, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The image type. Valid values:
        # - **0**: thumbnail.
        # - **1**: original image.
        # - **2**: all images. This is the default value.
        self.picture_type = picture_type
        # The ProductKey of the product to which the IPC device belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # Specifies the width of the target scaled image. Unit: px. Valid values: 1 to 4096.
        self.thumb_width = thumb_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capture_id is not None:
            result['CaptureId'] = self.capture_id

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.picture_type is not None:
            result['PictureType'] = self.picture_type

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureId') is not None:
            self.capture_id = m.get('CaptureId')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')

        return self

