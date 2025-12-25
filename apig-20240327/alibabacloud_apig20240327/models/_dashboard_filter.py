# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DashboardFilter(DaraModel):
    def __init__(
        self,
        route_name: str = None,
    ):
        self.route_name = route_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_name is not None:
            result['routeName'] = self.route_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('routeName') is not None:
            self.route_name = m.get('routeName')

        return self

