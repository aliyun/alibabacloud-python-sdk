# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdatePolarClawSkillRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        application_id: str = None,
        enabled: bool = None,
        env: Dict[str, str] = None,
        skill_key: str = None,
    ):
        # The Skill API key. An empty string indicates that the key is deleted.
        self.api_key = api_key
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # Specifies whether to enable the Skill.
        self.enabled = enabled
        # The environment variables as a key-value map. A null value indicates that the variable is deleted.
        self.env = env
        # The Skill identifier key.
        # 
        # This parameter is required.
        self.skill_key = skill_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.env is not None:
            result['Env'] = self.env

        if self.skill_key is not None:
            result['SkillKey'] = self.skill_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('SkillKey') is not None:
            self.skill_key = m.get('SkillKey')

        return self

