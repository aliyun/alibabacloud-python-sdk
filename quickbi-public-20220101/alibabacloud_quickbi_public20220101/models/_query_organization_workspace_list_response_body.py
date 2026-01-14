# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryOrganizationWorkspaceListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryOrganizationWorkspaceListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the paginated result of the workspace list, with detailed information about the workspaces stored in the Data parameter.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryOrganizationWorkspaceListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryOrganizationWorkspaceListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryOrganizationWorkspaceListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # List of workspaces.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page as set in the request.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryOrganizationWorkspaceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class QueryOrganizationWorkspaceListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        allow_publish_operation: bool = None,
        allow_share_operation: bool = None,
        create_time: str = None,
        create_user: str = None,
        create_user_account_name: str = None,
        modified_time: str = None,
        modify_user: str = None,
        modify_user_account_name: str = None,
        organization_id: str = None,
        owner: str = None,
        owner_account_name: str = None,
        real_owner_account_name: str = None,
        workspace_description: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Whether the work can be made public. Value range:
        # 
        # - true: Public
        # - false: Not public
        self.allow_publish_operation = allow_publish_operation
        # Indicates whether the work can be authorized for sharing. Possible values:
        # 
        # - true: Authorized
        # - false: Not authorized
        self.allow_share_operation = allow_share_operation
        # Creation time of the workspace.
        self.create_time = create_time
        # Quick BI user ID of the creator.
        self.create_user = create_user
        # Aliyun account name of the creator.
        self.create_user_account_name = create_user_account_name
        # Last modified time of the workspace.
        self.modified_time = modified_time
        # ID of the Quick BI user who modified the workspace.
        self.modify_user = modify_user
        # Aliyun account name of the modifier.
        self.modify_user_account_name = modify_user_account_name
        # ID of the organization to which the workspace belongs.
        self.organization_id = organization_id
        # Quick BI user ID of the workspace owner.
        self.owner = owner
        # Aliyun account name of the workspace owner.
        self.owner_account_name = owner_account_name
        self.real_owner_account_name = real_owner_account_name
        # Workspace description.
        self.workspace_description = workspace_description
        # Workspace ID.
        self.workspace_id = workspace_id
        # Name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_publish_operation is not None:
            result['AllowPublishOperation'] = self.allow_publish_operation

        if self.allow_share_operation is not None:
            result['AllowShareOperation'] = self.allow_share_operation

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.create_user_account_name is not None:
            result['CreateUserAccountName'] = self.create_user_account_name

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.modify_user_account_name is not None:
            result['ModifyUserAccountName'] = self.modify_user_account_name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name

        if self.real_owner_account_name is not None:
            result['RealOwnerAccountName'] = self.real_owner_account_name

        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPublishOperation') is not None:
            self.allow_publish_operation = m.get('AllowPublishOperation')

        if m.get('AllowShareOperation') is not None:
            self.allow_share_operation = m.get('AllowShareOperation')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CreateUserAccountName') is not None:
            self.create_user_account_name = m.get('CreateUserAccountName')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('ModifyUserAccountName') is not None:
            self.modify_user_account_name = m.get('ModifyUserAccountName')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')

        if m.get('RealOwnerAccountName') is not None:
            self.real_owner_account_name = m.get('RealOwnerAccountName')

        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

