# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CooperationShop(DaraModel):
    def __init__(
        self,
        cooperation_company_id: str = None,
        cooperation_shop_id: str = None,
        shop_id: str = None,
    ):
        self.cooperation_company_id = cooperation_company_id
        self.cooperation_shop_id = cooperation_shop_id
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooperation_company_id is not None:
            result['cooperationCompanyId'] = self.cooperation_company_id

        if self.cooperation_shop_id is not None:
            result['cooperationShopId'] = self.cooperation_shop_id

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cooperationCompanyId') is not None:
            self.cooperation_company_id = m.get('cooperationCompanyId')

        if m.get('cooperationShopId') is not None:
            self.cooperation_shop_id = m.get('cooperationShopId')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        return self

