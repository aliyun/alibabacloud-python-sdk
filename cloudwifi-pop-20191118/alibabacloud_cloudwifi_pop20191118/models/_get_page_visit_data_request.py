# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPageVisitDataRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        end_time: str = None,
        pid: str = None,
        start_time: str = None,
    ):
        # appCode
        self.app_code = app_code
        # appName
        self.app_name = app_name
        # endTime
        self.end_time = end_time
        # pId
        self.pid = pid
        # startTime
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.pid is not None:
            result['PId'] = self.pid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PId') is not None:
            self.pid = m.get('PId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

