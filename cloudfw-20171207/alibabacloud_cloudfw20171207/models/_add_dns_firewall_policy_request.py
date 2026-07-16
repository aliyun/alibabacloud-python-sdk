# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDnsFirewallPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        description: str = None,
        destination: str = None,
        destination_type: str = None,
        direction: str = None,
        ip_version: str = None,
        lang: str = None,
        priority: str = None,
        release: str = None,
        source: str = None,
        source_ip: str = None,
        source_type: str = None,
    ):
        # Specifies the action to take on traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: Allows the traffic.
        # 
        # - **drop**: Denies the traffic.
        # 
        # - **log**: Monitors the traffic.
        # 
        # This parameter is required.
        self.acl_action = acl_action
        # The description of the access control policy.
        # 
        # This parameter is required.
        self.description = description
        # The destination address in the access control policy.
        # 
        # - When **DestinationType** is `net`, this parameter specifies the destination CIDR block. Example: `1.2.3.4/24`.
        # 
        # - When **DestinationType** is `group`, this parameter specifies the name of the destination address book. Example: `db_group`.
        # 
        # - When **DestinationType** is `domain`, this parameter specifies the destination domain name. Example: `*.aliyuncs.com`.
        # 
        # - When **DestinationType** is `location`, this parameter specifies the destination region. For more information about location codes, see the documentation. Example: `["BJ11", "ZB"]`.
        # 
        # This parameter is required.
        self.destination = destination
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: destination CIDR block
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The traffic direction for the access control policy. Valid values:
        # 
        # - **in**: inbound traffic
        # 
        # - **out**: outbound traffic
        self.direction = direction
        # The IP version supported by the policy.
        # 
        # Valid values:
        # 
        # - **4**: IPv4
        # 
        # - **6**: IPv6
        # 
        # This parameter is required.
        self.ip_version = ip_version
        # The language of the request and response. Valid values:<br>-**zh**: Chinese<br>-**en**: English<br><br>
        self.lang = lang
        # The priority of the access control policy. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # Specifies whether to enable the access control policy. Valid values:
        # 
        # - **true**: Enables the access control policy.
        # 
        # - **false**: Disables the access control policy.
        # 
        # This parameter is required.
        self.release = release
        # The source address in the access control policy.
        # 
        # - When **SourceType** is `net`, this parameter specifies the source CIDR block. Example: `10.2.XX.XX/24`.
        # 
        # - When **SourceType** is `group`, this parameter specifies the name of the source address book. Example: `db_group`.
        # 
        # This parameter is required.
        self.source = source
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: source CIDR block
        # 
        # - **group**: source address book
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.release is not None:
            result['Release'] = self.release

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

