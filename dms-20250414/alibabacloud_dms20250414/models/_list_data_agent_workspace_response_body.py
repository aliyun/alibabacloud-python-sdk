# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataAgentWorkspaceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataAgentWorkspaceResponseBodyData()
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

        return self

class ListDataAgentWorkspaceResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListDataAgentWorkspaceResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.content = content
        self.page_number = page_number
        self.page_size = page_size
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListDataAgentWorkspaceResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataAgentWorkspaceResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        modify_time: int = None,
        role_name: str = None,
        total_member: int = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.modify_time = modify_time
        self.role_name = role_name
        self.total_member = total_member
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name
        self.workspace_status = workspace_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.total_member is not None:
            result['TotalMember'] = self.total_member

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.workspace_status is not None:
            result['WorkspaceStatus'] = self.workspace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('TotalMember') is not None:
            self.total_member = m.get('TotalMember')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('WorkspaceStatus') is not None:
            self.workspace_status = m.get('WorkspaceStatus')

        return self

