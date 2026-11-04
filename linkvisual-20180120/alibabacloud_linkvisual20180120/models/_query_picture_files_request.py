# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPictureFilesRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        picture_source: int = None,
        picture_type: int = None,
        product_key: str = None,
    ):
        # The start time of the retrieval range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The page number of the returned page. Pages start from 1.
        self.current_page = current_page
        # The DeviceName of the IP camera.
        # You can view the **DeviceName** on the **Devices** page of the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The end time of the retrieval range. The time is a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the IP camera. The ID is issued by IoT Platform and is the unique identifier of the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # Instance ID of the instance. You can view the **ID** of the current instance on the **Instance Overview** page of the IoT Platform console.
        # 
        # >Notice: 
        # - If the instance has an ID, you must specify instance ID. Otherwise, the call fails.
        # - If the instance does not have an <props="intl"><ph>**Instance Overview** page or </ph>ID, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The number of entries to return on each page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The source of the image. Valid values:
        # 
        # - **0**: all events. This is the default value.
        # - **1**: snapshot captured during an alert event.
        # - **2**: manual snapshot.
        # - **3**: other sources.
        # - **4**: cloud snapshot.
        self.picture_source = picture_source
        # The type of the image. Valid values:
        # 
        # - **0**: thumbnail. 
        # - **1**: original image.
        # - **2**: all images. This is the default value.
        self.picture_type = picture_type
        # The ProductKey of the product to which the IP camera belongs.
        # You can view the ProductKey on the **Products** page of the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.picture_source is not None:
            result['PictureSource'] = self.picture_source

        if self.picture_type is not None:
            result['PictureType'] = self.picture_type

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PictureSource') is not None:
            self.picture_source = m.get('PictureSource')

        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

