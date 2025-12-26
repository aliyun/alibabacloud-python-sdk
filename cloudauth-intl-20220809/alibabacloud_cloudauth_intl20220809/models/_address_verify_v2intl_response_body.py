# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class AddressVerifyV2IntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.AddressVerifyV2IntlResponseBodyResult = None,
    ):
        # [Return Code](https://www.alibabacloud.com/help/zh/ekyc/latest/add-verify-pro-api?spm=a2c63.p38356.0.i4#ae60001a3804w)
        self.code = code
        # Detailed description of the return code
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Result object
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.AddressVerifyV2IntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class AddressVerifyV2IntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        detail: str = None,
        transaction_id: str = None,
    ):
        # The verification result. Valid values:
        # 
        # - **1**: Passed (billed)
        # - **2**: Failed (The device is in a prohibited region) (billed)
        # - **3**: Unknown (billed)
        self.biz_code = biz_code
        # Verification details, including：
        # 
        # - **DistanceRange**：Position rang：[DistanceRange description](https://www.alibabacloud.com/help/zh/ekyc/latest/add-verify-pro-api?spm=a2c63.p38356.0.i27#ee274c08976er)。
        # > If the input phone number or address is empty, or if no carrier information is found, this field will not be returned.
        # 
        # - **IspName**: The carrier name:
        #    - **CMCC**: China Mobile
        #    - **CTCC**: China Telecom
        #    - **CUCC**: China Unicom
        # > This parameter is not returned if the mobile phone number or address is empty in the request, or if carrier information is not found.
        # 
        # - **PhoneStatus**: The status of the mobile phone:
        #   - **0**: Abnormal
        #   - **1**: Normal
        # 
        # > This parameter is not returned if the mobile phone number is empty in the request.
        self.detail = detail
        # The transaction ID
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

