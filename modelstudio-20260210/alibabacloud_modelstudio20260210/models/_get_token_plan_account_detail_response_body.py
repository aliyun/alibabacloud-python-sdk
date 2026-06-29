# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetTokenPlanAccountDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTokenPlanAccountDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTokenPlanAccountDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTokenPlanAccountDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_type: str = None,
        aliyun_uid: str = None,
        created_at: str = None,
        email: str = None,
        is_deleted: bool = None,
        name: str = None,
        org_memberships: List[main_models.GetTokenPlanAccountDetailResponseBodyDataOrgMemberships] = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The account type. Valid values:
        # 
        # - ALIYUN 
        # - SSO 
        # - SA
        self.account_type = account_type
        # The Alibaba Cloud UID. This parameter applies only to accounts of the ALIYUN type.
        self.aliyun_uid = aliyun_uid
        # The time when the account was created.
        self.created_at = created_at
        # The email address. This parameter applies only to accounts of the SSO type.
        self.email = email
        # The global status of the account. A value of 0 indicates Normal. A value of 1 indicates Frozen.
        self.is_deleted = is_deleted
        # The display name of the account.
        self.name = name
        # The list of organization memberships in a tree structure (organization → workspace).
        self.org_memberships = org_memberships

    def validate(self):
        if self.org_memberships:
            for v1 in self.org_memberships:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.email is not None:
            result['Email'] = self.email

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.name is not None:
            result['Name'] = self.name

        result['OrgMemberships'] = []
        if self.org_memberships is not None:
            for k1 in self.org_memberships:
                result['OrgMemberships'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.org_memberships = []
        if m.get('OrgMemberships') is not None:
            for k1 in m.get('OrgMemberships'):
                temp_model = main_models.GetTokenPlanAccountDetailResponseBodyDataOrgMemberships()
                self.org_memberships.append(temp_model.from_map(k1))

        return self

class GetTokenPlanAccountDetailResponseBodyDataOrgMemberships(DaraModel):
    def __init__(
        self,
        member_status: str = None,
        org_id: str = None,
        role_code: str = None,
        role_id: str = None,
        workspaces: List[main_models.GetTokenPlanAccountDetailResponseBodyDataOrgMembershipsWorkspaces] = None,
    ):
        # The organization member status. Valid values:
        # 
        # - ACTIVE 
        # - INITIAL 
        # - FROZEN
        self.member_status = member_status
        # The organization ID.
        self.org_id = org_id
        # The organization role code. Valid values:
        # 
        # - ORG_OWNER
        # - ORG_ADMIN
        # - ORG_MEMBER
        self.role_code = role_code
        # The organization role ID.
        self.role_id = role_id
        # The list of workspaces that the account has joined under the organization.
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for v1 in self.workspaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        result['Workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['Workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k1 in m.get('Workspaces'):
                temp_model = main_models.GetTokenPlanAccountDetailResponseBodyDataOrgMembershipsWorkspaces()
                self.workspaces.append(temp_model.from_map(k1))

        return self

class GetTokenPlanAccountDetailResponseBodyDataOrgMembershipsWorkspaces(DaraModel):
    def __init__(
        self,
        member_status: str = None,
        role_code: str = None,
        role_id: str = None,
        workspace_id: str = None,
    ):
        # The member status. Valid values:
        # - ACTIVE 
        # - FROZEN
        self.member_status = member_status
        # The workspace role code. Valid values:
        # - WS_ADMIN
        # - WS_MEMBER
        self.role_code = role_code
        # The workspace role ID.
        self.role_id = role_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_status is not None:
            result['MemberStatus'] = self.member_status

        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberStatus') is not None:
            self.member_status = m.get('MemberStatus')

        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

