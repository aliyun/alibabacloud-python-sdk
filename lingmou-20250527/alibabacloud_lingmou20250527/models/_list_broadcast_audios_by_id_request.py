# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListBroadcastAudiosByIdRequest(DaraModel):
    def __init__(
        self,
        audio_ids: List[str] = None,
    ):
        self.audio_ids = audio_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_ids is not None:
            result['audioIds'] = self.audio_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioIds') is not None:
            self.audio_ids = m.get('audioIds')

        return self

