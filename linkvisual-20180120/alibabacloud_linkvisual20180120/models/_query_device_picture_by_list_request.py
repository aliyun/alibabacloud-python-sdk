# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryDevicePictureByListRequest(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        expire_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        picture_id_list: List[str] = None,
        picture_type: int = None,
        product_key: str = None,
        thumb_width: int = None,
    ):
        # The DeviceName of the IP camera.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The expiration time of the image URL. Unit: minutes.
        self.expire_time = expire_time
        # The ID of the IP camera. The ID is issued by IoT Platform and uniquely identifies the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. **IotId** uniquely identifies the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
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
        # The list of image IDs. Image IDs are generated when you call the [TriggerCapturePicture](https://help.aliyun.com/document_detail/107914.html) operation.
        # 
        # > You can specify up to 50 image IDs in a single call.
        # 
        # This parameter is required.
        self.picture_id_list = picture_id_list
        # The image type. Valid values:
        # 
        # - **0**: thumbnail.
        # - **1**: original image. 
        # - **2**: all. Default value.
        self.picture_type = picture_type
        # The ProductKey of the product to which the IP camera belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # Specifies the width of the target thumbnail. Unit: px. Valid values: 1 to 4096.
        self.thumb_width = thumb_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list

        if self.picture_type is not None:
            result['PictureType'] = self.picture_type

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')

        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')

        return self

