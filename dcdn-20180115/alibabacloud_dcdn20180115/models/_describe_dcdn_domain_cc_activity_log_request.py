# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainCcActivityLogRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        start_time: str = None,
        trigger_object: str = None,
        value: str = None,
    ):
        # The accelerated domain name. You can specify one or more domain names. Separate multiple domain names with commas (,).
        # 
        # If you leave this parameter empty, the data of all domain names is queried.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The page number of the page returned. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **30**.
        self.page_size = page_size
        # The name of the defense rule.
        # 
        # *   default_normal in normal mode
        # *   default_attack in emergency mode
        # *   A custom rule name in custom mode. Example: test2.
        # 
        # If you leave this parameter empty, events that triggered rate limiting based on all rules are queried.
        self.rule_name = rule_name
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The resolution of the queried data is 5 minutes.
        # 
        # If you leave this parameter empty, the data collected over the last 24 hours is queried.
        self.start_time = start_time
        # The trigger of rate limiting by which you want to query data.
        # 
        # If you leave this parameter empty, all events that triggered rate limiting are queried.
        self.trigger_object = trigger_object
        # The value of the object that triggered rate limiting.
        # 
        # If you leave this parameter empty, events that triggered rate limiting based on all rules are queried.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

