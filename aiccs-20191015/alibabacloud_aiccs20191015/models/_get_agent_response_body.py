# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        agent_id: int = None,
        display_name: str = None,
        group_list: List[main_models.GetAgentResponseBodyDataGroupList] = None,
        status: int = None,
        tenant_id: int = None,
    ):
        self.account_name = account_name
        self.agent_id = agent_id
        self.display_name = display_name
        self.group_list = group_list
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        if self.group_list:
            for v1 in self.group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['GroupList'] = []
        if self.group_list is not None:
            for k1 in self.group_list:
                result['GroupList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.group_list = []
        if m.get('GroupList') is not None:
            for k1 in m.get('GroupList'):
                temp_model = main_models.GetAgentResponseBodyDataGroupList()
                self.group_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class GetAgentResponseBodyDataGroupList(DaraModel):
    def __init__(
        self,
        channel_type: int = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        skill_group_id: int = None,
    ):
        self.channel_type = channel_type
        self.description = description
        self.display_name = display_name
        self.name = name
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

