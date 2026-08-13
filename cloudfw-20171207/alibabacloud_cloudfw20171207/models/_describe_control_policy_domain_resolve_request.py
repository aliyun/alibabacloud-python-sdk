# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeControlPolicyDomainResolveRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        firewall_type: str = None,
        ip_version: int = None,
        lang: str = None,
        region_no: str = None,
    ):
        # The domain name. This parameter is required and must be specified when you call this operation.
        self.domain = domain
        # The type of the cloud firewall.
        self.firewall_type = firewall_type
        # The IP address version. Valid values: **4** (IPv4) and **6** (IPv6).
        # 
        # > This parameter is unconditionally required and has no dependency on RegionNo. If this parameter is not specified, the error MissingParameter.IpVersion is returned (-200157). If the value is invalid, the error ErrorParameterIpVersion is returned (-200135).
        self.ip_version = ip_version
        # The language type.
        self.lang = lang
        # The region ID. This parameter is required. If this parameter is not specified, the error MissingParameter.RegionNo is returned (-200155, The required parameter \\"RegionNo\\" is not provided.).
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

