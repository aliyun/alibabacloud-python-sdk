# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseRuleStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistics_infos: List[main_models.DescribeDefenseRuleStatisticsResponseBodyStatisticsInfos] = None,
    ):
        self.request_id = request_id
        self.statistics_infos = statistics_infos

    def validate(self):
        if self.statistics_infos:
            for v1 in self.statistics_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatisticsInfos'] = []
        if self.statistics_infos is not None:
            for k1 in self.statistics_infos:
                result['StatisticsInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.statistics_infos = []
        if m.get('StatisticsInfos') is not None:
            for k1 in m.get('StatisticsInfos'):
                temp_model = main_models.DescribeDefenseRuleStatisticsResponseBodyStatisticsInfos()
                self.statistics_infos.append(temp_model.from_map(k1))

        return self

class DescribeDefenseRuleStatisticsResponseBodyStatisticsInfos(DaraModel):
    def __init__(
        self,
        count: int = None,
        fourth_value: str = None,
        primary_value: str = None,
        secondary_value: str = None,
        third_value: str = None,
    ):
        self.count = count
        self.fourth_value = fourth_value
        self.primary_value = primary_value
        self.secondary_value = secondary_value
        self.third_value = third_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.fourth_value is not None:
            result['FourthValue'] = self.fourth_value

        if self.primary_value is not None:
            result['PrimaryValue'] = self.primary_value

        if self.secondary_value is not None:
            result['SecondaryValue'] = self.secondary_value

        if self.third_value is not None:
            result['ThirdValue'] = self.third_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FourthValue') is not None:
            self.fourth_value = m.get('FourthValue')

        if m.get('PrimaryValue') is not None:
            self.primary_value = m.get('PrimaryValue')

        if m.get('SecondaryValue') is not None:
            self.secondary_value = m.get('SecondaryValue')

        if m.get('ThirdValue') is not None:
            self.third_value = m.get('ThirdValue')

        return self

