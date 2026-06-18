# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSitePauseRequest(DaraModel):
    def __init__(
        self,
        paused: bool = None,
        site_id: int = None,
    ):
        # Indicates whether to pause proxy acceleration for the site. If set to `true`, DNS queries for the site return the record values directly to the client. Valid values:
        # 
        # - true: Pauses proxy acceleration for the site.
        # 
        # - false: Resumes proxy acceleration for the site.
        # 
        # This parameter is required.
        self.paused = paused
        # The site ID. To obtain this ID, call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
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
        if self.paused is not None:
            result['Paused'] = self.paused

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

