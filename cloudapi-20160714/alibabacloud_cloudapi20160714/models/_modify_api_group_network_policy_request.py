# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApiGroupNetworkPolicyRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        https_policy: str = None,
        inner_domain_enable: bool = None,
        internet_enable: bool = None,
        internet_ipv6enable: bool = None,
        security_token: str = None,
        vpc_intranet_enable: bool = None,
        vpc_slb_intranet_enable: bool = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The HTTPS security policy.
        self.https_policy = https_policy
        # Specifies whether to disable the public second-level domain name.
        self.inner_domain_enable = inner_domain_enable
        # Specifies whether to enable the virtual private cloud (VPC) second-level domain name.
        self.internet_enable = internet_enable
        # Specifies whether to enable IPv6. Valid values: **true** and **false**.
        self.internet_ipv6enable = internet_ipv6enable
        self.security_token = security_token
        # Specifies whether to enable the VPC domain name. Valid values:
        # 
        # *   TRUE
        # *   FALSE
        self.vpc_intranet_enable = vpc_intranet_enable
        # Specifies whether to enable the self-calling domain name.
        self.vpc_slb_intranet_enable = vpc_slb_intranet_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy

        if self.inner_domain_enable is not None:
            result['InnerDomainEnable'] = self.inner_domain_enable

        if self.internet_enable is not None:
            result['InternetEnable'] = self.internet_enable

        if self.internet_ipv6enable is not None:
            result['InternetIPV6Enable'] = self.internet_ipv6enable

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.vpc_intranet_enable is not None:
            result['VpcIntranetEnable'] = self.vpc_intranet_enable

        if self.vpc_slb_intranet_enable is not None:
            result['VpcSlbIntranetEnable'] = self.vpc_slb_intranet_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')

        if m.get('InnerDomainEnable') is not None:
            self.inner_domain_enable = m.get('InnerDomainEnable')

        if m.get('InternetEnable') is not None:
            self.internet_enable = m.get('InternetEnable')

        if m.get('InternetIPV6Enable') is not None:
            self.internet_ipv6enable = m.get('InternetIPV6Enable')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VpcIntranetEnable') is not None:
            self.vpc_intranet_enable = m.get('VpcIntranetEnable')

        if m.get('VpcSlbIntranetEnable') is not None:
            self.vpc_slb_intranet_enable = m.get('VpcSlbIntranetEnable')

        return self

