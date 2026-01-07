# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class UpdateDataAgentWorkspaceMemberRoleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateDataAgentWorkspaceMemberRoleResponseBodyData = None,
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
            temp_model = main_models.UpdateDataAgentWorkspaceMemberRoleResponseBodyData()
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

class UpdateDataAgentWorkspaceMemberRoleResponseBodyData(DaraModel):
    def __init__(
        self,
        join_time: int = None,
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

