# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryFaceDeviceGroupsByDeviceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryFaceDeviceGroupsByDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The response data.
        self.data = data
        # The error message.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.QueryFaceDeviceGroupsByDeviceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryFaceDeviceGroupsByDeviceResponseBodyData(DaraModel):
    def __init__(
        self,
        device_group_list: List[main_models.QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of device groups.
        self.device_group_list = device_group_list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of device groups.
        self.total = total

    def validate(self):
        if self.device_group_list:
            for v1 in self.device_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k1 in self.device_group_list:
                result['DeviceGroupList'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k1 in m.get('DeviceGroupList'):
                temp_model = main_models.QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList(DaraModel):
    def __init__(
        self,
        device_group_id: str = None,
        device_group_name: str = None,
        modified_time: str = None,
    ):
        # The device group ID.
        self.device_group_id = device_group_id
        # The device group name.
        self.device_group_name = device_group_name
        # The time when the device group was modified.
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        return self

