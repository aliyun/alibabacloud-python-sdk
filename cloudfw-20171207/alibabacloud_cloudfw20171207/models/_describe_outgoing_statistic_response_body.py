# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingStatisticResponseBody(DaraModel):
    def __init__(
        self,
        ignore_asset_count: int = None,
        ignore_domain_count: int = None,
        ignore_dst_ipcount: int = None,
        private_risk_asset_count: int = None,
        private_total_asset_count: int = None,
        request_id: str = None,
        risk_asset_count: int = None,
        risk_domain_count: int = None,
        risk_dst_ipcount: int = None,
        subscribe_asset_count: int = None,
        subscribe_domain_count: int = None,
        subscribe_dst_ipcount: int = None,
        total_asset_count: int = None,
        total_domain_count: int = None,
        total_dst_ipcount: int = None,
        total_protocol_count: int = None,
        uncovered_acl_domain: int = None,
        uncovered_acl_dst_ip: int = None,
        unknown_protocol_radio: str = None,
    ):
        self.ignore_asset_count = ignore_asset_count
        self.ignore_domain_count = ignore_domain_count
        self.ignore_dst_ipcount = ignore_dst_ipcount
        self.private_risk_asset_count = private_risk_asset_count
        self.private_total_asset_count = private_total_asset_count
        self.request_id = request_id
        self.risk_asset_count = risk_asset_count
        self.risk_domain_count = risk_domain_count
        self.risk_dst_ipcount = risk_dst_ipcount
        self.subscribe_asset_count = subscribe_asset_count
        self.subscribe_domain_count = subscribe_domain_count
        self.subscribe_dst_ipcount = subscribe_dst_ipcount
        self.total_asset_count = total_asset_count
        self.total_domain_count = total_domain_count
        self.total_dst_ipcount = total_dst_ipcount
        self.total_protocol_count = total_protocol_count
        self.uncovered_acl_domain = uncovered_acl_domain
        self.uncovered_acl_dst_ip = uncovered_acl_dst_ip
        self.unknown_protocol_radio = unknown_protocol_radio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_asset_count is not None:
            result['IgnoreAssetCount'] = self.ignore_asset_count

        if self.ignore_domain_count is not None:
            result['IgnoreDomainCount'] = self.ignore_domain_count

        if self.ignore_dst_ipcount is not None:
            result['IgnoreDstIPCount'] = self.ignore_dst_ipcount

        if self.private_risk_asset_count is not None:
            result['PrivateRiskAssetCount'] = self.private_risk_asset_count

        if self.private_total_asset_count is not None:
            result['PrivateTotalAssetCount'] = self.private_total_asset_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_asset_count is not None:
            result['RiskAssetCount'] = self.risk_asset_count

        if self.risk_domain_count is not None:
            result['RiskDomainCount'] = self.risk_domain_count

        if self.risk_dst_ipcount is not None:
            result['RiskDstIPCount'] = self.risk_dst_ipcount

        if self.subscribe_asset_count is not None:
            result['SubscribeAssetCount'] = self.subscribe_asset_count

        if self.subscribe_domain_count is not None:
            result['SubscribeDomainCount'] = self.subscribe_domain_count

        if self.subscribe_dst_ipcount is not None:
            result['SubscribeDstIPCount'] = self.subscribe_dst_ipcount

        if self.total_asset_count is not None:
            result['TotalAssetCount'] = self.total_asset_count

        if self.total_domain_count is not None:
            result['TotalDomainCount'] = self.total_domain_count

        if self.total_dst_ipcount is not None:
            result['TotalDstIPCount'] = self.total_dst_ipcount

        if self.total_protocol_count is not None:
            result['TotalProtocolCount'] = self.total_protocol_count

        if self.uncovered_acl_domain is not None:
            result['UncoveredAclDomain'] = self.uncovered_acl_domain

        if self.uncovered_acl_dst_ip is not None:
            result['UncoveredAclDstIP'] = self.uncovered_acl_dst_ip

        if self.unknown_protocol_radio is not None:
            result['UnknownProtocolRadio'] = self.unknown_protocol_radio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreAssetCount') is not None:
            self.ignore_asset_count = m.get('IgnoreAssetCount')

        if m.get('IgnoreDomainCount') is not None:
            self.ignore_domain_count = m.get('IgnoreDomainCount')

        if m.get('IgnoreDstIPCount') is not None:
            self.ignore_dst_ipcount = m.get('IgnoreDstIPCount')

        if m.get('PrivateRiskAssetCount') is not None:
            self.private_risk_asset_count = m.get('PrivateRiskAssetCount')

        if m.get('PrivateTotalAssetCount') is not None:
            self.private_total_asset_count = m.get('PrivateTotalAssetCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskAssetCount') is not None:
            self.risk_asset_count = m.get('RiskAssetCount')

        if m.get('RiskDomainCount') is not None:
            self.risk_domain_count = m.get('RiskDomainCount')

        if m.get('RiskDstIPCount') is not None:
            self.risk_dst_ipcount = m.get('RiskDstIPCount')

        if m.get('SubscribeAssetCount') is not None:
            self.subscribe_asset_count = m.get('SubscribeAssetCount')

        if m.get('SubscribeDomainCount') is not None:
            self.subscribe_domain_count = m.get('SubscribeDomainCount')

        if m.get('SubscribeDstIPCount') is not None:
            self.subscribe_dst_ipcount = m.get('SubscribeDstIPCount')

        if m.get('TotalAssetCount') is not None:
            self.total_asset_count = m.get('TotalAssetCount')

        if m.get('TotalDomainCount') is not None:
            self.total_domain_count = m.get('TotalDomainCount')

        if m.get('TotalDstIPCount') is not None:
            self.total_dst_ipcount = m.get('TotalDstIPCount')

        if m.get('TotalProtocolCount') is not None:
            self.total_protocol_count = m.get('TotalProtocolCount')

        if m.get('UncoveredAclDomain') is not None:
            self.uncovered_acl_domain = m.get('UncoveredAclDomain')

        if m.get('UncoveredAclDstIP') is not None:
            self.uncovered_acl_dst_ip = m.get('UncoveredAclDstIP')

        if m.get('UnknownProtocolRadio') is not None:
            self.unknown_protocol_radio = m.get('UnknownProtocolRadio')

        return self

