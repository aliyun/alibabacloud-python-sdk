# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvokeSkillShrinkRequest(DaraModel):
    def __init__(
        self,
        params_shrink: str = None,
        skill_id: str = None,
        stream: bool = None,
        source_id_of_assistant_id: str = None,
    ):
        self.params_shrink = params_shrink
        # This parameter is required.
        self.skill_id = skill_id
        self.stream = stream
        self.source_id_of_assistant_id = source_id_of_assistant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params_shrink is not None:
            result['Params'] = self.params_shrink

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.source_id_of_assistant_id is not None:
            result['sourceIdOfAssistantId'] = self.source_id_of_assistant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('sourceIdOfAssistantId') is not None:
            self.source_id_of_assistant_id = m.get('sourceIdOfAssistantId')

        return self

