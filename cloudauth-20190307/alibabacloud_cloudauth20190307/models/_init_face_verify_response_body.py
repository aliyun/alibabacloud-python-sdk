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
        # Return code: 200 indicates success, other values indicate failure.
        self.code = code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object.
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
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # URL for real-person authentication in a Web browser, which will redirect according to the ReturnUrl parameter after authentication.
        # 
        # >Notice: 
        # 
        # - The CertifyUrl returned by the initialization interface is valid for **30 minutes and can only be used once**. Please use it within the validity period to avoid reuse.
        # - This parameter requires the correct input of **MetaInfo** to return a CertifyUrl that matches the client. If you cannot obtain it, please check whether **MetaInfo** and other input parameters are correct.
        # 
        # - The domain name of this URL may change with service updates. To ensure normal service availability, it is recommended not to apply access control to this domain name.
        # 
        # - When redirecting in the browser, try not to use incognito mode or modify the URL, as this may result in a **signature error**.
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

