# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CheckResourcePermissionRequest(DaraModel):
    def __init__(
        self,
        check_command: main_models.CheckResourcePermissionRequestCheckCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command = check_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.check_command:
            self.check_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_command is not None:
            result['CheckCommand'] = self.check_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            temp_model = main_models.CheckResourcePermissionRequestCheckCommand()
            self.check_command = temp_model.from_map(m.get('CheckCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CheckResourcePermissionRequestCheckCommand(DaraModel):
    def __init__(
        self,
        operate: str = None,
        resource_list: List[main_models.CheckResourcePermissionRequestCheckCommandResourceList] = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.operate = operate
        # This parameter is required.
        self.resource_list = resource_list
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate is not None:
            result['Operate'] = self.operate

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operate') is not None:
            self.operate = m.get('Operate')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.CheckResourcePermissionRequestCheckCommandResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CheckResourcePermissionRequestCheckCommandResourceList(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

