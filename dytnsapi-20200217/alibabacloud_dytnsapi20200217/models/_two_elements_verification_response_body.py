# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class TwoElementsVerificationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TwoElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request status code.
        # 
        # - **OK**: The request was successful.
        # 
        # - For other error codes, see the error code table in this chapter.
        # - **RequestFrequencyLimit**: Due to operator restrictions, repeated high-frequency queries against the same number or name in a short period are prohibited. If this error code is returned, try again later.
        self.code = code
        # The structure.
        self.data = data
        # The description of the status code.
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
            temp_model = main_models.TwoElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TwoElementsVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        is_consistent: int = None,
    ):
        # The basic operator. Valid values:
        # 
        # - **China Mobile**.
        # 
        # - **China Unicom**.
        # 
        # - **China Telecom**.
        # 
        # >Notice: China Broadcasting Network numbers are not currently supported.
        self.basic_carrier = basic_carrier
        # Indicates whether the verification result is consistent. Returns:
        # 
        # - **1**: Consistent.
        # 
        # - **0**: Inconsistent.
        # 
        # - **2**: Not found.
        # 
        # The data update timeliness for different operators and cities is typically T+1 to T+3.
        # The verification results for different operator phone numbers in different states are as follows: 
        # 
        # |Operator/Phone Number Status|Suspended|Empty Number|Cancelled|
        # |--|--|--|--|
        # |China Mobile|Normal verification|Not found|Not found|
        # |China Unicom|Normal verification|Inconsistent|Inconsistent|
        # |China Telecom|Normal verification|Not found|Not found|
        self.is_consistent = is_consistent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier

        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')

        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')

        return self

