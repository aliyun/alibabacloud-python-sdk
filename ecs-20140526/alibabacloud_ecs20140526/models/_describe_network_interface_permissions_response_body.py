# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInterfacePermissionsResponseBody(DaraModel):
    def __init__(
        self,
        network_interface_permissions: main_models.DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissions = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the ENI permissions.
        self.network_interface_permissions = network_interface_permissions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.network_interface_permissions:
            self.network_interface_permissions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_permissions is not None:
            result['NetworkInterfacePermissions'] = self.network_interface_permissions.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfacePermissions') is not None:
            temp_model = main_models.DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissions()
            self.network_interface_permissions = temp_model.from_map(m.get('NetworkInterfacePermissions'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissions(DaraModel):
    def __init__(
        self,
        network_interface_permission: List[main_models.DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissionsNetworkInterfacePermission] = None,
    ):
        self.network_interface_permission = network_interface_permission

    def validate(self):
        if self.network_interface_permission:
            for v1 in self.network_interface_permission:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfacePermission'] = []
        if self.network_interface_permission is not None:
            for k1 in self.network_interface_permission:
                result['NetworkInterfacePermission'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_permission = []
        if m.get('NetworkInterfacePermission') is not None:
            for k1 in m.get('NetworkInterfacePermission'):
                temp_model = main_models.DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissionsNetworkInterfacePermission()
                self.network_interface_permission.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacePermissionsResponseBodyNetworkInterfacePermissionsNetworkInterfacePermission(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        network_interface_id: str = None,
        network_interface_permission_id: str = None,
        permission: str = None,
        permission_state: str = None,
        service_name: str = None,
    ):
        # The ID of the Alibaba Cloud partner (a certified ISV) or individual user.
        self.account_id = account_id
        # The ID of ENI N.
        self.network_interface_id = network_interface_id
        # The ID of the ENI permission.
        self.network_interface_permission_id = network_interface_permission_id
        # The ENI permission.
        self.permission = permission
        # The status of the ENI permission. Valid values:
        # 
        # *   Pending: The permission is being granted.
        # *   Granted: The permission is granted.
        # *   Revoking: The permission is being revoked.
        # *   Revoked: The permission is revoked.
        self.permission_state = permission_state
        # The name of the Alibaba Cloud service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_permission_id is not None:
            result['NetworkInterfacePermissionId'] = self.network_interface_permission_id

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.permission_state is not None:
            result['PermissionState'] = self.permission_state

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfacePermissionId') is not None:
            self.network_interface_permission_id = m.get('NetworkInterfacePermissionId')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('PermissionState') is not None:
            self.permission_state = m.get('PermissionState')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

