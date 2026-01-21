# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertHistoryListRequest(DaraModel):
    def __init__(
        self,
        ascending: bool = None,
        end_time: str = None,
        group_id: str = None,
        metric_name: str = None,
        namespace: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        start_time: str = None,
        state: str = None,
        status: str = None,
    ):
        # The order of alerts. Valid values:
        # 
        # *   true (default value): reverse chronological order
        # *   false: chronological order
        self.ascending = ascending
        # The end timestamp of the historical alerts that you want to query.
        # 
        # Unit: milliseconds.
        self.end_time = end_time
        # The ID of the application group.
        # 
        # For information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.group_id = group_id
        # The metric that is used to monitor the cloud service.
        # 
        # For information about how to query the name of a metric, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # For information about how to query the namespace of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The number of the page to return.
        # 
        # Default value: 1.
        self.page = page
        # The number of entries to return on each page.
        # 
        # Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the alert rule.
        # 
        # For information about how to obtain the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.rule_id = rule_id
        # The name of the alert rule.
        # 
        # For information about how to query the name of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.rule_name = rule_name
        # The start timestamp of the historical alerts that you want to query.
        # 
        # Unit: milliseconds.
        self.start_time = start_time
        # The status of the alert. Valid values:
        # 
        # *   ALARM (default value): Alerts are triggered.
        # *   OK: No alerts are triggered.
        self.state = state
        # Specifies whether alerts are muted. Valid values:
        # 
        # *   2 (default value): Alerts are muted and are not triggered within the mute period, even if the condition specified in the alert rule is met.
        # *   0: Alerts are triggered or cleared.
        # *   1: The alert rule is ineffective.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascending is not None:
            result['Ascending'] = self.ascending

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ascending') is not None:
            self.ascending = m.get('Ascending')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

