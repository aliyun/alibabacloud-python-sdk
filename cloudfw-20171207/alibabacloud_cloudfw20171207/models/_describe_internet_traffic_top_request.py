# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetTrafficTopRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        direction: str = None,
        end_time: str = None,
        lang: str = None,
        limit: str = None,
        rule_result: str = None,
        rule_source: str = None,
        show_country_name: str = None,
        sort: str = None,
        source_code: str = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The type of traffic data.
        # 
        # This parameter is required.
        self.data_type = data_type
        # The traffic direction.
        self.direction = direction
        # The end time. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the response.
        self.lang = lang
        # The maximum number of top entries to return. The default value is 50. Valid values: 1 to 50.
        self.limit = limit
        # The action of the rule.
        self.rule_result = rule_result
        # The source of the rule.
        self.rule_source = rule_source
        # The name of the country to display.
        self.show_country_name = show_country_name
        # The sorting method.
        self.sort = sort
        # The tracing code for the source.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The source IP address.
        self.source_ip = source_ip
        # The start time. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        if self.show_country_name is not None:
            result['ShowCountryName'] = self.show_country_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        if m.get('ShowCountryName') is not None:
            self.show_country_name = m.get('ShowCountryName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

