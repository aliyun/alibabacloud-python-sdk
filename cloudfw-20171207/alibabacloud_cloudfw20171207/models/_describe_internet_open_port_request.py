# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetOpenPortRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        end_time: str = None,
        lang: str = None,
        page_size: str = None,
        port: str = None,
        risk_level: str = None,
        service_name: str = None,
        service_name_fuzzy: str = None,
        source_ip: str = None,
        start_time: str = None,
        suggest_level: str = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.port = port
        self.risk_level = risk_level
        self.service_name = service_name
        self.service_name_fuzzy = service_name_fuzzy
        self.source_ip = source_ip
        self.start_time = start_time
        self.suggest_level = suggest_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_name_fuzzy is not None:
            result['ServiceNameFuzzy'] = self.service_name_fuzzy

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.suggest_level is not None:
            result['SuggestLevel'] = self.suggest_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceNameFuzzy') is not None:
            self.service_name_fuzzy = m.get('ServiceNameFuzzy')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SuggestLevel') is not None:
            self.suggest_level = m.get('SuggestLevel')

        return self

