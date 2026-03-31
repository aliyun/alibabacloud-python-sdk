# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleHitsTopClientIpResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_hits_top_client_ip: List[main_models.DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the top 10 IP addresses from which attacks are initiated.
        self.rule_hits_top_client_ip = rule_hits_top_client_ip

    def validate(self):
        if self.rule_hits_top_client_ip:
            for v1 in self.rule_hits_top_client_ip:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHitsTopClientIp'] = []
        if self.rule_hits_top_client_ip is not None:
            for k1 in self.rule_hits_top_client_ip:
                result['RuleHitsTopClientIp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_hits_top_client_ip = []
        if m.get('RuleHitsTopClientIp') is not None:
            for k1 in m.get('RuleHitsTopClientIp'):
                temp_model = main_models.DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp()
                self.rule_hits_top_client_ip.append(temp_model.from_map(k1))

        return self

class DescribeRuleHitsTopClientIpResponseBodyRuleHitsTopClientIp(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        count: int = None,
    ):
        # The IP address of the service client.
        self.client_ip = client_ip
        # The number of attacks that are initiated from the IP address.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

