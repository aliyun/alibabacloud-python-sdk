# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddCustomLineRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        ip_segment: List[main_models.AddCustomLineRequestIpSegment] = None,
        lang: str = None,
        line_name: str = None,
    ):
        # The domain name. You can call the [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The CIDR blocks.
        # 
        # This parameter is required.
        self.ip_segment = ip_segment
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the custom line.
        # 
        # This parameter is required.
        self.line_name = line_name

    def validate(self):
        if self.ip_segment:
            for v1 in self.ip_segment:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        result['IpSegment'] = []
        if self.ip_segment is not None:
            for k1 in self.ip_segment:
                result['IpSegment'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.ip_segment = []
        if m.get('IpSegment') is not None:
            for k1 in m.get('IpSegment'):
                temp_model = main_models.AddCustomLineRequestIpSegment()
                self.ip_segment.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self



class AddCustomLineRequestIpSegment(DaraModel):
    def __init__(
        self,
        end_ip: str = None,
        start_ip: str = None,
    ):
        # The end IP address of the CIDR block.
        self.end_ip = end_ip
        # The start IP address of the CIDR block.
        self.start_ip = start_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip

        if self.start_ip is not None:
            result['StartIp'] = self.start_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')

        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')

        return self

