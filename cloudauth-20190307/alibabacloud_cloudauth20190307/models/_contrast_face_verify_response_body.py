# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class ContrastFaceVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.ContrastFaceVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Request result
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
            temp_model = main_models.ContrastFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class ContrastFaceVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        identity_info: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        # Unique identifier for the real-person verification request.
        self.certify_id = certify_id
        # Information about the authenticated entity, which is usually empty in general authentication scenarios.
        self.identity_info = identity_info
        # Attachment information of the authenticated entity, mainly image materials, in JSON format, as follows.
        self.material_info = material_info
        # Whether it passed, T for pass, F for fail.
        self.passed = passed
        # Description of the authentication result. For details, see the SubCode explanation below.
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info

        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')

        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

