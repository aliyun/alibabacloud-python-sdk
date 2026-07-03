# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class IdnAuthorityVerifyIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.IdnAuthorityVerifyIntlResponseBodyResult = None,
    ):
        # The response code.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.IdnAuthorityVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class IdnAuthorityVerifyIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_source_info: str = None,
        passed: str = None,
        sub_code: str = None,
        transaction_id: str = None,
    ):
        # The detailed verification results from the data source are described as follows (using the Indonesian data source as an example):
        # - **govId, fullName, dob**: A comparison score equal to 1.0 indicates a complete match with the official data source. A score lower than 1.0 indicates a mismatch. 
        # - **selfiePhoto**: A comparison score greater than 0.8 indicates a match with the official data source. A score equal to or lower than 0.8 indicates a mismatch. 
        # - **liveness**: A score higher than 0.95 indicates a liveness detection risk. 
        # - **imgManipulationScore**: A score higher than 0.95 indicates an image tampering risk.
        self.ext_source_info = ext_source_info
        # Indicates whether the verification is passed. Valid values:
        # - Y: passed.
        # - N: not passed.
        self.passed = passed
        # The sub-result code.
        self.sub_code = sub_code
        # The unique identifier of the authentication request.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_source_info is not None:
            result['ExtSourceInfo'] = self.ext_source_info

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtSourceInfo') is not None:
            self.ext_source_info = m.get('ExtSourceInfo')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

