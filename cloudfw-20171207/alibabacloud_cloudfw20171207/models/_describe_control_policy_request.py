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
        # The action that Cloud Firewall performs on the traffic that matches the access control policy. Valid values:
        # 
        # - **accept**: Allow
        # 
        # - **drop**: Deny
        # 
        # - **log**: Monitor
        # 
        # > If you do not specify this parameter, all action types are queried.
        self.acl_action = acl_action
        # The unique ID of the access control policy. You must specify at least one of AclUuid and Direction. If you specify AclUuid, you can query the policy by its ID.
        self.acl_uuid = acl_uuid
        # The page number of the current page returned for a paged query during paging.
        # 
        # Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy match is supported.
        # 
        # > If you do not specify this parameter, the descriptions of all policies are queried.
        self.description = description
        # The destination address in the access control policy. Fuzzy match is supported. The value of Destination varies based on the destination type (DestinationType).
        # 
        # - If DestinationType is set to `net`, the destination address is a CIDR block. Example: 10.0.3.0/24.
        # 
        # - If DestinationType is set to `domain`, the destination address is a domain name. Example: aliyun.
        # 
        # - If DestinationType is set to `group`, the destination address is the name of an address book. Example: db_group.
        # 
        # - If DestinationType is set to `location`, the destination address is an area name. For more information about the area positional encoding, see AddControlPolicy. Example: ["BJ11", "ZB"].
        # 
        # > If you do not specify this parameter in the Settings, all types of destination addresses are queried.
        self.destination = destination
        # The traffic direction controlled by the access control policy. Valid values: in (inbound) and out (outbound). You must specify at least one of Direction and AclUuid. If AclUuid is not specified, you must specify a non-empty Direction. Otherwise, ErrorParametersDirection is returned.
        self.direction = direction
        # The IP address version. Valid values:
        # 
        # - **4** (default): IPv4
        # 
        # - **6**: IPv6
        self.ip_version = ip_version
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The maximum number of entries to return on each page for a paged query during paging.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The protocol type of the traffic in the access control policy. Valid values:
        # 
        # - **TCP**
        # - **UDP**
        # - **ICMP**
        # - **ANY** (all protocol types)
        # > If you do not specify this parameter, all protocol types are queried.
        self.proto = proto
        # Specifies whether the access control policy is enabled. Valid values:
        # 
        # - **true**: The access control policy is enabled.
        # 
        # - **false**: The access control policy is disabled.
        self.release = release
        # The recurrence type of the Policy Validity Period for the access control policy. Valid values:
        # - **Permanent** (default): Always
        # - **None**: One-time
        # - **Daily**: Daily
        # - **Weekly**: Weekly
        # - **Monthly**: Monthly
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy match is supported. The value of Source varies based on the value of SourceType.
        # 
        # - If SourceType is set to `net`, the source address is a CIDR block. Example: 192.0.XX.XX/24.
        # 
        # - If SourceType is set to `group`, the source address is the name of a source address book. Example: db_group. If this parameter is left empty, all access sources are queried.
        # 
        # - If SourceType is set to `location`, the source address is a source region. Example: Beijing or beijing. Both Chinese and English region names are supported.
        # 
        # > If you do not specify this parameter, all types of access sources are queried.
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

