# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListWorkspacesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The dataset.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The total number of workspaces that meet the condition, which is the same as the TotalCount parameter.
        self.max_results = max_results
        # NextToken does not take effect.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The request succeeded.
        # *   **false**: The request failed.
        self.success = success
        # The total number of workspaces that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListWorkspacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListWorkspacesResponseBodyData(DaraModel):
    def __init__(
        self,
        base_workspaces: List[main_models.ListWorkspacesResponseBodyDataBaseWorkspaces] = None,
    ):
        self.base_workspaces = base_workspaces

    def validate(self):
        if self.base_workspaces:
            for v1 in self.base_workspaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaseWorkspaces'] = []
        if self.base_workspaces is not None:
            for k1 in self.base_workspaces:
                result['BaseWorkspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.base_workspaces = []
        if m.get('BaseWorkspaces') is not None:
            for k1 in m.get('BaseWorkspaces'):
                temp_model = main_models.ListWorkspacesResponseBodyDataBaseWorkspaces()
                self.base_workspaces.append(temp_model.from_map(k1))

        return self

class ListWorkspacesResponseBodyDataBaseWorkspaces(DaraModel):
    def __init__(
        self,
        already_joined: bool = None,
        creator_id: int = None,
        creator_nick_name: str = None,
        creator_uid: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        owner_id: int = None,
        owner_nick_name: str = None,
        owner_uid: str = None,
        region: str = None,
        service_account_id: int = None,
        service_account_nick_name: str = None,
        service_account_uid: str = None,
        tenant_id: int = None,
        vpc_id: str = None,
        workspace_id: int = None,
        workspace_name: str = None,
    ):
        # Whether the current user has joined the workspace.
        self.already_joined = already_joined
        # The ID of the creator.
        self.creator_id = creator_id
        # The nickname of the creator.
        self.creator_nick_name = creator_nick_name
        # The Alibaba Cloud account UID of the creator.
        self.creator_uid = creator_uid
        # The description of the workspace.
        self.description = description
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The name of the workspace.
        self.name = name
        # The owner ID.
        self.owner_id = owner_id
        # The nickname of the owner.
        self.owner_nick_name = owner_nick_name
        # The Alibaba Cloud UID of the owner.
        self.owner_uid = owner_uid
        # The region ID.
        self.region = region
        # The ID of the service account.
        self.service_account_id = service_account_id
        # The nickname of the service account.
        self.service_account_nick_name = service_account_nick_name
        # The Alibaba Cloud account UID of the service account.
        self.service_account_uid = service_account_uid
        # The ID of the tenant to which the workspace belongs.
        self.tenant_id = tenant_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_joined is not None:
            result['AlreadyJoined'] = self.already_joined

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name

        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.region is not None:
            result['Region'] = self.region

        if self.service_account_id is not None:
            result['ServiceAccountId'] = self.service_account_id

        if self.service_account_nick_name is not None:
            result['ServiceAccountNickName'] = self.service_account_nick_name

        if self.service_account_uid is not None:
            result['ServiceAccountUid'] = self.service_account_uid

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyJoined') is not None:
            self.already_joined = m.get('AlreadyJoined')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')

        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceAccountId') is not None:
            self.service_account_id = m.get('ServiceAccountId')

        if m.get('ServiceAccountNickName') is not None:
            self.service_account_nick_name = m.get('ServiceAccountNickName')

        if m.get('ServiceAccountUid') is not None:
            self.service_account_uid = m.get('ServiceAccountUid')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

