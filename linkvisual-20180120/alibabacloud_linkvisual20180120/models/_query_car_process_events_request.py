# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCarProcessEventsRequest(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        area_index: int = None,
        begin_time: int = None,
        current_page: int = None,
        end_time: int = None,
        iot_instance_id: str = None,
        page_size: int = None,
        plate_no: str = None,
        sub_device_name: str = None,
        sub_iot_id: str = None,
        sub_product_key: str = None,
    ):
        # The action type of the vehicle. Valid values:
        # 
        # - **1**: Enter.
        # - **2**: Stay.
        # - **3**: Leave.
        self.action_type = action_type
        # The detection box of the IPC device. You can call the [InvokeThingService](https://help.aliyun.com/document_detail/69584.html) operation to query the number of detection boxes. Set **identifier** to **QueryAlgoTaskDetails**.
        self.area_index = area_index
        # The start time of the query range. The time is a 13-digit timestamp in milliseconds.
        self.begin_time = begin_time
        # The page number of the returned page. Pages start from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time of the query range. The time is a 13-digit timestamp in milliseconds.
        self.end_time = end_time
        # The instance ID. You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console.
        # 
        # >Notice: 
        # - If the instance has an ID, you must specify this ID. Otherwise, the call fails.
        # - If the instance does not have an ID<props="intl"><ph> or the **Instance Overview** page is not displayed</ph>, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # The number of entries to return on each page. Valid values: 1 to 20. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The license plate number. The value can be up to 15 characters in length.
        self.plate_no = plate_no
        # The name of the IPC device.
        # You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.sub_device_name = sub_device_name
        # The ID of the IP camera (IPC) device. The ID is issued by IoT Platform and uniquely identifies the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** uniquely identifies the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.sub_iot_id = sub_iot_id
        # The ProductKey of the product to which the IPC device belongs.
        # You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information about all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.sub_product_key = sub_product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.area_index is not None:
            result['AreaIndex'] = self.area_index

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no

        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name

        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id

        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')

        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')

        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')

        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')

        return self

