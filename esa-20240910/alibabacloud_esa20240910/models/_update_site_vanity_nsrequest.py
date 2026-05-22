# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteVanityNSRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        vanity_nslist: str = None,
    ):
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The custom nameserver names. You can specify two to five custom nameserver names. Separate multiple names with commas (,).
        self.vanity_nslist = vanity_nslist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.vanity_nslist is not None:
            result['VanityNSList'] = self.vanity_nslist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('VanityNSList') is not None:
            self.vanity_nslist = m.get('VanityNSList')

        return self

