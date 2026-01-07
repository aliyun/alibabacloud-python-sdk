# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListDataAgentWorkspaceMemberResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataAgentWorkspaceMemberResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataAgentWorkspaceMemberResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataAgentWorkspaceMemberResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListDataAgentWorkspaceMemberResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.content = content
        self.max_results = max_results
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
                temp_model = main_models.ListDataAgentWorkspaceMemberResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListDataAgentWorkspaceMemberResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        join_time: str = None,
        member_id: str = None,
        role_name: str = None,
        running_task_number: int = None,
        total_task_number: int = None,
        user_name: str = None,
    ):
        self.join_time = join_time
        self.member_id = member_id
        self.role_name = role_name
        self.running_task_number = running_task_number
        self.total_task_number = total_task_number
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_time is not None:
            result['JoinTime'] = self.join_time

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.running_task_number is not None:
            result['RunningTaskNumber'] = self.running_task_number

        if self.total_task_number is not None:
            result['TotalTaskNumber'] = self.total_task_number

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('RunningTaskNumber') is not None:
            self.running_task_number = m.get('RunningTaskNumber')

        if m.get('TotalTaskNumber') is not None:
            self.total_task_number = m.get('TotalTaskNumber')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

