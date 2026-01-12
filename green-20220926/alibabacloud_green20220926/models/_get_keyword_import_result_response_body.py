# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetKeywordImportResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetKeywordImportResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code.
        self.code = code
        # Returned data.
        self.data = data
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request, which can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
            temp_model = main_models.GetKeywordImportResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKeywordImportResultResponseBodyData(DaraModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_keywords: List[str] = None,
        invalid_count: int = None,
        invalid_keywords: List[str] = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_keywords: List[str] = None,
        success_count: int = None,
        tips: str = None,
        total_count: int = None,
    ):
        # Internationalization key.
        self.i_18n_key = i_18n_key
        # List of keywords with illegal length (too long or too short).
        self.illegal_length_keywords = illegal_length_keywords
        # Invalid count.
        self.invalid_count = invalid_count
        # List of invalid keywords.
        self.invalid_keywords = invalid_keywords
        # Keyword library ID.
        self.lib_id = lib_id
        # Task progress percentage.
        self.progress = progress
        # Repeat count.
        self.repeat_count = repeat_count
        # List of repeated keywords.
        self.repeat_keywords = repeat_keywords
        # Success count.
        self.success_count = success_count
        # Tips message.
        self.tips = tips
        # Total count.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key

        if self.illegal_length_keywords is not None:
            result['IllegalLengthKeywords'] = self.illegal_length_keywords

        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count

        if self.invalid_keywords is not None:
            result['InvalidKeywords'] = self.invalid_keywords

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count

        if self.repeat_keywords is not None:
            result['RepeatKeywords'] = self.repeat_keywords

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')

        if m.get('IllegalLengthKeywords') is not None:
            self.illegal_length_keywords = m.get('IllegalLengthKeywords')

        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')

        if m.get('InvalidKeywords') is not None:
            self.invalid_keywords = m.get('InvalidKeywords')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('RepeatKeywords') is not None:
            self.repeat_keywords = m.get('RepeatKeywords')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

