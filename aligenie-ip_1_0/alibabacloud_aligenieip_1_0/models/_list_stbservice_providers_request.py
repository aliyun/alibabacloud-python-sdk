# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSTBServiceProvidersRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        province: str = None,
    ):
        # This parameter is required.
        self.city = city
        # This parameter is required.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

