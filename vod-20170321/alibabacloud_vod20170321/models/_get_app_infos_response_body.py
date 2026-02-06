# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetAppInfosResponseBody(DaraModel):
    def __init__(
        self,
        app_info_list: List[main_models.GetAppInfosResponseBodyAppInfoList] = None,
        code: str = None,
        non_exist_app_ids: List[str] = None,
        request_id: str = None,
    ):
        # The details of applications.
        self.app_info_list = app_info_list
        # The HTTP status code that is returned.
        self.code = code
        # The IDs of applications that do not exist.
        self.non_exist_app_ids = non_exist_app_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_info_list:
            for v1 in self.app_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k1 in self.app_info_list:
                result['AppInfoList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.non_exist_app_ids is not None:
            result['NonExistAppIds'] = self.non_exist_app_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k1 in m.get('AppInfoList'):
                temp_model = main_models.GetAppInfosResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('NonExistAppIds') is not None:
            self.non_exist_app_ids = m.get('NonExistAppIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAppInfosResponseBodyAppInfoList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        creation_time: str = None,
        description: str = None,
        modification_time: str = None,
        resource_group_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The time when the application was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the application.
        self.description = description
        # The last time when the application was modified. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the application. Valid values:
        # 
        # *   **Normal**
        # *   **Disable**
        self.status = status
        # The type of the application. Valid values:
        # 
        # *   **System**
        # *   **Custom**
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

