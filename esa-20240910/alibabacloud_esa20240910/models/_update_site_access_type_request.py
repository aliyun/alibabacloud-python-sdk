# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteAccessTypeRequest(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        site_id: int = None,
    ):
        # The new DNS setup of the website. Valid values:
        # 
        # *   **NS**
        # *   **CNAME**
        # 
        # This parameter is required.
        self.access_type = access_type
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

