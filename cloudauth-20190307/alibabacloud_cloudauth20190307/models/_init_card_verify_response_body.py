# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class InitCardVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.InitCardVerifyResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        # Important
        # - This parameter indicates whether the interface was called correctly. For detailed return code descriptions, see the error codes.
        # - Business results should be viewed through the fields in ResultObject.
        self.code = code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return result.
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
            temp_model = main_models.InitCardVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class InitCardVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        # Verification request ID, a unique identifier for the verification service\\"s authentication request.
        # - When querying the authentication result, the authentication request ID must be provided.
        # 
        # - The CertifyId field is a billing statistics field. To facilitate subsequent bill reconciliation, please retain this field information locally. The CertifyId returned by the initialization interface is valid for 30 minutes and can only be submitted once for authentication. Please apply it within the validity period to avoid reuse.
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        return self

