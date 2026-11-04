# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class TransferDeviceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TransferDeviceInstanceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code:
        # 
        # - **200**: The call was successful.
        # - Other values: The call failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The result.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The unique identifier that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # Indicates whether the call was successful:
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
            temp_model = main_models.TransferDeviceInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TransferDeviceInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_list: List[main_models.TransferDeviceInstanceResponseBodyDataFailedList] = None,
        success_list: List[main_models.TransferDeviceInstanceResponseBodyDataSuccessList] = None,
    ):
        # The list of devices that failed to be transferred.
        self.failed_list = failed_list
        # The list of devices that were successfully transferred.
        self.success_list = success_list

    def validate(self):
        if self.failed_list:
            for v1 in self.failed_list:
                 if v1:
                    v1.validate()
        if self.success_list:
            for v1 in self.success_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedList'] = []
        if self.failed_list is not None:
            for k1 in self.failed_list:
                result['FailedList'].append(k1.to_map() if k1 else None)

        result['SuccessList'] = []
        if self.success_list is not None:
            for k1 in self.success_list:
                result['SuccessList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_list = []
        if m.get('FailedList') is not None:
            for k1 in m.get('FailedList'):
                temp_model = main_models.TransferDeviceInstanceResponseBodyDataFailedList()
                self.failed_list.append(temp_model.from_map(k1))

        self.success_list = []
        if m.get('SuccessList') is not None:
            for k1 in m.get('SuccessList'):
                temp_model = main_models.TransferDeviceInstanceResponseBodyDataSuccessList()
                self.success_list.append(temp_model.from_map(k1))

        return self

class TransferDeviceInstanceResponseBodyDataSuccessList(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        message: str = None,
    ):
        # The name of the device.
        self.device_name = device_name
        # The description of the successful transfer.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class TransferDeviceInstanceResponseBodyDataFailedList(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        message: str = None,
    ):
        # The name of the device.
        self.device_name = device_name
        # The description of the failed transfer.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

