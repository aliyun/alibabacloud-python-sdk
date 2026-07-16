# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class InitFaceVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.InitFaceVerifyResponseBodyResultObject = None,
    ):
        # The response code. 200 indicates success. Other values indicate failure.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The result object.
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
            temp_model = main_models.InitFaceVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class InitFaceVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        certify_url: str = None,
    ):
        # The unique identifier for ID Verification.
        self.certify_id = certify_id
        # The URL for performing ID Verification in a web browser. After authentication is complete, the page redirects based on the ReturnUrl parameter.
        # 
        # >Notice: 
        # 
        # - The CertifyUrl returned by the initialization operation is **valid for 30 minutes and can be submitted for authentication only once**. Use it within the validity period and do not reuse it.
        # - This parameter requires the **MetaInfo** parameter to be correctly passed in to return a CertifyUrl that matches the client. If the URL cannot be obtained, check whether **MetaInfo** and other input parameters are correct.
        # 
        # - The domain name of this URL may change with service updates. To ensure normal service availability, do not apply access control to this domain name.
        # 
        # - Do not use incognito mode or modify the URL during browser redirection. Otherwise, a **signature exception** error may occur.
        # 
        # .
        self.certify_url = certify_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.certify_url is not None:
            result['CertifyUrl'] = self.certify_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('CertifyUrl') is not None:
            self.certify_url = m.get('CertifyUrl')

        return self

