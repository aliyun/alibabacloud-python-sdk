# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GrantResourcePermissionRequest(DaraModel):
    def __init__(
        self,
        grant_command: main_models.GrantResourcePermissionRequestGrantCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.grant_command = grant_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.grant_command:
            self.grant_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_command is not None:
            result['GrantCommand'] = self.grant_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantCommand') is not None:
            temp_model = main_models.GrantResourcePermissionRequestGrantCommand()
            self.grant_command = temp_model.from_map(m.get('GrantCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GrantResourcePermissionRequestGrantCommand(DaraModel):
    def __init__(
        self,
        effective_end: str = None,
        operate_list: List[str] = None,
        reason: str = None,
        resource_list: List[main_models.GrantResourcePermissionRequestGrantCommandResourceList] = None,
        resource_type: str = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.effective_end = effective_end
        # This parameter is required.
        self.operate_list = operate_list
        self.reason = reason
        # This parameter is required.
        self.resource_list = resource_list
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.user_id_list = user_id_list

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
        if self.effective_end is not None:
            result['EffectiveEnd'] = self.effective_end

        if self.operate_list is not None:
            result['OperateList'] = self.operate_list

        if self.reason is not None:
            result['Reason'] = self.reason

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveEnd') is not None:
            self.effective_end = m.get('EffectiveEnd')

        if m.get('OperateList') is not None:
            self.operate_list = m.get('OperateList')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.GrantResourcePermissionRequestGrantCommandResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

class GrantResourcePermissionRequestGrantCommandResourceList(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
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

