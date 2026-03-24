# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleAlertMetricInput(DaraModel):
    def __init__(
        self,
        filter_values: List[main_models.AlertRuleAlertMetricInputFilterValue] = None,
        group_id: str = None,
        metric_id: str = None,
        param_values: List[main_models.AlertRuleAlertMetricInputParamValue] = None,
    ):
        # 用户输入的过滤条件列表。指标所支持的参数列表、过滤条件列表可通过ListAlertMetrics进行查询。
        self.filter_values = filter_values
        # 用户所选指标组的key
        self.group_id = group_id
        # 用户所选预定义指标的key
        self.metric_id = metric_id
        # 输入的参数列表。  指标所支持的参数列表、过滤条件列表可通过ListAlertMetrics进行查询。
        self.param_values = param_values

    def validate(self):
        if self.filter_values:
            for v1 in self.filter_values:
                 if v1:
                    v1.validate()
        if self.param_values:
            for v1 in self.param_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['filterValues'] = []
        if self.filter_values is not None:
            for k1 in self.filter_values:
                result['filterValues'].append(k1.to_map() if k1 else None)

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.metric_id is not None:
            result['metricId'] = self.metric_id

        result['paramValues'] = []
        if self.param_values is not None:
            for k1 in self.param_values:
                result['paramValues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_values = []
        if m.get('filterValues') is not None:
            for k1 in m.get('filterValues'):
                temp_model = main_models.AlertRuleAlertMetricInputFilterValue()
                self.filter_values.append(temp_model.from_map(k1))

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('metricId') is not None:
            self.metric_id = m.get('metricId')

        self.param_values = []
        if m.get('paramValues') is not None:
            for k1 in m.get('paramValues'):
                temp_model = main_models.AlertRuleAlertMetricInputParamValue()
                self.param_values.append(temp_model.from_map(k1))

        return self

