# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserDefineRegionRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        region_tag: str = None,
    ):
        # The unique ID of the custom namespace. You can call the ListUserDefineRegion operation to query the ID. For more information, see [ListUserDefineRegion](https://help.aliyun.com/document_detail/149377.html).
        self.id = id
        # The tag of the custom namespace.
        self.region_tag = region_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')

        return self

