# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataEventSelectorRequest(DaraModel):
    def __init__(
        self,
        trail_name: str = None,
    ):
        # The name of the trail.
        # 
        # This parameter is required.
        self.trail_name = trail_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        return self

