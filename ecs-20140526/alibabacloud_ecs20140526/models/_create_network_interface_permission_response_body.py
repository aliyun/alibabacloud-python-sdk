# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkInterfacePermissionResponseBody(DaraModel):
    def __init__(
        self,
        network_interface_permission: main_models.CreateNetworkInterfacePermissionResponseBodyNetworkInterfacePermission = None,
        request_id: str = None,
    ):
        # Details about permissions on the ENI.
        self.network_interface_permission = network_interface_permission
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.network_interface_permission:
            self.network_interface_permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_permission is not None:
            result['NetworkInterfacePermission'] = self.network_interface_permission.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfacePermission') is not None:
            temp_model = main_models.CreateNetworkInterfacePermissionResponseBodyNetworkInterfacePermission()
            self.network_interface_permission = temp_model.from_map(m.get('NetworkInterfacePermission'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateNetworkInterfacePermissionResponseBodyNetworkInterfacePermission(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        network_interface_id: str = None,
        network_interface_permission_id: str = None,
        permission: str = None,
        permission_state: str = None,
        service_name: str = None,
    ):
        # The ID of the Alibaba Cloud partner (a certified ISV).
        self.account_id = account_id
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The ID of the permission on the ENI.
        self.network_interface_permission_id = network_interface_permission_id
        # The permission on the ENI.
        self.permission = permission
        # The state of the permission on the ENI. Valid values:
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

