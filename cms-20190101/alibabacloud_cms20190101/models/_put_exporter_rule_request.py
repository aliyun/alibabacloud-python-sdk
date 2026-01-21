# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutExporterRuleRequest(DaraModel):
    def __init__(
        self,
        describe: str = None,
        dst_names: List[str] = None,
        metric_name: str = None,
        namespace: str = None,
        region_id: str = None,
        rule_name: str = None,
        target_windows: str = None,
    ):
        # The description of the data export rule.
        self.describe = describe
        # The destination to which the data is exported. Valid values of N: 1 to 20.
        # 
        # This parameter is required.
        self.dst_names = dst_names
        # The name of the metric.
        # 
        # > 
        # 
        # For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # > For more information, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        self.region_id = region_id
        # The name of the rule.
        # 
        # > If the specified rule exists, the existing rule is modified. Otherwise, a rule is created.
        self.rule_name = rule_name
        # The time window of the exported data. Unit: seconds.
        # 
        # > 
        # 
        # *   Separate multiple time windows with commas (,).
        # 
        # *   Data in a time window of less than 60 seconds cannot be exported.
        self.target_windows = target_windows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe is not None:
            result['Describe'] = self.describe

        if self.dst_names is not None:
            result['DstNames'] = self.dst_names

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.target_windows is not None:
            result['TargetWindows'] = self.target_windows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('DstNames') is not None:
            self.dst_names = m.get('DstNames')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TargetWindows') is not None:
            self.target_windows = m.get('TargetWindows')

        return self

