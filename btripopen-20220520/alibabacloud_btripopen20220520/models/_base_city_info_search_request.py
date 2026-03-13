# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BaseCityInfoSearchRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.keyword = keyword
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

