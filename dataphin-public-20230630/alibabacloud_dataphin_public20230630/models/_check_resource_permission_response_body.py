# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CheckResourcePermissionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        resource_permission_list: List[main_models.CheckResourcePermissionResponseBodyResourcePermissionList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.resource_permission_list = resource_permission_list
        self.success = success

    def validate(self):
        if self.resource_permission_list:
            for v1 in self.resource_permission_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcePermissionList'] = []
        if self.resource_permission_list is not None:
            for k1 in self.resource_permission_list:
                result['ResourcePermissionList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_permission_list = []
        if m.get('ResourcePermissionList') is not None:
            for k1 in m.get('ResourcePermissionList'):
                temp_model = main_models.CheckResourcePermissionResponseBodyResourcePermissionList()
                self.resource_permission_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckResourcePermissionResponseBodyResourcePermissionList(DaraModel):
    def __init__(
        self,
        has_permission: bool = None,
        resource_id: str = None,
    ):
        self.has_permission = has_permission
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

