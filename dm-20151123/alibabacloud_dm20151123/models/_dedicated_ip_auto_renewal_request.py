# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DedicatedIpAutoRenewalRequest(DaraModel):
    def __init__(
        self,
        auto_renewal: str = None,
        buy_resource_ids: str = None,
    ):
        # Whether to enable auto-renewal
        # 
        # This parameter is required.
        self.auto_renewal = auto_renewal
        # Purchase instance ID, separated by English commas if multiple.
        # 
        # This parameter is required.
        self.buy_resource_ids = buy_resource_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.buy_resource_ids is not None:
            result['BuyResourceIds'] = self.buy_resource_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BuyResourceIds') is not None:
            self.buy_resource_ids = m.get('BuyResourceIds')

        return self

