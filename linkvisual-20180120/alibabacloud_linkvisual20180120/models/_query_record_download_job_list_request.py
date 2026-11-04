# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordDownloadJobListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        page_size: int = None,
        product_key: str = None,
    ):
        # Specifies the page number to return. Default value: 1.
        self.current_page = current_page
        # The DeviceName of the video device. You can view the **DeviceName** of devices under a specified product on the **Devices** page in the [IoT Platform console](https://iot.console.aliyun.com/devices) or by calling the [QueryDevice](https://help.aliyun.com/document_detail/69905.html) operation.
        # 
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The ID of the video device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the ID.
        # 
        # >Notice:  **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the ID of the current instance on the **Instance Overview** tab in the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # Specifies the number of entries to return per page. Maximum value: 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The **ProductKey** of the product to which the video device belongs.
        # 
        # You can view the information of all products under the current instance on the **Products** page in the [IoT Platform console](https://iot.console.aliyun.com/product) or by calling the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation.
        # 
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

