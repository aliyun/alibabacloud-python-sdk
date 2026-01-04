# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEnsRouteEntryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
    ):
        # The description of the route entry. The description must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The ID of the custom route.
        # 
        # This parameter is required.
        self.route_entry_id = route_entry_id
        # The name of the route.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.route_entry_name = route_entry_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        return self

