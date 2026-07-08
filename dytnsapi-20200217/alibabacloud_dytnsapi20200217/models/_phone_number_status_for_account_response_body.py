# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class PhoneNumberStatusForAccountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PhoneNumberStatusForAccountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. Valid values:
        # 
        # - **OK**: The request was successful.
        # 
        # - **OperatorLimit**: The query is prohibited by the carrier.
        # 
        # - **RequestFrequencyLimit**: Carriers restrict frequent queries for the same number within a short period. If you receive this error code, try again later.
        self.code = code
        # The response object.
        self.data = data
        # The description of the status code.
        self.message = message
        # The ID of the request. This ID is unique to each request and can be used for troubleshooting.
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
            temp_model = main_models.PhoneNumberStatusForAccountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PhoneNumberStatusForAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier: str = None,
        status: str = None,
    ):
        # The number\\"s current carrier. If the number has been ported to a new carrier through mobile number portability, the new carrier is returned. Valid values:
        # 
        # - **CMCC**: China Mobile
        # 
        # - **CUCC**: China Unicom
        # 
        # - **CTCC**: China Telecom
        # 
        # > Queries for China Broadnet numbers are not supported.
        self.carrier = carrier
        # The status of the phone number. Valid values:
        # 
        # - **NORMAL**: The number is active.
        # 
        # - **SHUTDOWN**: The number is suspended or temporarily out of service.
        # 
        # - **POWER_OFF**: The phone is powered off.
        # 
        # - **NOT_EXIST**: The number is non-existent.
        # 
        # - **DEFECT**: The number is invalid.
        # 
        # - **UNKNOWN**: The status is unknown.
        # 
        # > Due to adjustments in the carrier\\"s system, China Telecom numbers do not return the `busy` and `powered off` statuses. For more information, [see the official announcement](https://help.aliyun.com/document_detail/2489709.html).
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

