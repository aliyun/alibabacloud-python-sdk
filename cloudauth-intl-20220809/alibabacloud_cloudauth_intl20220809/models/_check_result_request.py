# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckResultRequest(DaraModel):
    def __init__(
        self,
        extra_image_control_list: str = None,
        is_return_image: str = None,
        merchant_biz_id: str = None,
        return_five_category_spoof_result: str = None,
        transaction_id: str = None,
    ):
        # The additional information to return.
        self.extra_image_control_list = extra_image_control_list
        # Specifies whether to return images. Valid values:
        # - Y: Return images.
        # - N: Do not return images.
        self.is_return_image = is_return_image
        # The merchant-defined unique business ID used for subsequent troubleshooting. The value can be a combination of letters and digits with a maximum length of 32 characters. Ensure that the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # Specifies whether to return the anti-spoofing detection result.
        self.return_five_category_spoof_result = return_five_category_spoof_result
        # The verification ID.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_image_control_list is not None:
            result['ExtraImageControlList'] = self.extra_image_control_list

        if self.is_return_image is not None:
            result['IsReturnImage'] = self.is_return_image

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.return_five_category_spoof_result is not None:
            result['ReturnFiveCategorySpoofResult'] = self.return_five_category_spoof_result

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraImageControlList') is not None:
            self.extra_image_control_list = m.get('ExtraImageControlList')

        if m.get('IsReturnImage') is not None:
            self.is_return_image = m.get('IsReturnImage')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('ReturnFiveCategorySpoofResult') is not None:
            self.return_five_category_spoof_result = m.get('ReturnFiveCategorySpoofResult')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

