# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class AddKeywordsToLibResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AddKeywordsToLibResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.AddKeywordsToLibResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddKeywordsToLibResponseBodyData(DaraModel):
    def __init__(
        self,
        keywords_result: main_models.AddKeywordsToLibResponseBodyDataKeywordsResult = None,
        lib_id: str = None,
        task_id: str = None,
    ):
        # Result.
        self.keywords_result = keywords_result
        # The id of the keyword library.
        self.lib_id = lib_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.keywords_result:
            self.keywords_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords_result is not None:
            result['KeywordsResult'] = self.keywords_result.to_map()

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordsResult') is not None:
            temp_model = main_models.AddKeywordsToLibResponseBodyDataKeywordsResult()
            self.keywords_result = temp_model.from_map(m.get('KeywordsResult'))

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class AddKeywordsToLibResponseBodyDataKeywordsResult(DaraModel):
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
        total_count: int = None,
    ):
        # Internationalization key.
        self.i_18n_key = i_18n_key
        # List of keywords that are too long or too short.
        self.illegal_length_keywords = illegal_length_keywords
        # Invalid keyword count.
        self.invalid_count = invalid_count
        # List of invalid keywords
        self.invalid_keywords = invalid_keywords
        # The id of the keyword library.
        self.lib_id = lib_id
        # The progress percentage of the task.
        self.progress = progress
        # Duplicate keyword count
        self.repeat_count = repeat_count
        # List of duplicate keywords
        self.repeat_keywords = repeat_keywords
        # The success count of keywords.
        self.success_count = success_count
        # The total count of keywords.
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

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

