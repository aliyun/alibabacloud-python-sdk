# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomizedListHeadersRequest(DaraModel):
    def __init__(
        self,
        lang_type: str = None,
        list_type: str = None,
        region_id: str = None,
    ):
        self.lang_type = lang_type
        self.list_type = list_type
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang_type is not None:
            result['LangType'] = self.lang_type

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

