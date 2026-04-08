# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class LoggingConfiguration(DaraModel):
    def __init__(
        self,
        destinations: List[main_models.LogDestination] = None,
    ):
        # 日志输出的目标配置列表
        self.destinations = destinations

    def validate(self):
        if self.destinations:
            for v1 in self.destinations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['destinations'] = []
        if self.destinations is not None:
            for k1 in self.destinations:
                result['destinations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('destinations') is not None:
            for k1 in m.get('destinations'):
                temp_model = main_models.LogDestination()
                self.destinations.append(temp_model.from_map(k1))

        return self

