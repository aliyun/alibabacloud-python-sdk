# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyNatRateLimitRuleRequest(DaraModel):
    def __init__(
        self,
        bandwidth_limit: str = None,
        client_token: str = None,
        dry_run: str = None,
        nat_gateway_id: str = None,
        region_id: str = None,
        rule_description: str = None,
        rule_id: str = None,
        rule_name: str = None,
        source_cidrs: List[str] = None,
    ):
        # The new bandwidth limit. Unit: Mbit/s.
        self.bandwidth_limit = bandwidth_limit
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without querying the resource status. The system checks whether your AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the resource status is queried.
        self.dry_run = dry_run
        # The ID of the NAT gateway to which the rate limiting rule belongs.
        self.nat_gateway_id = nat_gateway_id
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        self.region_id = region_id
        # The new description of the rate limiting rule.
        self.rule_description = rule_description
        # The ID of the rate limiting rule.
        self.rule_id = rule_id
        # The new name of the rate limiting rule.
        self.rule_name = rule_name
        # The new list of source CIDR blocks for the rate limiting rule.
        self.source_cidrs = source_cidrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_description is not None:
            result['RuleDescription'] = self.rule_description

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.source_cidrs is not None:
            result['SourceCIDRs'] = self.source_cidrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleDescription') is not None:
            self.rule_description = m.get('RuleDescription')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SourceCIDRs') is not None:
            self.source_cidrs = m.get('SourceCIDRs')

        return self

