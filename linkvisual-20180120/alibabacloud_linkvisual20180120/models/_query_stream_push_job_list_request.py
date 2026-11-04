# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryStreamPushJobListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_name: str = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        job_type: int = None,
        page_size: int = None,
        product_key: str = None,
    ):
        # Specifies the page number of the page to return. Default value: 1.
        self.current_page = current_page
        # The DeviceName of the device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The ID of the device. The ID is the unique identifier that is issued by IoT Platform to the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # Instance ID of the instance. You can view instance ID of the current instance on the **Instance Overview** tab in the IoT Platform console.
        # 
        # This parameter is required.
        self.iot_instance_id = iot_instance_id
        # The type of the stream push job. Valid values:
        # 
        # - **1** (default): continuous job.
        # - **2**: triggered job. The job ends after it is interrupted.
        self.job_type = job_type
        # Specifies the number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The **ProductKey** of the product to which the device belongs.
        # You can view the **ProductKey** on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information of all products under the current account.
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

        if self.job_type is not None:
            result['JobType'] = self.job_type

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

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

