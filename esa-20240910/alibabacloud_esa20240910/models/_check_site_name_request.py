# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSiteNameRequest(DaraModel):
    def __init__(
        self,
        site_name: str = None,
    ):
        # The website name.
        # 
        # This parameter is required.
        self.site_name = site_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_name is not None:
            result['SiteName'] = self.site_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        return self

