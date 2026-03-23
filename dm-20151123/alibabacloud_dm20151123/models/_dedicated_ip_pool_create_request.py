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
        # The IDs of the purchased IP instances. Separate multiple IDs with commas (,). You can obtain the instance IDs from the response of the DedicatedIpNonePoolList operation.
        self.buy_resource_ids = buy_resource_ids
        # The name of the IP pool. The name must be 1 to 50 characters in length. It can contain letters, digits, underscores (_), and hyphens (-). The name cannot be changed after the IP pool is created.
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

