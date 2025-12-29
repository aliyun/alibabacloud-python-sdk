# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFaceGuardRiskRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        device_token: str = None,
        outer_order_no: str = None,
        product_code: str = None,
    ):
        # Authentication ID
        self.biz_id = biz_id
        # Risk identification - device token.
        self.device_token = device_token
        # This identifier is used for subsequent troubleshooting, and you need to ensure that this value is unique in your business.
        # 
        # Supports the use of English letters (including uppercase and lowercase) and numbers, with a maximum length of 32 characters.
        self.outer_order_no = outer_order_no
        # Product code, fixed value: FACE_GUARD
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

