# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLFlowWaste(DaraModel):
    def __init__(
        self,
        useful_sec: int = None,
    ):
        # The cumulative duration of trained trajectories, in seconds.
        self.useful_sec = useful_sec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.useful_sec is not None:
            result['UsefulSec'] = self.useful_sec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsefulSec') is not None:
            self.useful_sec = m.get('UsefulSec')

        return self

