# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class LanguageDetectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.LanguageDetectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of 200 indicates success. For other response codes, refer to the error code documentation.
        self.code = code
        # The language detection result data, including the detected language and usage information.
        self.data = data
        # The error message. Returns "Success" for successful calls. Returns a specific error message for failed calls, such as "The parameters contain sensitive information. Try other input.".
        self.message = message
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: Successful.
        # - false: Failed.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.LanguageDetectResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class LanguageDetectResponseBodyData(DaraModel):
    def __init__(
        self,
        detected_language: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The detected language code.
        self.detected_language = detected_language
        # The usage information, including the number of input characters.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detected_language is not None:
            result['DetectedLanguage'] = self.detected_language

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetectedLanguage') is not None:
            self.detected_language = m.get('DetectedLanguage')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

