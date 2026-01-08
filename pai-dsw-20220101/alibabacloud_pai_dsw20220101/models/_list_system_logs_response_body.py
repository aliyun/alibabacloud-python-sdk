# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class ListSystemLogsResponseBody(DaraModel):
    def __init__(
        self,
        offset: str = None,
        system_logs: List[main_models.ListSystemLogsResponseBodySystemLogs] = None,
    ):
        self.offset = offset
        self.system_logs = system_logs

    def validate(self):
        if self.system_logs:
            for v1 in self.system_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        result['SystemLogs'] = []
        if self.system_logs is not None:
            for k1 in self.system_logs:
                result['SystemLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        self.system_logs = []
        if m.get('SystemLogs') is not None:
            for k1 in m.get('SystemLogs'):
                temp_model = main_models.ListSystemLogsResponseBodySystemLogs()
                self.system_logs.append(temp_model.from_map(k1))

        return self

class ListSystemLogsResponseBodySystemLogs(DaraModel):
    def __init__(
        self,
        content: str = None,
        gmt_create_time: str = None,
        level: str = None,
    ):
        self.content = content
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

