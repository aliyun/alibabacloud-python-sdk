# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceVpcRegion(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.region_name is not None:
            result['regionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('regionName') is not None:
            self.region_name = m.get('regionName')

        return self

