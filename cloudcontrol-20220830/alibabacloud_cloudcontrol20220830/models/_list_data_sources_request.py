# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListDataSourcesRequest(DaraModel):
    def __init__(
        self,
        attribute_name: str = None,
        filter: Dict[str, Any] = None,
    ):
        # The name of the attribute. Only `RegionId` is supported.
        # 
        # This parameter is required.
        self.attribute_name = attribute_name
        # The filter condition. The value must be a JSON string in the {"key1":"value1"} format.
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['attributeName'] = self.attribute_name

        if self.filter is not None:
            result['filter'] = self.filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributeName') is not None:
            self.attribute_name = m.get('attributeName')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        return self

