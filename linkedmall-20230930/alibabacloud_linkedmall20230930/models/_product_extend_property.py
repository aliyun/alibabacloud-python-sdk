# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductExtendProperty(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The property key.
        # 
        # > Valid values:
        # >
        # > - - `ss_picture_scene` (scene picture)
        # >
        # > - - `ss_picture_white_background` (white background picture)
        # >
        # > - - `extraPeriod` (shelf life)
        # >
        # > - - `itemBoundaryInventoryZeroTag` (Reserved. Ignore this parameter.)
        # >
        # > - - `shoppingShowTitle` (shopping guide title)
        # >
        # > - - `itemCCStatus` (Reserved. Ignore this parameter.)
        # >
        # > - - `brandLogo` (brand logo)
        # >
        # > - - `multipleBuyLimit` (purchase multiple)
        # >
        # > - - `eticket_type` (electronic coupon type)
        # >
        # > - - `eticket_upper_buy_limit` (maximum purchase quantity of electronic coupons per order)
        # >
        # > - - `validity_type` (validity period type of electronic coupon)
        # >
        # > - - `etc_expiry_date` (Validity period of the electronic coupon. Valid only when `validity_type` is `1`.)
        # >
        # > - - `etc_duration_date` (Validity period of the electronic coupon. Valid only when `validity_type` is `2`, `3`, or `5`.)
        # >
        # > - - `f_refund` (Automatic refund ratio for valid electronic coupons)
        # >
        # > - - `refund` (automatic refund ratio for expired electronic coupons)
        # >
        # > - - `writeoff` (Reserved. Ignore this parameter.)
        self.key = key
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

