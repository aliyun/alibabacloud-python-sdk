# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseCountStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        defense_count_statistics: main_models.DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics = None,
        request_id: str = None,
    ):
        self.defense_count_statistics = defense_count_statistics
        self.request_id = request_id

    def validate(self):
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountStatistics') is not None:
            temp_model = main_models.DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m.get('DefenseCountStatistics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics(DaraModel):
    def __init__(
        self,
        defense_count_total_usage_of_current_month: int = None,
        flow_pack_count_remain: int = None,
        max_usable_defense_count_current_month: int = None,
    ):
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month
        self.flow_pack_count_remain = flow_pack_count_remain
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month

        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain

        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')

        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')

        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')

        return self

