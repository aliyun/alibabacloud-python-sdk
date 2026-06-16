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
        # The response code. A value of 200 indicates success. Other values indicate failure.
        self.code = code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The result information.
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
        # - 1: Verification consistent (billable).
        # - 2: Verification inconsistent (billable).
        # - 3: No record found (not billable).
        self.biz_code = biz_code
        # The verification details. Valid values:
        # 
        # - **101**: Verification passed.
        # - **201**: Authentication information inconsistent. The cardholder information is incorrect.
        # - **202**: Authentication information inconsistent. The bank card has not enabled authenticated payment.
        # - **203**: Authentication information inconsistent. The bank card has expired.
        # - **204**: Authentication information inconsistent. The bank card is restricted.
        # - **205**: Authentication information inconsistent. The card has been confiscated.
        # - **206**: Authentication information inconsistent. The bank card is invalid.
        # - **207**: Authentication information inconsistent. No issuing bank found for this card.
        # - **208**: Authentication information inconsistent. The card is not initialized or is a dormant card.
        # - **209**: Authentication information inconsistent. The card is a fraudulent or retained card.
        # - **210**: Authentication information inconsistent. The card has been reported lost.
        # - **211**: Authentication information inconsistent. The number of incorrect password attempts has exceeded the limit.
        # - **212**: Authentication information inconsistent. The issuing bank does not support this transaction.
        # - **213**: Authentication information inconsistent. The card status is abnormal or the card is invalid.
        # - **214**: Authentication information inconsistent. No phone number is registered with the card.
        # - **215**: Authentication information inconsistent. The password, expiration date, or CVN2 is incorrect.
        # - **216**: Authentication information inconsistent. Other card exceptions.
        # - **301**: Verification unavailable. The bank card does not support this service.
        # - **302**: Verification unavailable. Verification failed or the bank rejected the verification. Contact the issuing bank.
        # - **303**: Verification unavailable. The bank card does not currently support phone number verification.
        # - **304**: Verification unavailable. The bank card number is incorrect.
        # - **305**: Verification unavailable. Other reasons.
        # - **306**: Verification unavailable. The number of verification attempts has exceeded the limit.
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

