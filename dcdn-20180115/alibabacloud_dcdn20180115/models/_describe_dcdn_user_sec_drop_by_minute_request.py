# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserSecDropByMinuteRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        lang: str = None,
        object: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_name: str = None,
        sec_func: str = None,
        start_time: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2006-01-02T15:05:04Z.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The language. Valid values: en and zh. Default value: en
        # 
        # This parameter is required.
        self.lang = lang
        # The object that triggered rate limiting.
        self.object = object
        # The number of the page to return. Pages start from page 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size
        # The rule that was triggered.
        self.rule_name = rule_name
        # The name of the security feature.
        # 
        # This parameter is required.
        self.sec_func = sec_func
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2006-01-02T15:04:04Z.
        self.start_time = start_time

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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object is not None:
            result['Object'] = self.object

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sec_func is not None:
            result['SecFunc'] = self.sec_func

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SecFunc') is not None:
            self.sec_func = m.get('SecFunc')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

