# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FaceGuardRiskRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        device_token: str = None,
        merchant_biz_id: str = None,
        product_code: str = None,
        type: str = None,
    ):
        # The customer business ID.
        self.biz_id = biz_id
        # The device token obtained from the Face Guard SDK.
        self.device_token = device_token
        # The merchant-defined unique business identifier, used for subsequent troubleshooting. The value can contain letters and digits with a maximum length of 32 characters. Make sure the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # The product code. Set the value to FACE_GUARD.
        self.product_code = product_code
        self.type = type

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

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

