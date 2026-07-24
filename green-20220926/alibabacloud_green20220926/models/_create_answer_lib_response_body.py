# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class CreateAnswerLibResponseBody(DaraModel):
    def __init__(
        self,
        lib_id: str = None,
        request_id: str = None,
        result: main_models.CreateAnswerLibResponseBodyResult = None,
        task_id: str = None,
    ):
        # The ID of the proxy answer library.
        self.lib_id = lib_id
        # The ID assigned by the backend to uniquely identify the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The result.
        self.result = result
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CreateAnswerLibResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class CreateAnswerLibResponseBodyResult(DaraModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_samples: List[str] = None,
        invalid_count: int = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_samples: List[str] = None,
        success_count: int = None,
        task_id: str = None,
        total_count: int = None,
    ):
        # The internationalization key.
        self.i_18n_key = i_18n_key
        # The list of invalid proxy answers.
        self.illegal_length_samples = illegal_length_samples
        # The number of invalid samples.
        self.invalid_count = invalid_count
        # The ID of the proxy answer library.
        self.lib_id = lib_id
        # The task progress percentage.
        self.progress = progress
        # The number of duplicate samples.
        self.repeat_count = repeat_count
        # The list of duplicate proxy answers.
        self.repeat_samples = repeat_samples
        # The number of successful samples.
        self.success_count = success_count
        # The task ID.
        self.task_id = task_id
        # The total count.
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

        if self.illegal_length_samples is not None:
            result['IllegalLengthSamples'] = self.illegal_length_samples

        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count

        if self.repeat_samples is not None:
            result['RepeatSamples'] = self.repeat_samples

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')

        if m.get('IllegalLengthSamples') is not None:
            self.illegal_length_samples = m.get('IllegalLengthSamples')

        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('RepeatSamples') is not None:
            self.repeat_samples = m.get('RepeatSamples')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

