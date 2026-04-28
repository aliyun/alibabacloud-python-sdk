# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryAgentSkillResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryAgentSkillResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudQueryAgentSkillResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryAgentSkillResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudQueryAgentSkillResponseBodyDataList] = None,
    ):
        # 座席技能列表
        self.list = list

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.CloudQueryAgentSkillResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudQueryAgentSkillResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        create_time: str = None,
        enterprise_id: int = None,
        id: int = None,
        skill_id: int = None,
        skill_level: int = None,
        skill_name: str = None,
    ):
        # 座席id
        self.agent_id = agent_id
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 企业编号
        self.enterprise_id = enterprise_id
        # queueSkill关系表中id
        self.id = id
        # skill的id
        self.skill_id = skill_id
        # 技能值
        self.skill_level = skill_level
        # 技能名称
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.id is not None:
            result['Id'] = self.id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_level is not None:
            result['SkillLevel'] = self.skill_level

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillLevel') is not None:
            self.skill_level = m.get('SkillLevel')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

