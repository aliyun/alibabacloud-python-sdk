# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetWorkspaceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The error message that is returned if the request failed.
        self.message = message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorkspaceResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        owner_id: str = None,
        region_id: str = None,
        service_account_id: str = None,
        tid: int = None,
        vpc_id: str = None,
        workspace_id: int = None,
        workspace_name: str = None,
    ):
        # The description of the workspace.
        self.description = description
        # The owner ID.
        self.owner_id = owner_id
        # The ID of the region to which the workspace belongs.
        self.region_id = region_id
        # The ID of the service account.
        self.service_account_id = service_account_id
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
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
        if self.description is not None:
            result['Description'] = self.description

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_account_id is not None:
            result['ServiceAccountId'] = self.service_account_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceAccountId') is not None:
            self.service_account_id = m.get('ServiceAccountId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

