# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectRequest(DaraModel):
    def __init__(
        self,
        cross_region: bool = None,
    ):
        self.cross_region = cross_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_region is not None:
            result['crossRegion'] = self.cross_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crossRegion') is not None:
            self.cross_region = m.get('crossRegion')

        return self

