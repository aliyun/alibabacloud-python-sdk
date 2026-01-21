# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricRuleListRequest(DaraModel):
    def __init__(
        self,
        alert_state: str = None,
        dimensions: str = None,
        enable_state: bool = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        rule_ids: str = None,
        rule_name: str = None,
    ):
        # The status of the alert rule. Valid values:
        # 
        # *   OK: The alert rule has no active alerts.
        # *   ALARM: The alert rule has active alerts.
        # *   INSUFFICIENT_DATA: No data is available.
        self.alert_state = alert_state
        # The monitoring dimensions of the specified resource.
        # 
        # Set the value to a collection of `key:value` pairs. Example: `{"userId":"120886317861****"}` or `{"instanceId":"i-2ze2d6j5uhg20x47****"}`.
        self.dimensions = dimensions
        # Specifies whether to query enabled or disabled alert rules. Valid values:
        # 
        # *   true: queries enabled alert rules.
        # *   false: queries disabled alert rules.
        self.enable_state = enable_state
        # The ID of the application group.
        # 
        # For information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.group_id = group_id
        # The name of the metric.
        # 
        # For information about how to obtain the name of a metric, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For information about how to obtain the namespace of a cloud service, see [DescribeMetricMetaList](https://help.aliyun.com/document_detail/98846.html) or [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The page number of the page to return.
        # 
        # Minimum value: 1. Default value: 1.
        self.page = page
        # The number of entries to return on each page.
        # 
        # Minimum value: 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the alert rule. You can specify up to 20 IDs at a time. Separate multiple IDs with commas (,).
        self.rule_ids = rule_ids
        # The name of the alert rule.
        # 
        # This parameter supports fuzzy match.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.enable_state is not None:
            result['EnableState'] = self.enable_state

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

