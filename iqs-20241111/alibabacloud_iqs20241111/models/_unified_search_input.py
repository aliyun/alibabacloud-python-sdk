# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class UnifiedSearchInput(DaraModel):
    def __init__(
        self,
        advanced_params: Dict[str, Any] = None,
        category: str = None,
        contents: main_models.RequestContents = None,
        engine_type: str = None,
        location: str = None,
        location_info: main_models.LocationInfo = None,
        query: str = None,
        time_range: str = None,
    ):
        self.advanced_params = advanced_params
        self.category = category
        self.contents = contents
        self.engine_type = engine_type
        self.location = location
        self.location_info = location_info
        self.query = query
        self.time_range = time_range

    def validate(self):
        if self.contents:
            self.contents.validate()
        if self.location_info:
            self.location_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_params is not None:
            result['advancedParams'] = self.advanced_params

        if self.category is not None:
            result['category'] = self.category

        if self.contents is not None:
            result['contents'] = self.contents.to_map()

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.location is not None:
            result['location'] = self.location

        if self.location_info is not None:
            result['locationInfo'] = self.location_info.to_map()

        if self.query is not None:
            result['query'] = self.query

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedParams') is not None:
            self.advanced_params = m.get('advancedParams')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('contents') is not None:
            temp_model = main_models.RequestContents()
            self.contents = temp_model.from_map(m.get('contents'))

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('locationInfo') is not None:
            temp_model = main_models.LocationInfo()
            self.location_info = temp_model.from_map(m.get('locationInfo'))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

