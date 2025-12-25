# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeWafSourceIpSegmentResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        waf_source_ip: main_models.DescribeWafSourceIpSegmentResponseBodyWafSourceIp = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The back-to-origin CIDR blocks that are used by the protection cluster.
        self.waf_source_ip = waf_source_ip

    def validate(self):
        if self.waf_source_ip:
            self.waf_source_ip.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.waf_source_ip is not None:
            result['WafSourceIp'] = self.waf_source_ip.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WafSourceIp') is not None:
            temp_model = main_models.DescribeWafSourceIpSegmentResponseBodyWafSourceIp()
            self.waf_source_ip = temp_model.from_map(m.get('WafSourceIp'))

        return self

class DescribeWafSourceIpSegmentResponseBodyWafSourceIp(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
        ipv_6: List[str] = None,
    ):
        # An array of back-to-origin IPv4 CIDR blocks.
        self.ipv_4 = ipv_4
        # An array of back-to-origin IPv6 CIDR blocks.
        self.ipv_6 = ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['IPv4'] = self.ipv_4

        if self.ipv_6 is not None:
            result['IPv6'] = self.ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4') is not None:
            self.ipv_4 = m.get('IPv4')

        if m.get('IPv6') is not None:
            self.ipv_6 = m.get('IPv6')

        return self

