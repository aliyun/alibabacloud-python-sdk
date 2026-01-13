# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadApiCallDailyDetailCmd(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        end_time: str = None,
        engine_type: str = None,
        start_time: str = None,
    ):
        self.api_name = api_name
        self.end_time = end_time
        self.engine_type = engine_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

