# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryLocalFileUploadJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryLocalFileUploadJobResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code:
        # 
        # - **200**: The call is successful.
        # - Other values: An error occurred. For more information about error codes, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The query result.
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
            temp_model = main_models.QueryLocalFileUploadJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryLocalFileUploadJobResponseBodyData(DaraModel):
    def __init__(
        self,
        result_list: List[main_models.QueryLocalFileUploadJobResponseBodyDataResultList] = None,
        status: int = None,
    ):
        # The task list.
        self.result_list = result_list
        # The status of the video recording upload task. Valid values:
        # 
        # - 0: The task is being initialized.
        # - 1: The task is running.
        # - 2: The task is completed.
        self.status = status

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.QueryLocalFileUploadJobResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class QueryLocalFileUploadJobResponseBodyDataResultList(DaraModel):
    def __init__(
        self,
        code: int = None,
        device_name: str = None,
        file_list: List[main_models.QueryLocalFileUploadJobResponseBodyDataResultListFileList] = None,
        iot_id: str = None,
        product_key: str = None,
        slot_end_time: int = None,
        slot_start_time: int = None,
        slot_status: int = None,
    ):
        # The status code of the video recording upload task. Valid values:
        # 
        # - 200: Normal.
        # - 9201: The device is offline. Bring the device online and try again.
        # - 9409: No cloud storage quota is available. Check the cloud storage quota and try again.
        # - 9417: A device, network, or other exception occurred. Try again, or check the device and network status.
        # - 9435: The video recording file does not exist. Make sure that the video recording file is stored locally on the video device and try again.
        self.code = code
        # The DeviceName of the video device.
        self.device_name = device_name
        # The list of video recording files.
        self.file_list = file_list
        # The ID of the video device. The ID is issued by IoT Platform and uniquely identifies the device.
        self.iot_id = iot_id
        # The ProductKey of the product to which the video device belongs.
        self.product_key = product_key
        # The end time of the video recording upload task.
        self.slot_end_time = slot_end_time
        # The start time of the video recording upload task.
        self.slot_start_time = slot_start_time
        # The execution status of the video recording upload task within the time period specified by **SlotStartTime** and **SlotEndTime**. Valid values:
        # - 0: The task is being initialized.
        # - 1: The task is running.
        # - 2: The task is completed.
        # - 3: An exception occurred during task execution.
        # - 4: The task is manually terminated.
        self.slot_status = slot_status

    def validate(self):
        if self.file_list:
            for v1 in self.file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        result['FileList'] = []
        if self.file_list is not None:
            for k1 in self.file_list:
                result['FileList'].append(k1.to_map() if k1 else None)

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.slot_end_time is not None:
            result['SlotEndTime'] = self.slot_end_time

        if self.slot_start_time is not None:
            result['SlotStartTime'] = self.slot_start_time

        if self.slot_status is not None:
            result['SlotStatus'] = self.slot_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        self.file_list = []
        if m.get('FileList') is not None:
            for k1 in m.get('FileList'):
                temp_model = main_models.QueryLocalFileUploadJobResponseBodyDataResultListFileList()
                self.file_list.append(temp_model.from_map(k1))

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('SlotEndTime') is not None:
            self.slot_end_time = m.get('SlotEndTime')

        if m.get('SlotStartTime') is not None:
            self.slot_start_time = m.get('SlotStartTime')

        if m.get('SlotStatus') is not None:
            self.slot_status = m.get('SlotStatus')

        return self

class QueryLocalFileUploadJobResponseBodyDataResultListFileList(DaraModel):
    def __init__(
        self,
        file_end_time: int = None,
        file_name: str = None,
        file_start_time: int = None,
    ):
        # The end time of the video recording file.
        self.file_end_time = file_end_time
        # The name of the video recording file.
        self.file_name = file_name
        # The start time of the video recording file.
        self.file_start_time = file_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_end_time is not None:
            result['FileEndTime'] = self.file_end_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_start_time is not None:
            result['FileStartTime'] = self.file_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileEndTime') is not None:
            self.file_end_time = m.get('FileEndTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileStartTime') is not None:
            self.file_start_time = m.get('FileStartTime')

        return self

