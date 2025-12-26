# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class AddressVerifyIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.AddressVerifyIntlResponseBodyResultObject = None,
    ):
        # Return code.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result information.
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
            temp_model = main_models.AddressVerifyIntlResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class AddressVerifyIntlResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        address_info: str = None,
        isp_name: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # Address verification details.
        self.address_info = address_info
        # Operator name:
        # - CMCC: China Mobile
        # - CTCC: China Telecom
        # - CUCC: China Unicom
        self.isp_name = isp_name
        # Verification result, values:
        # - Y: Yes, the verified address distance is less than or equal to 10KM.
        # - N: No, the verified address distance is greater than 10KM.
        self.passed = passed
        # Authentication result description.
        self.sub_code = sub_code
        # Unique identifier for the authentication request.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

