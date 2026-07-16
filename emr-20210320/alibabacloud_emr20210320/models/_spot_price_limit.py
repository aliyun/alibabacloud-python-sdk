# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')

        return self

