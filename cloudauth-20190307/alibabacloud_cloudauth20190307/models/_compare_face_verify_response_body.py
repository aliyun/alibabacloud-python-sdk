# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class CompareFaceVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.CompareFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, other values indicate failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Face comparison result information.
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
            temp_model = main_models.CompareFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CompareFaceVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        passed: str = None,
        verify_score: float = None,
    ):
        # Unique identifier for the real-person authentication request.
        self.certify_id = certify_id
        # Whether the verification passed, T for pass, F for fail.
        self.passed = passed
        # Face comparison score.
        self.verify_score = verify_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.verify_score is not None:
            result['VerifyScore'] = self.verify_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('VerifyScore') is not None:
            self.verify_score = m.get('VerifyScore')

        return self

