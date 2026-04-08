# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class CreateMmsTimerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateMmsTimerResponseBodyData = None,
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateMmsTimerResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateMmsTimerResponseBodyData(DaraModel):
    def __init__(
        self,
        timer_id: int = None,
    ):
        # timer id
        self.timer_id = timer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timer_id is not None:
            result['timerId'] = self.timer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timerId') is not None:
            self.timer_id = m.get('timerId')

        return self

