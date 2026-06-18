# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWafFilterRequest(DaraModel):
    def __init__(
        self,
        phase: str = None,
        site_id: int = None,
        target: str = None,
        type: str = None,
    ):
        # Specifies the WAF phase from which to retrieve the matching engine information.
        self.phase = phase
        # Specifies the ID of the site. You can get this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        self.site_id = site_id
        # Specifies the application target of the matching engine.
        self.target = target
        # Specifies the rule type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phase is not None:
            result['Phase'] = self.phase

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

