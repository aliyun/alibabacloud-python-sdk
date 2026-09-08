# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLProgressRollout(DaraModel):
    def __init__(
        self,
        finished: int = None,
        processed: main_models.RLProgressProcessed = None,
        rate_per_min: float = None,
    ):
        # 窗口内完成总数
        self.finished = finished
        # rollout 已处理计数
        self.processed = processed
        # 完成速率（条/分钟），由最近 120 条完成事件估算
        self.rate_per_min = rate_per_min

    def validate(self):
        if self.processed:
            self.processed.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finished is not None:
            result['Finished'] = self.finished

        if self.processed is not None:
            result['Processed'] = self.processed.to_map()

        if self.rate_per_min is not None:
            result['RatePerMin'] = self.rate_per_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Processed') is not None:
            temp_model = main_models.RLProgressProcessed()
            self.processed = temp_model.from_map(m.get('Processed'))

        if m.get('RatePerMin') is not None:
            self.rate_per_min = m.get('RatePerMin')

        return self

