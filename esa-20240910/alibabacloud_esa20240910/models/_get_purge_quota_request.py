# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPurgeQuotaRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        type: str = None,
    ):
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The refresh task type. Valid values:
        # - **file** (default): file refresh.
        # - **cachetag**: cache tag refresh.
        # - **directory**: directory refresh.
        # - **ignoreParams**: ignore-parameters refresh.
        # - **hostname**: hostname refresh.
        # - **purgeall**: purge all cache under the site.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

