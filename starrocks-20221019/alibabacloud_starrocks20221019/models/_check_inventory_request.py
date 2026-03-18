# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInventoryRequest(DaraModel):
    def __init__(
        self,
        cluster_info: str = None,
        zone_id: str = None,
    ):
        self.cluster_info = cluster_info
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

