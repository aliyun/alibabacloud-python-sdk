# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class OfflineSkillRequest(DaraModel):
    def __init__(
        self,
        body: main_models.OfflineSkillRequestBody = None,
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
            temp_model = main_models.OfflineSkillRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class OfflineSkillRequestBody(DaraModel):
    def __init__(
        self,
        scope: str = None,
        skill_version: str = None,
    ):
        # The operation scope. Valid values:
        # - skill: the entire Skill.
        # - version: a specified version.
        self.scope = scope
        # The Skill version number.
        self.skill_version = skill_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scope is not None:
            result['scope'] = self.scope

        if self.skill_version is not None:
            result['skillVersion'] = self.skill_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('skillVersion') is not None:
            self.skill_version = m.get('skillVersion')

        return self

