# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSkillSpaceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        skill_space_description: str = None,
        skill_space_name: str = None,
    ):
        # A client-generated token to ensure the idempotence of the request. The token must be unique across requests. The **ClientToken** value can contain only ASCII characters and must be no more than 64 characters in length.
        self.client_token = client_token
        # The description of the skill space.
        # 
        # This parameter is required.
        self.skill_space_description = skill_space_description
        # The name of the skill space.
        # 
        # This parameter is required.
        self.skill_space_name = skill_space_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.skill_space_description is not None:
            result['SkillSpaceDescription'] = self.skill_space_description

        if self.skill_space_name is not None:
            result['SkillSpaceName'] = self.skill_space_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('SkillSpaceDescription') is not None:
            self.skill_space_description = m.get('SkillSpaceDescription')

        if m.get('SkillSpaceName') is not None:
            self.skill_space_name = m.get('SkillSpaceName')

        return self

