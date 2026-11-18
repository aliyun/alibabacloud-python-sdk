# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LocationInfo(DaraModel):
    def __init__(
        self,
        city: str = None,
        ip: str = None,
    ):
        # The city associated with the search. It is used to return information about the corresponding region in scenarios such as weather.
        self.city = city
        # The IP address associated with the search. It is used to identify the region in supported scenarios and has a lower priority than city.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city

        if self.ip is not None:
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self

