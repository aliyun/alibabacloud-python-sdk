# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DedicatedIpPoolUpdateRequest(DaraModel):
    def __init__(
        self,
        buy_resource_ids: str = None,
        id: str = None,
        update_resource: bool = None,
    ):
        # Purchased IP instance IDs, separated by commas; sourced from the DedicatedIpNonePoolList API\\"s returned IP purchase instance IDs
        self.buy_resource_ids = buy_resource_ids
        # IP pool ID
        self.id = id
        # Whether to change the associated IP, enter true
        self.update_resource = update_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids

        if self.id is not None:
            result['Id'] = self.id

        if self.update_resource is not None:
            result['UpdateResource'] = self.update_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('UpdateResource') is not None:
            self.update_resource = m.get('UpdateResource')

        return self

