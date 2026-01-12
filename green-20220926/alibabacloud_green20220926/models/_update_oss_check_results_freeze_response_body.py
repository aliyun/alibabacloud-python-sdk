# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class UpdateOssCheckResultsFreezeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateOssCheckResultsFreezeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.UpdateOssCheckResultsFreezeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateOssCheckResultsFreezeResponseBodyData(DaraModel):
    def __init__(
        self,
        invalid_count: int = None,
        repeat_count: int = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.invalid_count = invalid_count
        self.repeat_count = repeat_count
        self.success_count = success_count
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

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidCount') is not None:
            self.invalid_count = m.get('InvalidCount')

        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

