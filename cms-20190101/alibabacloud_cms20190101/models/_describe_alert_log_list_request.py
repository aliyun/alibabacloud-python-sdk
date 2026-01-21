# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertLogListRequest(DaraModel):
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
        # The end timestamp of the alert logs to be queried.
        # 
        # Unit: milliseconds.
        # 
        # You can query only the alert logs within the last year. If the query time is longer than one year, the return value of the `AlertLogList` parameter is empty.
        # 
        # >  The time period between the start time specified by `StartTime` and end time specified by `EndTime` must be less than or equal to 15 days. You must specify StartTime and EndTime at the same time, or leave StartTime and EndTime empty at the same time. If you do not specify this parameter, the alert logs within the last 15 minutes are queried by default.
        self.end_time = end_time
        # The type of the alert event. Valid values:
        # 
        # *   TRIGGERED: The alert is triggered.
        # *   RESOLVED: The alert is resolved.
        self.event_type = event_type
        # The dimensions based on which data is aggregated. This parameter is equivalent to the GROUP BY clause in SQL. Valid values:
        # 
        # *   `product`: aggregates data by cloud service.
        # *   `level`: aggregates data by alert level.
        # *   `groupId`: aggregates data by application group.
        # *   `contactGroup`: aggregates data by alert contact group.
        # *   `product,metricName`: aggregates data both by cloud service and by metric.
        self.group_by = group_by
        # The ID of the application group.
        self.group_id = group_id
        # The statistical period of alert logs. Unit: minutes.
        self.last_min = last_min
        # The severity level and notification methods of the alert. Valid values:
        # 
        # *   P4: Alert notifications are sent by using emails and DingTalk chatbots.
        # *   OK: No alert is generated.
        self.level = level
        # The metric name.
        # 
        # > For more information about the metrics of different cloud services, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # >  For information about how to query the namespace of a cloud service, see [Appendix 1: Metrics](https://help.aliyun.com/document_detail/163515.html).
        self.namespace = namespace
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The abbreviation of the service name.
        # 
        # For information about how to obtain the abbreviation of a cloud service name, see [DescribeProductsOfActiveMetricRule](https://help.aliyun.com/document_detail/114930.html).
        self.product = product
        self.region_id = region_id
        # The ID of the alert rule.
        # 
        # For information about how to obtain the ID of an alert rule, see [DescribeMetricRuleList](https://help.aliyun.com/document_detail/114941.html).
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The search keyword that is used to query alert logs.
        self.search_key = search_key
        # The status of the alert. Valid values:
        # 
        # *   0: The alert is triggered or cleared.
        # *   1: The alert is ineffective.
        # *   2: The alert is muted.
        # *   3: The host is restarting.
        # *   4: No alert notification is sent.
        # 
        # If the value of the SendStatus parameter is 0, the value P4 of the Level parameter indicates a triggered alert and the value OK indicates a cleared alert.
        self.send_status = send_status
        # The type of the alert rule. Valid value: METRIC. This value indicates an alert rule for time series metrics.
        self.source_type = source_type
        # The start timestamp of the alert logs to be queried.
        # 
        # Unit: milliseconds.
        # 
        # You can query only the alert logs within the last year. If the query time is longer than one year, the return value of the `AlertLogList` parameter is empty.
        # 
        # >  The time period between the start time specified by `StartTime` and the end time specified by `EndTime` must be less than or equal to 15 days. You must specify StartTime and EndTime at the same time, or leave StartTime and EndTime empty at the same time. If you do not specify this parameter, the alert logs within the last 15 minutes are queried by default.
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

