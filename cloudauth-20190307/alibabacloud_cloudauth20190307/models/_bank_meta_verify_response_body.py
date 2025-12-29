# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class BankMetaVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.BankMetaVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information
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
            temp_model = main_models.BankMetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class BankMetaVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        sub_code: str = None,
    ):
        # Verification result.
        # 
        # - 1: Consistent (billable)
        # - 2: Inconsistent (billable)
        # - 3: No record found (non-billable)
        self.biz_code = biz_code
        # Verification details:
        # 
        # - **101**: Verification passed.
        # - **201**: Authentication information does not match, cardholder information is incorrect.
        # - **202**: Authentication information does not match, bank card has not enabled authentication payment.
        # - **203**: Authentication information does not match, bank card has expired.
        # - **204**: Authentication information does not match, bank card is a restricted card.
        # - **205**: Authentication information does not match, this card has been confiscated.
        # - **206**: Authentication information does not match, bank card is invalid.
        # - **207**: Authentication information does not match, this card has no corresponding issuing bank.
        # - **208**: Authentication information does not match, the card is uninitialized or a dormant card.
        # - **209**: Authentication information does not match, this card is a cheating card or swallowed card.
        # - **210**: Authentication information does not match, this card has been reported lost.
        # - **211**: Authentication information does not match, the number of password errors exceeds the limit.
        # - **212**: Authentication information does not match, the issuing bank does not support this transaction.
        # - **213**: Authentication information does not match, the card status is abnormal or the card is invalid.
        # - **214**: Authentication information does not match, no mobile phone number reserved.
        # - **215**: Authentication information does not match, the entered password, expiration date, or CVN2 is incorrect.
        # - **216**: Authentication information does not match, other card anomalies.
        # - **301**: Unable to verify, the bank card does not support this service.
        # - **302**: Unable to verify, verification failed or the bank refused to verify, please contact the issuing bank.
        # - **303**: Unable to verify, the bank card does not currently support mobile phone number verification.
        # - **304**: Unable to verify, the bank card number is incorrect.
        # - **305**: Unable to verify, other reasons.
        # - **306**: Unable to verify, the number of verifications exceeds the limit.
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

