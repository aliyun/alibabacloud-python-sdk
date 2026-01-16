# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagsRequest(DaraModel):
    def __init__(
        self,
        page_size: int = None,
        resource_type: str = None,
    ):
        # The return results.
        self.page_size = page_size
        # The tag value of the ENI.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

