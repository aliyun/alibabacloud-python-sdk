# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class TextCorrectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TextCorrectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response code. Returns "success" during normal calls.
        self.code = code
        # Intelligent error correction result data.
        self.data = data
        # Error message. Returns "Success" during normal calls. Returns specific error information during exceptions, such as "The parameters contain sensitive information. Please try a different input."
        self.message = message
        # Request ID, used to identify a unique request call.
        self.request_id = request_id
        # Whether the call was successful. true indicates success, false indicates failure.
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
            temp_model = main_models.TextCorrectResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TextCorrectResponseBodyData(DaraModel):
    def __init__(
        self,
        corrected_text: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The corrected text.
        self.corrected_text = corrected_text
        # Usage information, including the number of input characters.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corrected_text is not None:
            result['CorrectedText'] = self.corrected_text

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorrectedText') is not None:
            self.corrected_text = m.get('CorrectedText')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

