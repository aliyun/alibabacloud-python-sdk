# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnsRouteEntryRequest(DaraModel):
    def __init__(
        self,
        route_entry_id: str = None,
    ):
        # The ID of the route that you want to delete.
        # 
        # This parameter is required.
        self.route_entry_id = route_entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        return self

