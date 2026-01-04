# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEnsSaleConditionControlShrinkRequest(DaraModel):
    def __init__(
        self,
        ali_uid_account: str = None,
        commodity_code: str = None,
        custom_account: str = None,
        sale_controls_shrink: str = None,
    ):
        self.ali_uid_account = ali_uid_account
        # This parameter is required.
        self.commodity_code = commodity_code
        self.custom_account = custom_account
        # This parameter is required.
        self.sale_controls_shrink = sale_controls_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid_account is not None:
            result['AliUidAccount'] = self.ali_uid_account

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.custom_account is not None:
            result['CustomAccount'] = self.custom_account

        if self.sale_controls_shrink is not None:
            result['SaleControls'] = self.sale_controls_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUidAccount') is not None:
            self.ali_uid_account = m.get('AliUidAccount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomAccount') is not None:
            self.custom_account = m.get('CustomAccount')

        if m.get('SaleControls') is not None:
            self.sale_controls_shrink = m.get('SaleControls')

        return self

