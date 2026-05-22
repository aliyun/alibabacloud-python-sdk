# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PurgeCachesShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        edge_compute_purge: bool = None,
        force: bool = None,
        site_id: int = None,
        type: str = None,
    ):
        self.content_shrink = content_shrink
        self.edge_compute_purge = edge_compute_purge
        self.force = force
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.edge_compute_purge is not None:
            result['EdgeComputePurge'] = self.edge_compute_purge

        if self.force is not None:
            result['Force'] = self.force

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('EdgeComputePurge') is not None:
            self.edge_compute_purge = m.get('EdgeComputePurge')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

