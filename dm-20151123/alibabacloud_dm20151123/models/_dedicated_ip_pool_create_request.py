# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DedicatedIpPoolCreateRequest(DaraModel):
    def __init__(
        self,
        buy_resource_ids: str = None,
        name: str = None,
    ):
        # Purchased IP instance IDs, separated by commas; derived from the IP purchase instance IDs returned by the DedicatedIpNonePoolList interface.
        self.buy_resource_ids = buy_resource_ids
        # IP pool name;
        # Length should be 1-50 characters, allowing English letters, numbers, _, and -. The name cannot be modified after the IP pool is created.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

