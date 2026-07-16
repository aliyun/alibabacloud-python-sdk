# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KopilotListConversationsRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        region_id: str = None,
        size: int = None,
    ):
        self.page = page
        # This parameter is required.
        self.region_id = region_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

