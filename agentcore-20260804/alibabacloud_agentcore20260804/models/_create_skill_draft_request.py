# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateSkillDraftRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateSkillDraftRequestBody = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.CreateSkillDraftRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class CreateSkillDraftRequestBody(DaraModel):
    def __init__(
        self,
        based_on_version: str = None,
        commit_msg: str = None,
        skill_card: str = None,
        skill_name: str = None,
        target_version: str = None,
    ):
        # The version from which to fork the draft. If not specified, a new Skill is created.
        self.based_on_version = based_on_version
        # The commit message.
        self.commit_msg = commit_msg
        # The Skill card JSON string that contains the complete Skill information.
        self.skill_card = skill_card
        # The Skill name.
        # 
        # This parameter is required.
        self.skill_name = skill_name
        # The draft version number to assign. If not specified, the version number is automatically incremented.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.based_on_version is not None:
            result['basedOnVersion'] = self.based_on_version

        if self.commit_msg is not None:
            result['commitMsg'] = self.commit_msg

        if self.skill_card is not None:
            result['skillCard'] = self.skill_card

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basedOnVersion') is not None:
            self.based_on_version = m.get('basedOnVersion')

        if m.get('commitMsg') is not None:
            self.commit_msg = m.get('commitMsg')

        if m.get('skillCard') is not None:
            self.skill_card = m.get('skillCard')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

