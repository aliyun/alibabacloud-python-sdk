# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOriginPoolShrinkRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        name: str = None,
        origins_shrink: str = None,
        site_id: int = None,
    ):
        # Whether the origin address pool is enabled:
        # 
        # - true: Enabled;
        # - false: Disabled.
        self.enabled = enabled
        # The name of the origin address pool, which must be unique within a site.
        # 
        # This parameter is required.
        self.name = name
        # Information about the origins added to the origin address pool, with multiple origins passed as an array.
        self.origins_shrink = origins_shrink
        # The site ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) API.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.origins_shrink is not None:
            result['Origins'] = self.origins_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origins') is not None:
            self.origins_shrink = m.get('Origins')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

