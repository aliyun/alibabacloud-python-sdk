# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent: main_models.CreateAgentResponseBodyAgent = None,
        request_id: str = None,
    ):
        # The details of the created agent.
        self.agent = agent
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.agent:
            self.agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.CreateAgentResponseBodyAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateAgentResponseBodyAgent(DaraModel):
    def __init__(
        self,
        expert_suites: List[main_models.CreateAgentResponseBodyAgentExpertSuites] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        name: str = None,
        skills: List[main_models.CreateAgentResponseBodyAgentSkills] = None,
    ):
        # 已保存的套件引用。官方资源返回来源及目录 ID；发布后的制品版本由 PackageVersion 表示。
        self.expert_suites = expert_suites
        # The creation time. The value is a UNIX timestamp in milliseconds.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # The last modification time. The value is a UNIX timestamp in milliseconds.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        # The name of the agent.
        self.name = name
        # 已保存的 Skill 引用；官方 Skill 在 Agent 发布后返回固定的 PackageVersion。
        self.skills = skills

    def validate(self):
        if self.expert_suites:
            for v1 in self.expert_suites:
                 if v1:
                    v1.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExpertSuites'] = []
        if self.expert_suites is not None:
            for k1 in self.expert_suites:
                result['ExpertSuites'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.name is not None:
            result['Name'] = self.name

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expert_suites = []
        if m.get('ExpertSuites') is not None:
            for k1 in m.get('ExpertSuites'):
                temp_model = main_models.CreateAgentResponseBodyAgentExpertSuites()
                self.expert_suites.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.CreateAgentResponseBodyAgentSkills()
                self.skills.append(temp_model.from_map(k1))

        return self

class CreateAgentResponseBodyAgentSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        package_version: str = None,
        skill_id: str = None,
        source: str = None,
        version: int = None,
    ):
        self.name = name
        # 创建时不返回；请使用 GetAgent 显式查询已发布版本获取固定的官方制品版本。
        self.package_version = package_version
        self.skill_id = skill_id
        self.source = source
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateAgentResponseBodyAgentExpertSuites(DaraModel):
    def __init__(
        self,
        package_version: str = None,
        source: str = None,
        suite_id: str = None,
        version: int = None,
    ):
        # 创建时不返回；请使用 GetAgent 显式查询已发布版本获取固定的官方套件制品版本。
        self.package_version = package_version
        self.source = source
        self.suite_id = suite_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.source is not None:
            result['Source'] = self.source

        if self.suite_id is not None:
            result['SuiteId'] = self.suite_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SuiteId') is not None:
            self.suite_id = m.get('SuiteId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

