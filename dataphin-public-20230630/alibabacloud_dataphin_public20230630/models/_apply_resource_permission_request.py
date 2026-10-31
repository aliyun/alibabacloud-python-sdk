# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ApplyResourcePermissionRequest(DaraModel):
    def __init__(
        self,
        apply_command: main_models.ApplyResourcePermissionRequestApplyCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The permission application request.
        # 
        # This parameter is required.
        self.apply_command = apply_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.apply_command:
            self.apply_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_command is not None:
            result['ApplyCommand'] = self.apply_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyCommand') is not None:
            temp_model = main_models.ApplyResourcePermissionRequestApplyCommand()
            self.apply_command = temp_model.from_map(m.get('ApplyCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ApplyResourcePermissionRequestApplyCommand(DaraModel):
    def __init__(
        self,
        grant_to_users: List[main_models.ApplyResourcePermissionRequestApplyCommandGrantToUsers] = None,
        granularity: str = None,
        operate_list: List[str] = None,
        reason: str = None,
        resource_list: List[main_models.ApplyResourcePermissionRequestApplyCommandResourceList] = None,
        resource_type: str = None,
    ):
        # The list of users to whom permissions are granted.
        # 
        # This parameter is required.
        self.grant_to_users = grant_to_users
        # The permission granularity. Valid values: TABLE (table-level permissions) and COLUMN (column-level permissions).
        # 
        # This parameter is required.
        self.granularity = granularity
        # The list of operation types.
        # 
        # This parameter is required.
        self.operate_list = operate_list
        # The reason for the application. This parameter is required and cannot be empty or contain only whitespace characters.
        # 
        # This parameter is required.
        self.reason = reason
        # The list of resources for which permissions are applied.
        # 
        # This parameter is required.
        self.resource_list = resource_list
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.grant_to_users:
            for v1 in self.grant_to_users:
                 if v1:
                    v1.validate()
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantToUsers'] = []
        if self.grant_to_users is not None:
            for k1 in self.grant_to_users:
                result['GrantToUsers'].append(k1.to_map() if k1 else None)

        if self.granularity is not None:
            result['Granularity'] = self.granularity

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_to_users = []
        if m.get('GrantToUsers') is not None:
            for k1 in m.get('GrantToUsers'):
                temp_model = main_models.ApplyResourcePermissionRequestApplyCommandGrantToUsers()
                self.grant_to_users.append(temp_model.from_map(k1))

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('OperateList') is not None:
            self.operate_list = m.get('OperateList')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.ApplyResourcePermissionRequestApplyCommandResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ApplyResourcePermissionRequestApplyCommandResourceList(DaraModel):
    def __init__(
        self,
        column_list: List[str] = None,
        resource_id: str = None,
    ):
        # The list of column names specified for column-level permissions. This parameter is required when the granularity is COLUMN.
        self.column_list = column_list
        # The resource ID, which is the GUID of the table metadata.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_list is not None:
            result['ColumnList'] = self.column_list

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnList') is not None:
            self.column_list = m.get('ColumnList')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

class ApplyResourcePermissionRequestApplyCommandGrantToUsers(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        period_end: str = None,
        period_type: str = None,
        project_id: str = None,
        user_id: str = None,
    ):
        # The account type.
        # 
        # This parameter is required.
        self.account_type = account_type
        # The expiration date of the permission. Format: yyyy-MM-dd.
        self.period_end = period_end
        # The type of the permission validity period.
        self.period_type = period_type
        # The project ID of the production account. This parameter is required when the account type is PRODUCE.
        self.project_id = project_id
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.period_end is not None:
            result['PeriodEnd'] = self.period_end

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('PeriodEnd') is not None:
            self.period_end = m.get('PeriodEnd')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

