# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateCustomLineRequest(DaraModel):
    def __init__(
        self,
        ip_segment: List[main_models.UpdateCustomLineRequestIpSegment] = None,
        lang: str = None,
        line_id: int = None,
        line_name: str = None,
    ):
        # The list of IP ranges. Use a hyphen (-) to separate the start and end IP addresses. Specify one IP segment per line. You can specify 1 to 50 IP ranges. To specify a single IP address, use the format IP1-IP1. The IP ranges cannot overlap.
        self.ip_segment = ip_segment
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The unique ID of the custom line. You can call [DescribeCustomLines](https://help.aliyun.com/document_detail/2355671.html) to obtain this ID.
        # 
        # This parameter is required.
        self.line_id = line_id
        # The name of the custom line. The name must be 1 to 20 characters long and can contain Chinese characters, letters, digits, hyphens (-), and underscores (_).
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
        result['IpSegment'] = []
        if self.ip_segment is not None:
            for k1 in self.ip_segment:
                result['IpSegment'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_segment = []
        if m.get('IpSegment') is not None:
            for k1 in m.get('IpSegment'):
                temp_model = main_models.UpdateCustomLineRequestIpSegment()
                self.ip_segment.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

class UpdateCustomLineRequestIpSegment(DaraModel):
    def __init__(
        self,
        end_ip: str = None,
        start_ip: str = None,
    ):
        # The end IP address of the IP range.
        self.end_ip = end_ip
        # The start IP address of the IP range.
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

