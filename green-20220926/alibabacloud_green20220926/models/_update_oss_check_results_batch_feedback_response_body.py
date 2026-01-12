# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOssCheckResultsBatchFeedbackResponseBody(DaraModel):
    def __init__(
        self,
        invalid_count: int = None,
        repeat_count: int = None,
        request_id: str = None,
        success_count: int = None,
        tips: str = None,
        total_count: int = None,
    ):
        self.invalid_count = invalid_count
        self.repeat_count = repeat_count
        self.request_id = request_id
        self.success_count = success_count
        self.tips = tips
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invalid_count is not None:
            result['InvalidCount'] = self.invalid_count

        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.tips is not None:
            result['Tips'] = self.tips

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

