# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHttpResponseHeaderModificationRuleRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        site_id: int = None,
    ):
        # The configuration ID, which can be obtained by calling the [ListHttpResponseHeaderModificationRules](~~ListHttpResponseHeaderModificationRules~~) operation.
        # 
        # This parameter is required.
        self.config_id = config_id
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
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

