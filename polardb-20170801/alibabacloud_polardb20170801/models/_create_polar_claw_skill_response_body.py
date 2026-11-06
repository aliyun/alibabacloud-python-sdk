# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawSkillResponseBody(DaraModel):
    def __init__(
        self,
        is_update: str = None,
        request_id: str = None,
        skill_name: str = None,
    ):
        # Used for system scheduled task checks. Modifications are not supported for the current scheduled task.
        self.is_update = is_update
        # The request ID.
        self.request_id = request_id
        # The name of the skill.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_update is not None:
            result['IsUpdate'] = self.is_update

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsUpdate') is not None:
            self.is_update = m.get('IsUpdate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

