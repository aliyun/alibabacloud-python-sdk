# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateAgentSkillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        skill_info: List[main_models.CreateAgentSkillResponseBodySkillInfo] = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The skill information.
        self.skill_info = skill_info

    def validate(self):
        if self.skill_info:
            for v1 in self.skill_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillInfo'] = []
        if self.skill_info is not None:
            for k1 in self.skill_info:
                result['SkillInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_info = []
        if m.get('SkillInfo') is not None:
            for k1 in m.get('SkillInfo'):
                temp_model = main_models.CreateAgentSkillResponseBodySkillInfo()
                self.skill_info.append(temp_model.from_map(k1))

        return self

class CreateAgentSkillResponseBodySkillInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        instruction: str = None,
        skill_id: str = None,
        skill_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The skill description.
        self.description = description
        # The skill summary.
        self.instruction = instruction
        # The unique ID of the skill.
        self.skill_id = skill_id
        # The skill name.
        self.skill_name = skill_name
        # The skill status.
        self.status = status
        # The skill type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

