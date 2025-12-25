# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteNameExclusiveRequest(DaraModel):
    def __init__(
        self,
        enable: str = None,
        site_id: int = None,
    ):
        # Specifies whether to enable site hold. Valid values:
        # 
        # *   on
        # *   off
        # 
        # This parameter is required.
        self.enable = enable
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
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

