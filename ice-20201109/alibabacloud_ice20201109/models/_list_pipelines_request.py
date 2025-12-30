# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelinesRequest(DaraModel):
    def __init__(
        self,
        speed: str = None,
    ):
        # The type of the MPS queue.
        # 
        # Valid values:
        # 
        # *   Boost: MPS queue with transcoding speed boosted.
        # *   Standard: standard MPS queue.
        # *   NarrowBandHDV2: MPS queue that supports Narrowband HD 2.0.
        self.speed = speed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.speed is not None:
            result['Speed'] = self.speed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')

        return self

