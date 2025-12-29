# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneTwiceTelVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePhoneTwiceTelVerifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **PortabilityNumberNotSupported**: The phone number that is involved in mobile number portability is not supported.
        # *   **RequestNumberNotSupported**: You are not allowed to query phone numbers assigned by China Broadnet (that is, phone numbers start with 192) and phone numbers assigned by virtual network operators (VNOs).
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        # 
        # >  You are charged for phone number verifications if the value of Code is OK and the value of VerifyResult is not 0. For more information, see [Pricing](https://help.aliyun.com/document_detail/154751.html).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot and locate issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePhoneTwiceTelVerifyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneTwiceTelVerifyResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier: str = None,
        verify_result: str = None,
    ):
        # The carrier. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  The returned result indicates the carrier who assigns the phone number. If the phone number involves mobile number portability, the carrier after mobile number portability is returned.
        self.carrier = carrier
        # The result of the request. Valid values:
        # 
        # *   **0**: It is unable to judge whether the phone number is a reassigned number.
        # *   **1**: The phone number is a reassigned number.
        # *   **2**: The phone number is not a reassigned number.
        # *   **3**: The phone number has been canceled.
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

