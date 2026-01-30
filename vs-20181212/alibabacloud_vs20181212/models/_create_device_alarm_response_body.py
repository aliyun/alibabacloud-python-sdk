# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeviceAlarmResponseBody(DaraModel):
    def __init__(
        self,
        alarm_delay: int = None,
        alarm_id: str = None,
        expire: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.alarm_delay = alarm_delay
        self.alarm_id = alarm_id
        self.expire = expire
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_delay is not None:
            result['AlarmDelay'] = self.alarm_delay

        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmDelay') is not None:
            self.alarm_delay = m.get('AlarmDelay')

        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

