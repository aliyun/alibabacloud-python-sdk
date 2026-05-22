# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedTransformRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        site_version: int = None,
    ):
        # Site ID, which can be obtained by calling [ListSites](https://help.aliyun.com/document_detail/2850189.html).
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site. For sites with version management enabled, you can use this parameter to specify the effective version of the configuration, defaulting to version 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

