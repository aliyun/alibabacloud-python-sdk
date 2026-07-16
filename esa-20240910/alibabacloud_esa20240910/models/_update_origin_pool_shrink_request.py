# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOriginPoolShrinkRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        origins_shrink: str = None,
        site_id: int = None,
    ):
        # Specifies whether the origin address pool is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enabled = enabled
        # The origin address pool ID. You can call the [ListOriginPools](~~ListOriginPools~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.id = id
        # The origin server information added to the origin address pool. Use an array to pass multiple origin servers.
        self.origins_shrink = origins_shrink
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.origins_shrink is not None:
            result['Origins'] = self.origins_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Origins') is not None:
            self.origins_shrink = m.get('Origins')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

