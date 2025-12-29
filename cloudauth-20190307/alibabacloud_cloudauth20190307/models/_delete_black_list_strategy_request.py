# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBlackListStrategyRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        product_name: str = None,
        region_id: str = None,
    ):
        # Rule ID.
        self.id = id
        # Product Name:
        # - **id2meta**: ID card two-factor verification
        # - **mobile3Meta**: Mobile phone number factor verification
        # - **bankcardMeta**: Bank card factor verification
        self.product_name = product_name
        # Region ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

