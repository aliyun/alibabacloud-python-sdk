# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductSaleInfoQuery(DaraModel):
    def __init__(
        self,
        distributor_shop_id: str = None,
        division_code: str = None,
    ):
        # This parameter is required.
        self.distributor_shop_id = distributor_shop_id
        self.division_code = division_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distributor_shop_id is not None:
            result['distributorShopId'] = self.distributor_shop_id

        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('distributorShopId') is not None:
            self.distributor_shop_id = m.get('distributorShopId')

        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        return self

