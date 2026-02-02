# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateCustomAgentResponseBody(DaraModel):
    def __init__(
        self,
        enable_tools: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        skills: List[main_models.UpdateCustomAgentResponseBodySkills] = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        # Indicates whether tools are enabled.
        self.enable_tools = enable_tools
        # The ID of the agent.
        self.id = id
        # The name of the agent.
        self.name = name
        # The request ID.
        self.request_id = request_id
        self.skills = skills
        # The system prompts.
        self.system_prompt = system_prompt
        # The information about the tool.
        self.tools = tools

    def validate(self):
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools is not None:
            result['Tools'] = self.tools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.UpdateCustomAgentResponseBodySkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        return self

class UpdateCustomAgentResponseBodySkills(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        skill_type: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.skill_type = skill_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        return self

