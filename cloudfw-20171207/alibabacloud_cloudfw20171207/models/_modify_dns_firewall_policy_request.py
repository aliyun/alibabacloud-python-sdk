# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDnsFirewallPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        description: str = None,
        destination: str = None,
        destination_type: str = None,
        lang: str = None,
        priority: str = None,
        release: str = None,
        source: str = None,
        source_ip: str = None,
        source_type: str = None,
    ):
        # The action that is performed on traffic that hits the access control policy. Valid values:
        # 
        # - **accept**: Allow
        # 
        # - **drop**: Deny
        # 
        # - **log**: Monitor
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The description of the access control policy.
        self.description = description
        # The destination address in the access control policy.
        # 
        # - If **DestinationType** is set to net, **Destination** specifies the destination CIDR block. For example: 1.2.3.4/24
        # 
        # - If **DestinationType** is set to group, **Destination** specifies the name of the destination address book. For example: db_group
        # 
        # - If **DestinationType** is set to domain, **Destination** specifies the destination domain name. For example: \\*.aliyuncs.com
        # 
        # - If **DestinationType** is set to location, **Destination** specifies the destination region. For more information about the location codes, see the following description. For example: ["BJ11", "ZB"]
        self.destination = destination
        # The type of the destination address in the access control policy.
        # 
        # Valid values:
        # 
        # - **net**: destination CIDR block (CIDR address)
        # 
        # - **group**: destination address book
        # 
        # - **domain**: destination domain name
        self.destination_type = destination_type
        # The language of the content within the request and response. Valid values:-**zh**: Chinese-**en**: English
        self.lang = lang
        # The priority of the access control policy before the modification.
        self.priority = priority
        # The status of the access control policy. By default, the policy is enabled after it is created. Valid values:
        # 
        # - **true**: enables the access control policy.
        # 
        # - **false**: disables the access control policy.
        self.release = release
        self.source = source
        # The source IP address of the visitor.
        self.source_ip = source_ip
        # The type of the source address in the access control policy. Valid values:
        # 
        # - **net**: source CIDR block (CIDR)
        # 
        # - **group**: source address book
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

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

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

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

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

