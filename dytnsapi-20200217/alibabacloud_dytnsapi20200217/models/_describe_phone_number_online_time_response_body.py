# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneNumberOnlineTimeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePhoneNumberOnlineTimeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request status code. Valid values:
        # 
        # - **OK**: The request was successful.
        # - **PortabilityNumberNotSupported**: The mobile number portability number is not supported.
        # - **RequestFrequencyLimit**: Due to carrier restrictions, frequent repeated queries on the same number within a short period are prohibited. If this error code is returned, try again later.
        # 
        # > Charges are incurred when Code is OK and VerifyResult is not -1. For billing details, see [Cell Phone Number Service Pricing](https://help.aliyun.com/document_detail/154751.html).
        # >
        self.code = code
        # The returned data.
        self.data = data
        # The description of the number status code.
        self.message = message
        # The request ID.
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
            temp_model = main_models.DescribePhoneNumberOnlineTimeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneNumberOnlineTimeResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier_code: str = None,
        verify_result: str = None,
    ):
        # The carrier SMS status code. Valid values:
        # - **CMCC**: China Mobile
        # - **CUCC**: China Unicom
        # - **CTCC**: China Telecom
        # - **CBN**: China Broadnet
        self.carrier_code = carrier_code
        # The enumeration value of the network registration duration. Valid values:
        # 
        # - **-1**: No duration was found.
        # - **0**: Abnormal phone status, for example, a non-existent number.
        # - **1**: [0-3) months.
        # - **2**: [3-6) months.
        # - **3**: [6-12) months.
        # - **4**: [12-24) months.
        # - **5**: [24,+∞) months.
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carrier_code is not None:
            result['CarrierCode'] = self.carrier_code

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CarrierCode') is not None:
            self.carrier_code = m.get('CarrierCode')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

