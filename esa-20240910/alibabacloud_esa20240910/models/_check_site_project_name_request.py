# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSiteProjectNameRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        site_id: int = None,
    ):
        # The real-time log project name.
        # 
        # > Allowed character set (hyphens only, no underscores), length range, and naming rule examples (such as \\"ali-dcdn-log-56\\")
        # 
        # This parameter is required.
        self.project_name = project_name
        # The site ID. You can call [ListSites](https://help.aliyun.com/document_detail/2850189.html) to obtain the site ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

