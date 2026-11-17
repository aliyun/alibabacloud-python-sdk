# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class BankMetaVerifyIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.BankMetaVerifyIntlResponseBodyResultObject = None,
    ):
        # The return code. A value of 200 indicates success, and other values indicate failure.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result information.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.BankMetaVerifyIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class BankMetaVerifyIntlResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        sub_code: str = None,
    ):
        # The verification result code. Valid values:
        # - 1: The verification is consistent. You are billed for this call.
        # - 2: The verification is inconsistent. You are billed for this call.
        # - 3: No record is found. You are not billed for this call.
        self.biz_code = biz_code
        # The verification details. Valid values:
        # 
        # - **101**: The verification is successful.
        # - **201**: The authentication information is inconsistent. The cardholder information is incorrect.
        # - **202**: The authentication information is inconsistent. The bank card is not enabled for authenticated payment.
        # - **203**: The authentication information is inconsistent. The bank card has expired.
        # - **204**: The authentication information is inconsistent. The bank card is restricted.
        # - **205**: The authentication information is inconsistent. The bank card has been confiscated.
        # - **206**: The authentication information is inconsistent. The bank card is invalid.
        # - **207**: The authentication information is inconsistent. The bank card has no corresponding issuing bank.
        # - **208**: The authentication information is inconsistent. The bank card is not initialized or is a dormant card.
        # - **209**: The authentication information is inconsistent. The bank card is a fraudulent or captured card.
        # - **210**: The authentication information is inconsistent. The bank card has been reported as lost.
        # - **211**: The authentication information is inconsistent. The number of incorrect password attempts has exceeded the limit.
        # - **212**: The authentication information is inconsistent. The issuing bank does not support this transaction.
        # - **213**: The authentication information is inconsistent. The card status is abnormal or the card is invalid.
        # - **214**: The authentication information is inconsistent. No mobile phone number is reserved.
        # - **215**: The authentication information is inconsistent. The entered password, expiration date, or CVN2 is incorrect.
        # - **216**: The authentication information is inconsistent. Other card exceptions occurred.
        # - **301**: The verification cannot be performed. The bank card does not support this service.
        # - **302**: The verification cannot be performed. The verification failed or the bank rejected the verification. Contact the issuing bank.
        # - **303**: The verification cannot be performed. The bank card does not support mobile phone number verification.
        # - **304**: The verification cannot be performed. The bank card number is incorrect.
        # - **305**: The verification cannot be performed. Other reasons.
        # - **306**: The verification cannot be performed. The number of verification attempts has exceeded the limit.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

