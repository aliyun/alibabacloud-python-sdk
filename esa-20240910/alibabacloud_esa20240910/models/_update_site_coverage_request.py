# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteCoverageRequest(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        site_id: int = None,
    ):
        # The desired service location. Valid values:
        # 
        # *   **domestic**: the Chinese mainland
        # *   **global**: global
        # *   **overseas**: outside the Chinese mainland
        # 
        # This parameter is required.
        self.coverage = coverage
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
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
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

