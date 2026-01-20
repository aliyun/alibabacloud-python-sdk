# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListPermissionVersionsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        permissions: List[main_models.ListPermissionVersionsResponseBodyPermissions] = None,
        request_id: str = None,
    ):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        # The information about the permission.
        self.permissions = permissions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.ListPermissionVersionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPermissionVersionsResponseBodyPermissions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_permission: bool = None,
        default_version: bool = None,
        permission_name: str = None,
        permission_version: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_permission = default_permission
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.default_version = default_version
        # The name of the permission.
        self.permission_name = permission_name
        # The version of the permission.
        self.permission_version = permission_version
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        self.resource_type = resource_type
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name

        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')

        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

