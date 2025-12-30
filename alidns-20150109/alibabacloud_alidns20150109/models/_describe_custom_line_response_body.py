# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomLineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        domain_name: str = None,
        id: int = None,
        ip_segment_list: List[main_models.DescribeCustomLineResponseBodyIpSegmentList] = None,
        name: str = None,
        request_id: str = None,
    ):
        # The code of the custom line.
        self.code = code
        # The domain name.
        self.domain_name = domain_name
        # The ID/Name of the custom line.
        self.id = id
        # The CIDR blocks. Separate IP addresses with a hyphen (-). Enter a CIDR block in each row. You can enter 1 to 50 CIDR blocks at a time. If a CIDR block contains only one IP address, enter the IP address in the format of IP1-IP1. Different CIDR blocks cannot be overlapped.
        self.ip_segment_list = ip_segment_list
        # The name of the custom line.
        self.name = name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ip_segment_list:
            for v1 in self.ip_segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        result['IpSegmentList'] = []
        if self.ip_segment_list is not None:
            for k1 in self.ip_segment_list:
                result['IpSegmentList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.ip_segment_list = []
        if m.get('IpSegmentList') is not None:
            for k1 in m.get('IpSegmentList'):
                temp_model = main_models.DescribeCustomLineResponseBodyIpSegmentList()
                self.ip_segment_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomLineResponseBodyIpSegmentList(DaraModel):
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

