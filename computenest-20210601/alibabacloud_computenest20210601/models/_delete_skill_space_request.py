# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSkillSpaceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        skill_space_id: str = None,
    ):
        # A client-generated token to ensure the idempotence of the request. The value must be unique for each request. The **ClientToken** supports only ASCII characters and can be up to 64 characters long.
        self.client_token = client_token
        # The ID of the SkillSpace.
        # 
        # This parameter is required.
        self.skill_space_id = skill_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.skill_space_id is not None:
            result['SkillSpaceId'] = self.skill_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('SkillSpaceId') is not None:
            self.skill_space_id = m.get('SkillSpaceId')

        return self

