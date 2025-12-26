# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class CredentialRecognitionIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CredentialRecognitionIntlResponseBodyResult = None,
    ):
        # Return code.
        self.code = code
        # Response message for the returned information.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Returned result.
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
            temp_model = main_models.CredentialRecognitionIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CredentialRecognitionIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_id_info: str = None,
        sub_code: str = None,
        success: str = None,
    ):
        # Identified key information in JSON format.
        self.ext_id_info = ext_id_info
        # Authentication result description
        self.sub_code = sub_code
        # Extraction result. Values:
        # - S: Success.
        # - F: Failure.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_id_info is not None:
            result['ExtIdInfo'] = self.ext_id_info

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtIdInfo') is not None:
            self.ext_id_info = m.get('ExtIdInfo')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

