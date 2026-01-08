# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAclWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        domain_group_use_dns: bool = None,
        nat_domain_group_use_dns: bool = None,
        request_id: str = None,
        support_message_type: bool = None,
        vpc_domain_group_use_dns: bool = None,
    ):
        self.domain_group_use_dns = domain_group_use_dns
        self.nat_domain_group_use_dns = nat_domain_group_use_dns
        self.request_id = request_id
        self.support_message_type = support_message_type
        self.vpc_domain_group_use_dns = vpc_domain_group_use_dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_group_use_dns is not None:
            result['DomainGroupUseDns'] = self.domain_group_use_dns

        if self.nat_domain_group_use_dns is not None:
            result['NatDomainGroupUseDns'] = self.nat_domain_group_use_dns

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_message_type is not None:
            result['SupportMessageType'] = self.support_message_type

        if self.vpc_domain_group_use_dns is not None:
            result['VpcDomainGroupUseDns'] = self.vpc_domain_group_use_dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainGroupUseDns') is not None:
            self.domain_group_use_dns = m.get('DomainGroupUseDns')

        if m.get('NatDomainGroupUseDns') is not None:
            self.nat_domain_group_use_dns = m.get('NatDomainGroupUseDns')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportMessageType') is not None:
            self.support_message_type = m.get('SupportMessageType')

        if m.get('VpcDomainGroupUseDns') is not None:
            self.vpc_domain_group_use_dns = m.get('VpcDomainGroupUseDns')

        return self

