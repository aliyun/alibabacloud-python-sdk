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
        # The request status code. Valid values:
        # 
        # - **OK**: The request was successful.
        # 
        # - **OperatorLimit**: The carrier restricts queries for this phone number.
        # 
        # - **RequestFrequencyLimit**: Indicates that requests for a single number are too frequent. Due to carrier restrictions, repeated queries for the same number within a short period are prohibited. If you receive this error code, try again later.
        self.code = code
        # A container for the returned data.
        self.data = data
        # The description of the status code.
        self.message = message
        # The unique ID of the request. Use this ID to troubleshoot issues.
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
        # The carrier of the phone number. If the number has been ported, this parameter returns the current carrier. Valid values:
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
        # - **NORMAL**: Active.
        # 
        # - **SHUTDOWN**: Shutdown.
        # 
        # - **POWER_OFF**: Powered off.
        # 
        # - **NOT_EXIST**: Non-existent number.
        # 
        # - **DEFECT**: Invalid number.
        # 
        # - **UNKNOWN**: Unknown.
        # 
        # > Due to carrier system adjustments, the statuses for busy, suspected to be powered off, and powered off are not returned for China Telecom numbers. For more information, see the [official announcement](https://help.aliyun.com/document_detail/2489709.html).
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

