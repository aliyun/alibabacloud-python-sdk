# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ResourceLimitDetails(DaraModel):
    def __init__(
        self,
        gclevel: str = None,
        resource_limit: Dict[str, Any] = None,
        should_ignore_resource_check: bool = None,
    ):
        self.gclevel = gclevel
        self.resource_limit = resource_limit
        self.should_ignore_resource_check = should_ignore_resource_check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gclevel is not None:
            result['GCLevel'] = self.gclevel

        if self.resource_limit is not None:
            result['ResourceLimit'] = self.resource_limit

        if self.should_ignore_resource_check is not None:
            result['ShouldIgnoreResourceCheck'] = self.should_ignore_resource_check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GCLevel') is not None:
            self.gclevel = m.get('GCLevel')

        if m.get('ResourceLimit') is not None:
            self.resource_limit = m.get('ResourceLimit')

        if m.get('ShouldIgnoreResourceCheck') is not None:
            self.should_ignore_resource_check = m.get('ShouldIgnoreResourceCheck')

        return self

