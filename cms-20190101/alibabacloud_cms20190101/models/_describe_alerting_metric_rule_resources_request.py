# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertingMetricRuleResourcesRequest(DaraModel):
    def __init__(
        self,
        alert_before_time: str = None,
        dimensions: str = None,
        group_id: str = None,
        namespace: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        # Queries the alerts that were triggered before the specified time. Timestamps in milliseconds are supported.
        self.alert_before_time = alert_before_time
        # The dimensions that specify the resources whose monitoring data you want to query.
        self.dimensions = dimensions
        # The ID of the application group. For information about how to obtain the ID of an application group, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.group_id = group_id
        # The namespace of the cloud service.
        # 
        # For more information about the namespaces of cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The page number.
        # 
        # Default value: 1.
        self.page = page
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the alert rule. For information about how to obtain the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_before_time is not None:
            result['AlertBeforeTime'] = self.alert_before_time

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.group_id is not None:
            result['GroupId'] = self.group_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertBeforeTime') is not None:
            self.alert_before_time = m.get('AlertBeforeTime')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

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

        return self

