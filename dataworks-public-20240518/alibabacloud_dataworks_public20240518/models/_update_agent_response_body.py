# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent: main_models.UpdateAgentResponseBodyAgent = None,
        request_id: str = None,
    ):
        # The details of the updated agent.
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
            temp_model = main_models.UpdateAgentResponseBodyAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateAgentResponseBodyAgent(DaraModel):
    def __init__(
        self,
        agent_version: int = None,
        expert_suites: List[main_models.UpdateAgentResponseBodyAgentExpertSuites] = None,
        gmt_create_time: int = None,
        gmt_modified_time: int = None,
        name: str = None,
        skills: List[main_models.UpdateAgentResponseBodyAgentSkills] = None,
    ):
        # The updated agent definition version.
        self.agent_version = agent_version
        # The bound expert suites.
        self.expert_suites = expert_suites
        # The time when the agent was created. The value is a UNIX timestamp in milliseconds.
        self.gmt_create_time = gmt_create_time
        # The time when the agent was last modified. The value is a UNIX timestamp in milliseconds.
        self.gmt_modified_time = gmt_modified_time
        # The name of the agent.
        self.name = name
        # The list of bound skill references after the update.
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
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

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
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        self.expert_suites = []
        if m.get('ExpertSuites') is not None:
            for k1 in m.get('ExpertSuites'):
                temp_model = main_models.UpdateAgentResponseBodyAgentExpertSuites()
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
                temp_model = main_models.UpdateAgentResponseBodyAgentSkills()
                self.skills.append(temp_model.from_map(k1))

        return self

class UpdateAgentResponseBodyAgentSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        skill_id: str = None,
        source: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # The name of the bound custom skill.
        self.name = name
        # The official skill ID.
        self.skill_id = skill_id
        # The source of the skill.
        self.source = source
        # The published version number of the bound custom skill.
        self.version = version
        # The version selection expression.
        self.version_selector = version_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        if self.version_selector is not None:
            result['VersionSelector'] = self.version_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionSelector') is not None:
            self.version_selector = m.get('VersionSelector')

        return self

class UpdateAgentResponseBodyAgentExpertSuites(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        semantic_version: str = None,
        source: str = None,
        suite_id: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # The suite description of the bound version.
        self.description = description
        # The display name of the bound version.
        self.display_name = display_name
        # The suite name of the bound version.
        self.name = name
        # The semantic version of the bound version.
        self.semantic_version = semantic_version
        # The source of the expert suite.
        self.source = source
        # The ID of the expert suite.
        self.suite_id = suite_id
        # The bound published version number.
        self.version = version
        # The version selection expression.
        self.version_selector = version_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.semantic_version is not None:
            result['SemanticVersion'] = self.semantic_version

        if self.source is not None:
            result['Source'] = self.source

        if self.suite_id is not None:
            result['SuiteId'] = self.suite_id

        if self.version is not None:
            result['Version'] = self.version

        if self.version_selector is not None:
            result['VersionSelector'] = self.version_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SemanticVersion') is not None:
            self.semantic_version = m.get('SemanticVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SuiteId') is not None:
            self.suite_id = m.get('SuiteId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionSelector') is not None:
            self.version_selector = m.get('VersionSelector')

        return self

