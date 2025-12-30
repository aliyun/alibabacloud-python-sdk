# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearAIAgentVoiceprintRequest(DaraModel):
    def __init__(
        self,
        voiceprint_id: str = None,
    ):
        # The unique identifier for the voiceprint.
        self.voiceprint_id = voiceprint_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.voiceprint_id is not None:
            result['VoiceprintId'] = self.voiceprint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VoiceprintId') is not None:
            self.voiceprint_id = m.get('VoiceprintId')

        return self

