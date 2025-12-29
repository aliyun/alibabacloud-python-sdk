# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class PhoneNumberStatusForSmsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PhoneNumberStatusForSmsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **OperatorLimit**: The carrier prohibits the query of the phone number.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The unique request ID. It is a common parameter and can be used to troubleshoot issues.
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
            temp_model = main_models.PhoneNumberStatusForSmsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PhoneNumberStatusForSmsResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        # The basic carrier who assigns the phone number. If the queried phone number involves mobile number portability, the carrier after mobile number portability is returned. Valid values:
        # 
        # *   **CMCC**: China Mobile
        # *   **CUCC**: China Unicom
        # *   **CTCC**: China Telecom
        # 
        # >  You are not allowed to query the phone numbers assigned by China Broadnet.
        self.carrier = carrier
        # The returned status for the queried phone number. Valid values:
        # 
        # *   **NORMAL**: The queried phone number can be reached.
        # *   **SHUTDOWN**: The queried phone number is suspended.
        # *   **POWER_OFF**: The phone is powered off.
        # *   **NOT_EXIST**: The queried phone number is a nonexistent number.
        # *   **DEFECT**: The queried phone number is invalid.
        # *   **UNKNOWN**: The queried phone number is unknown.
        # 
        # >  Due to system adjustment of the carrier, the BUSY, SUSPECTED_POWER_OFF, and POWER_OFF states cannot be returned for the numbers assigned by China Telecom. [For more information, see the official announcements](https://help.aliyun.com/document_detail/2489709.html).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

