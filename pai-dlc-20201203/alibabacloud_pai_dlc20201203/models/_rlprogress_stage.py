# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressStage(DaraModel):
    def __init__(
        self,
        duration: float = None,
        end_time: int = None,
        key: str = None,
        label: str = None,
        marker: str = None,
        optional: bool = None,
        start_time: int = None,
        status: str = None,
    ):
        # 阶段耗时（秒，保留 3 位小数）；一个 step 常整体落在同一秒内，故不取整
        self.duration = duration
        # 阶段结束时间（unix 秒）
        self.end_time = end_time
        # 阶段标识
        self.key = key
        # 阶段中文名
        self.label = label
        # 匹配该阶段的日志标记文案
        self.marker = marker
        # 是否为可选阶段；可选阶段未出现时状态记为 skipped
        self.optional = optional
        # 阶段开始时间（unix 秒）
        self.start_time = start_time
        # done / running / waiting / pending / skipped
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

