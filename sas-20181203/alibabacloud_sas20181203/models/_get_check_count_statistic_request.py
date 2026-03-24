# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCheckCountStatisticRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        statistic_type: str = None,
        task_sources: List[str] = None,
        vendors: List[str] = None,
    ):
        # 语言参数
        self.lang = lang
        # The type of the statistics. Valid values:
        # 
        # *   **user**: the top five users that are granted excessive permissions.
        # *   **role**: the top five roles that are granted excessive permissions.
        # *   **instance**: the top five cloud services on which risks are detected.
        # *   **host**: the top five servers on which baseline risks are detected.
        self.statistic_type = statistic_type
        # Task source.
        self.task_sources = task_sources
        # The cloud service providers.
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.statistic_type is not None:
            result['StatisticType'] = self.statistic_type

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('StatisticType') is not None:
            self.statistic_type = m.get('StatisticType')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

