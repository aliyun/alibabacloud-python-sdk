# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateServiceMirrorRequest(DaraModel):
    def __init__(
        self,
        ratio: int = None,
        target: List[str] = None,
    ):
        # The percentage of traffic that you want to mirror. Valid values: 0 to 100.
        self.ratio = ratio
        # The service instances.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

