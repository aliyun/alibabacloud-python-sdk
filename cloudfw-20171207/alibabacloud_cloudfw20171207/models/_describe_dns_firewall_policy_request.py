# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDnsFirewallPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        ip_version: str = None,
        lang: str = None,
        page_size: str = None,
        release: str = None,
        source: str = None,
        source_ip: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic in the access control policy of the DNS border firewall. Valid values:
        # 
        # - **accept**: Allow
        # - **drop**: Deny
        # - **log**: Monitor
        # 
        # > If you do not specify this parameter, all actions are queried.
        self.acl_action = acl_action
        # The unique ID of the firewall rule.
        self.acl_uuid = acl_uuid
        # The page number of the current page for a paging query. Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The description of the DNS border firewall policy.
        self.description = description
        # The destination address in the access control policy of the DNS border firewall. Fuzzy match is supported.
        # 
        # > Destination can be a single CIDR block, a domain name, or an address book name.
        self.destination = destination
        # The IP address version. Valid values:
        # 
        # - **4**: IPv4
        # - **6**: IPv6
        self.ip_version = ip_version
        # The language of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The number of entries to return in the current query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the access control policy. By default, the policy is enabled after it is created. Valid values:
        # 
        # - **true**: Enabled
        # 
        # - **false**: Disabled
        self.release = release
        # The source address in the access control policy of the DNS border firewall. Fuzzy match is supported.
        # 
        # > Source can be a single CIDR block or an address book name.
        self.source = source
        # The source IP address of the requester.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.release is not None:
            result['Release'] = self.release

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

