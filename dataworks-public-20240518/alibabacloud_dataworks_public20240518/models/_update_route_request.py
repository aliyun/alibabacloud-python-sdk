# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRouteRequest(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        id: int = None,
    ):
        # The destination CIDR block of the route that you want to update.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The route ID of the network resource.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

