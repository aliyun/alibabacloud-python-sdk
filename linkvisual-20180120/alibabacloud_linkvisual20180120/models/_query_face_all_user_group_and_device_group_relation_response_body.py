# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData = None,
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
        # Indicates whether the API call was successful.
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
            temp_model = main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of face synchronization relationships between user groups and device groups.
        self.list = list
        # The page number.
        self.page = page
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList(DaraModel):
    def __init__(
        self,
        control_id: str = None,
        control_type: str = None,
        device_group_id: str = None,
        modified_time: str = None,
        user_group_id: str = None,
    ):
        # The control ID of the synchronization relationship between the user group and the device group.
        self.control_id = control_id
        # The face synchronization relationship type, which synchronizes user photos and user information.
        self.control_type = control_type
        # The device group ID.
        self.device_group_id = device_group_id
        # The modification time.
        self.modified_time = modified_time
        # The user group ID.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_id is not None:
            result['ControlId'] = self.control_id

        if self.control_type is not None:
            result['ControlType'] = self.control_type

        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')

        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')

        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

