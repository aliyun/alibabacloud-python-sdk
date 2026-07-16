# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class PhoneNumberStatusForRealResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PhoneNumberStatusForRealResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request status code. Valid values:
        # 
        # - **OK**: The request was successful.
        # 
        # - **OperatorLimit**: The query for the phone number is restricted by the carrier.
        # 
        # - **RequestFrequencyLimit**: Carriers prohibit high-frequency queries for the same number within a short period. If this error code is returned, try again later.
        self.code = code
        # The data returned for the request.
        self.data = data
        # The description of the status code.
        self.message = message
        # A unique identifier for the request. You can use this ID to troubleshoot issues.
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
            temp_model = main_models.PhoneNumberStatusForRealResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PhoneNumberStatusForRealResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        # The carrier that provides service for the phone number. If the number has been ported through mobile number portability (MNP), this field returns the new carrier. Valid values:
        # 
        # - **CMCC**: China Mobile.
        # 
        # - **CUCC**: China Unicom.
        # 
        # - **CTCC**: China Telecom.
        # 
        # > Queries for China Broadnet numbers are not supported.
        self.carrier = carrier
        # The status of the phone number. Valid values:
        # 
        # - **NORMAL**: The number is in service.
        # 
        # - **SHUTDOWN**: The service for the number is suspended.
        # 
        # - **POWER_OFF**: The phone is powered off.
        # 
        # - **NOT_EXIST**: The number is not in service.
        # 
        # - **BUSY**: The line is busy.
        # 
        # - **SUSPECTED_POWER_OFF**: The phone is suspected to be powered off.
        # 
        # - **DEFECT**: The number is invalid.
        # 
        # - **UNKNOWN**: The status is unknown.
        # 
        # > Due to carrier system adjustments, China Telecom numbers no longer return the `BUSY`, `SUSPECTED_POWER_OFF`, and `POWER_OFF` statuses. For more information, see the [official announcement](https://help.aliyun.com/document_detail/2489709.html).
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

