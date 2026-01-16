# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigBucketPrefixFilterConfigValue(DaraModel):
    def __init__(
        self,
        prefix_filter_type: str = None,
        prefix_filters: List[str] = None,
    ):
        self.prefix_filter_type = prefix_filter_type
        self.prefix_filters = prefix_filters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type

        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')

        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')

        return self

