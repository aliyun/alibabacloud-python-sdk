# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryCarProcessEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCarProcessEventsResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # - **200**: The call was successful.
        # - Other values: An error occurred. For more information, see [Error codes](https://help.aliyun.com/document_detail/288314.html).
        self.code = code
        # The data returned if the call is successful.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryCarProcessEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCarProcessEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[main_models.QueryCarProcessEventsResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The total number of pages.
        self.page_count = page_count
        # The list of returned intelligent alert events.
        self.page_data = page_data
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of vehicle recognition events.
        self.total = total

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.QueryCarProcessEventsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryCarProcessEventsResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        area_index: int = None,
        confidence: int = None,
        event_id: str = None,
        event_pic_id: str = None,
        event_pic_url: str = None,
        event_time: int = None,
        event_type: int = None,
        iot_id: str = None,
        plate_no: str = None,
        sub_device_name: str = None,
        sub_device_nick_name: str = None,
        sub_iot_id: str = None,
        sub_product_key: str = None,
        task_id: str = None,
    ):
        # The action type of the vehicle.
        self.action_type = action_type
        # The number of detection boxes recognized by the IPC device.
        self.area_index = area_index
        # The confidence level of the vehicle recognition.
        self.confidence = confidence
        # The ID of the intelligent alert event.
        self.event_id = event_id
        # The ID of the intelligent alert event picture.
        self.event_pic_id = event_pic_id
        # The URL of the intelligent alert event picture.
        self.event_pic_url = event_pic_url
        # The timestamp when the event occurred, in milliseconds.
        self.event_time = event_time
        # The type of the intelligent alert event. Valid values:
        # 
        # - **0**: All intelligent alert events.
        # - Multiple intelligent alert events: Enter the sequence numbers of the intelligent alert events and separate them with commas (,), such as `10001,10002`.
        # > You can specify up to 10 intelligent alert events at a time.
        # 
        # To view all intelligent alert event types, go to the **Define Feature** tab of the **Product Details** page in the IoT Platform console. For more information, see [View intelligent alert event types](https://help.aliyun.com/document_detail/207701.html).
        self.event_type = event_type
        # The IotId of the V-series edge appliance.
        self.iot_id = iot_id
        # The license plate number.
        self.plate_no = plate_no
        # The DeviceName of the IPC device.
        self.sub_device_name = sub_device_name
        # The DeviceNickName of the IPC device.
        self.sub_device_nick_name = sub_device_nick_name
        # The ID of the IPC device.
        self.sub_iot_id = sub_iot_id
        # The ProductKey of the IPC device.
        self.sub_product_key = sub_product_key
        # The task ID of the vehicle detection event.
        self.task_id = task_id

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

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id

        if self.event_pic_url is not None:
            result['EventPicUrl'] = self.event_pic_url

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no

        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name

        if self.sub_device_nick_name is not None:
            result['SubDeviceNickName'] = self.sub_device_nick_name

        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id

        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')

        if m.get('EventPicUrl') is not None:
            self.event_pic_url = m.get('EventPicUrl')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')

        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')

        if m.get('SubDeviceNickName') is not None:
            self.sub_device_nick_name = m.get('SubDeviceNickName')

        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')

        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

