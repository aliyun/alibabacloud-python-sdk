# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAIAgentVoiceprintShrinkRequest(DaraModel):
    def __init__(
        self,
        input_shrink: str = None,
        voiceprint_id: str = None,
    ):
        # The input file.
        self.input_shrink = input_shrink
        # A unique identifier for the voiceprint. Generate this ID based on your own business rules. Requirement: 1 to 127 characters in length.
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

