# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertLogHistogramRequest(DaraModel):
    def __init__(
        self,
        contact_group: str = None,
        end_time: int = None,
        event_type: str = None,
        group_by: str = None,
        group_id: str = None,
        last_min: str = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        product: str = None,
        region_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        search_key: str = None,
        send_status: str = None,
        source_type: str = None,
        start_time: int = None,
    ):
        # The alert contact group.
        self.contact_group = contact_group
        # The end timestamp for querying alert history.
        # 
        # Unit: milliseconds.
        # 
        # > - You can query only the alert history within the last year.
        # > - The interval between the start time (StartTime) and end time (EndTime) must be less than or equal to 15 days.
        self.end_time = end_time
        # The alert type. Valid values:
        # 
        # - TRIGGERED: The alert is triggered.
        # - RESOLVED: The alert recovers.
        self.event_type = event_type
        # Aggregates data by spatial dimension, equivalent to Group By in SQL. Valid values:
        # - `product`: aggregates by Alibaba Cloud service.
        # - `level`: aggregates by alert level.
        # - `groupId`: aggregates by application group.
        # - `contactGroup`: aggregates by alert contact group.
        # - `product,metricName`: aggregates by Alibaba Cloud service and metric.
        self.group_by = group_by
        # The application group ID.
        self.group_id = group_id
        # The period for obtaining logs. Unit: minutes.
        self.last_min = last_min
        # The alert level and notification method. Valid values:
        # 
        # <props="china">- P2: phone call + text message + email + DingTalk chatbot.
        # 
        # <props="china">- P3: text message + email + DingTalk chatbot.
        # 
        # <props="china">- P4: email + DingTalk chatbot.
        # 
        # <props="china">- OK: no alert.
        # 
        # <props="intl">- P4: email + DingTalk chatbot.
        # 
        # <props="intl">- OK: no alert.
        # 
        # <props="partner">- P4: email + DingTalk chatbot.
        # 
        # <props="partner">- OK: no alert.
        self.level = level
        # The metric name.
        # 
        # > For information about the metrics of Alibaba Cloud services, see [Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the Alibaba Cloud service.
        # 
        # > For information about the namespaces of Alibaba Cloud services, see [Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The abbreviation of the Alibaba Cloud service name.
        self.product = product
        self.region_id = region_id
        # The alert rule ID.
        # 
        # 
        # For information about how to obtain the alert rule ID, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.rule_id = rule_id
        # The alert rule name.
        self.rule_name = rule_name
        # The keyword for searching alert history.
        self.search_key = search_key
        # The alert status. Valid values:
        # - 0: An alert is triggered or the alert recovers to Normal.
        # - 1: The alert is not in the effective period.
        # - 2: The mute for epoch.
        # - 3: The host is restarting.
        # - 4: Alerts are not send.
        # 
        # <props="china">When the alert status is 0, if the value of Level is P2, P3, or P4, an alert is triggered. If the value of Level is OK, the alert recovers to Normal.
        # <props="intl">When the alert status is 0, if the value of Level is P4, an alert is triggered. If the value of Level is OK, the alert recovers to Normal.
        # <props="partner">When the alert status is 0, if the value of Level is P4, an alert is triggered. If the value of Level is OK, the alert recovers to Normal.
        self.send_status = send_status
        # **[Deprecated]** This parameter is deprecated and does not need to be specified.
        self.source_type = source_type
        # The start timestamp for querying alert history.
        # 
        # Unit: milliseconds.
        # 
        # > - You can query only the alert history within the last year.
        # > - The interval between the start time (StartTime) and end time (EndTime) must be less than or equal to 15 days.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.last_min is not None:
            result['LastMin'] = self.last_min

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.send_status is not None:
            result['SendStatus'] = self.send_status

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LastMin') is not None:
            self.last_min = m.get('LastMin')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

