# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class CredentialRecognitionIntlV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CredentialRecognitionIntlV2ResponseBodyResult = None,
    ):
        # The return code. A value of 200 indicates a successful request. Other values indicate failures.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The response result.
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
            temp_model = main_models.CredentialRecognitionIntlV2ResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CredentialRecognitionIntlV2ResponseBodyResult(DaraModel):
    def __init__(
        self,
        ext_id_info: str = None,
        sub_code: str = None,
        success: str = None,
    ):
        # The recognized key information, in JSON format.
        self.ext_id_info = ext_id_info
        # The result code. Valid values:
        # 
        # - 200: OCR extraction succeeded and all rule checks passed.
        # - 204: Validation result is inconsistent. OCR extraction succeeded, but some fields in CheckRuleConfig did not pass (N).
        # - 211: Quality does not meet requirements. Quality detection did not pass when idQuality is set to Y (not yet supported in the current version).
        # - 212: Anti-forgery check did not pass. fraudCheck was triggered and anti-forgery verification failed.
        # - 213: No text was extracted, or the credential type check did not pass.
        self.sub_code = sub_code
        # The extraction result. Valid values:
        # - S: Succeeded.
        # - F: Failed.
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

