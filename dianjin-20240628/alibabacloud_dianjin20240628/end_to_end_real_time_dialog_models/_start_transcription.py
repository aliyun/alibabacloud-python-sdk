# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class StartTranscription(DaraModel):
    def __init__(
        self,
        play_code: str = None,
        meta_data: Dict[str, Any] = None,
        self_directed: bool = None,
    ):
        # This parameter is required.
        self.play_code = play_code
        self.meta_data = meta_data
        self.self_directed = self_directed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.play_code is not None:
            result['playCode'] = self.play_code

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.self_directed is not None:
            result['selfDirected'] = self.self_directed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('playCode') is not None:
            self.play_code = m.get('playCode')

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('selfDirected') is not None:
            self.self_directed = m.get('selfDirected')

        return self

