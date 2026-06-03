# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class GetSmsCodeLimitConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSmsCodeLimitConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSmsCodeLimitConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSmsCodeLimitConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        limit_day: int = None,
        limit_hour: int = None,
        limit_id: int = None,
        limit_minute: int = None,
        limit_other: str = None,
    ):
        self.limit_day = limit_day
        self.limit_hour = limit_hour
        self.limit_id = limit_id
        self.limit_minute = limit_minute
        self.limit_other = limit_other

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_day is not None:
            result['LimitDay'] = self.limit_day

        if self.limit_hour is not None:
            result['LimitHour'] = self.limit_hour

        if self.limit_id is not None:
            result['LimitId'] = self.limit_id

        if self.limit_minute is not None:
            result['LimitMinute'] = self.limit_minute

        if self.limit_other is not None:
            result['LimitOther'] = self.limit_other

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitDay') is not None:
            self.limit_day = m.get('LimitDay')

        if m.get('LimitHour') is not None:
            self.limit_hour = m.get('LimitHour')

        if m.get('LimitId') is not None:
            self.limit_id = m.get('LimitId')

        if m.get('LimitMinute') is not None:
            self.limit_minute = m.get('LimitMinute')

        if m.get('LimitOther') is not None:
            self.limit_other = m.get('LimitOther')

        return self

