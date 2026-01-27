# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RiskSceneConfig(DaraModel):
    def __init__(
        self,
        detect_channel: List[str] = None,
        office_channel: List[str] = None,
    ):
        self.detect_channel = detect_channel
        self.office_channel = office_channel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detect_channel is not None:
            result['DetectChannel'] = self.detect_channel

        if self.office_channel is not None:
            result['OfficeChannel'] = self.office_channel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectChannel') is not None:
            self.detect_channel = m.get('DetectChannel')

        if m.get('OfficeChannel') is not None:
            self.office_channel = m.get('OfficeChannel')

        return self

