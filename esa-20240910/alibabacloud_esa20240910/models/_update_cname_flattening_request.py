# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCnameFlatteningRequest(DaraModel):
    def __init__(
        self,
        flatten_mode: str = None,
        site_id: int = None,
    ):
        # The CNAME flattening mode. Valid values:
        # 
        # *   flatten_all: flattens all CNAMEs.
        # *   flatten_at_root: flattens only the root domain. Default: flatten_at_root
        # 
        # This parameter is required.
        self.flatten_mode = flatten_mode
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
        if self.flatten_mode is not None:
            result['FlattenMode'] = self.flatten_mode

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlattenMode') is not None:
            self.flatten_mode = m.get('FlattenMode')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

