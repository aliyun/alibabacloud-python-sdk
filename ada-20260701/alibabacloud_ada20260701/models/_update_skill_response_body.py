# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillResponseBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
        skill_id: str = None,
        success: bool = None,
        updated_at: int = None,
    ):
        # The Skill name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # Skill ID。
        self.skill_id = skill_id
        # Returns `true` when the Skill update and optional bundle replacement have been fully committed and confirmed by read-back.
        self.success = success
        # The time when the Skill was updated, in UNIX millisecond timestamp.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.success is not None:
            result['Success'] = self.success

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

