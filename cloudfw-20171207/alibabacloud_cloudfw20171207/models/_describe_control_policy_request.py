# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
    ):
        # The action that Cloud Firewall performs on the traffic. Valid values:
        # 
        # - **accept**: Allow
        # 
        # - **drop**: Deny
        # 
        # - **log**: Monitor
        # 
        # > If you do not set this parameter, all action types are queried.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The number of the page to return.
        # 
        # Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy queries are supported.
        # 
        # > If you do not set this parameter, the descriptions of all policies are queried.
        self.description = description
        # The destination address in the access control policy. Fuzzy queries are supported. The value of this parameter varies based on the value of the \\`DestinationType\\` parameter.
        # 
        # - If \\`DestinationType\\` is \\`net\\`, the value of this parameter is a CIDR block. Example: 10.0.3.0/24.
        # 
        # - If \\`DestinationType\\` is \\`domain\\`, the value of this parameter is a domain name. Example: aliyun.
        # 
        # - If \\`DestinationType\\` is \\`group\\`, the value of this parameter is the name of an address book. Example: db_group.
        # 
        # - If \\`DestinationType\\` is \\`location\\`, the value of this parameter is a region name. For more information about region codes, see AddControlPolicy. Example: \\`["BJ11", "ZB"]\\`.
        # 
        # > If you do not set this parameter, all types of destination addresses are queried.
        self.destination = destination
        # The traffic direction that the access control policy controls. Valid values:
        # 
        # - **in**: Inbound traffic from an external source to an internal destination.
        # 
        # - **out**: Outbound traffic from an internal source to an external destination.
        self.direction = direction
        # The IP version supported. Valid values:
        # 
        # - **4** (default): IPv4 address
        # 
        # - **6**: IPv6 address
        self.ip_version = ip_version
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The protocol type of the traffic in the access control policy. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # - **ANY** (all protocol types)
        # 
        # > If you do not set this parameter, all protocol types are queried.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # - **true**: The access control policy is enabled.
        # 
        # - **false**: The access control policy is disabled.
        self.release = release
        # The recurrence type for the policy validity period of the access control policy. Valid values:
        # 
        # - **Permanent** (default): Always
        # 
        # - **None**: One-time
        # 
        # - **Daily**: Daily
        # 
        # - **Weekly**: Weekly
        # 
        # - **Monthly**: Monthly
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy queries are supported. The value of this parameter varies based on the value of the \\`SourceType\\` parameter.
        # 
        # - If \\`SourceType\\` is \\`net\\`, the value of this parameter is a CIDR block. Example: 192.0.XX.XX/24.
        # 
        # - If \\`SourceType\\` is \\`group\\`, the value of this parameter is the name of a source address book. Example: \\`db_group\\`. If you leave this parameter empty, all source addresses are queried.
        # 
        # - If \\`SourceType\\` is \\`location\\`, the value of this parameter is a source region. Example: \\`Beijing\\` or \\`beijing\\`. You can use either the Chinese name or the English name for the query.
        # 
        # > If you do not set this parameter, all types of source addresses are queried.
        self.source = source

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

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.release is not None:
            result['Release'] = self.release

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.source is not None:
            result['Source'] = self.source

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

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

