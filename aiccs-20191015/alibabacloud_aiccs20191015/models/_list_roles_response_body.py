# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class ListRolesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRolesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRolesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRolesResponseBodyData(DaraModel):
    def __init__(
        self,
        bu_id: int = None,
        code: str = None,
        create_time: str = None,
        description: str = None,
        role_group_id: int = None,
        role_group_name: str = None,
        role_id: int = None,
        title: str = None,
    ):
        self.bu_id = bu_id
        self.code = code
        self.create_time = create_time
        self.description = description
        self.role_group_id = role_group_id
        self.role_group_name = role_group_name
        self.role_id = role_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bu_id is not None:
            result['BuId'] = self.bu_id

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.role_group_id is not None:
            result['RoleGroupId'] = self.role_group_id

        if self.role_group_name is not None:
            result['RoleGroupName'] = self.role_group_name

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RoleGroupId') is not None:
            self.role_group_id = m.get('RoleGroupId')

        if m.get('RoleGroupName') is not None:
            self.role_group_name = m.get('RoleGroupName')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

