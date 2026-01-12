# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAnswerImportProgressResponseBody(DaraModel):
    def __init__(
        self,
        i_18n_key: str = None,
        illegal_length_samples: List[str] = None,
        invalid_count: int = None,
        lib_id: str = None,
        progress: int = None,
        repeat_count: int = None,
        repeat_samples: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        task_id: str = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.i_18n_key = i_18n_key
        self.illegal_length_samples = illegal_length_samples
        self.invalid_count = invalid_count
        self.lib_id = lib_id
        self.progress = progress
        self.repeat_count = repeat_count
        self.repeat_samples = repeat_samples
        self.request_id = request_id
        self.success_count = success_count
        self.task_id = task_id
        self.tips = tips
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tips is not None:
            result['Tips'] = self.tips

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

